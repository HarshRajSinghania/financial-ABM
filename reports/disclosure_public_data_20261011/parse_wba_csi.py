"""Reproduce the WBA CSI snapshot CSVs and quality audit using only Python stdlib."""

import csv
import hashlib
import json
import math
import re
import statistics
import sys
import unicodedata
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / 'data/raw/disclosure_public_20261011'
OUT = ROOT / 'data/processed/disclosure_public_20261011'
REPORT = Path(__file__).resolve().parent
WORKBOOK = RAW / 'wba_csi_assessments_2021_2023_april2024_v2.xlsx'
EXPECTED_SHA256 = '6e94e0d739c5efc69a86e1b9d70e8480bad66e6521b9287a1feb0f613f13abda'
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
REL = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'
EXPORTS = {
    '1. Introduction': ('introduction_grid.csv', None),
    '2. Methodology': ('methodology_grid.csv', None),
    '3. Latest indicator scores': ('latest_indicator_scores.csv', 3),
    '4. Latest element scores': ('latest_element_scores.csv', 3),
    '5. Latest full assessment': ('latest_full_assessment.csv', 1),
}


def sha256(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def column_index(address):
    letters = re.match(r'[A-Z]+', address).group()
    result = 0
    for letter in letters:
        result = result * 26 + ord(letter) - 64
    return result - 1


def column_name(index):
    result = ''
    index += 1
    while index:
        index, remainder = divmod(index - 1, 26)
        result = chr(65 + remainder) + result
    return result


def read_sheet(archive, part, strings, metadata, formula_writer):
    with archive.open(part) as handle:
        for _, element in ET.iterparse(handle, events=('end',)):
            tag = element.tag.rsplit('}', 1)[-1]
            if tag == 'dimension':
                metadata['declared_dimension'] = element.get('ref')
            elif tag == 'mergeCell':
                metadata['merged_ranges'].append(element.get('ref'))
            elif tag == 'col' and element.get('hidden') == '1':
                metadata['hidden_columns'].append(dict(element.attrib))
            elif tag == 'row':
                row_number = int(element.get('r'))
                if element.get('hidden') == '1':
                    metadata['hidden_rows'].append(row_number)
                cells = {}
                for cell in element.findall('s:c', NS):
                    address = cell.get('r')
                    cell_type = cell.get('t', 'n')
                    metadata['cell_types'][cell_type] += 1
                    value = cell.find('s:v', NS)
                    text = value.text or '' if value is not None else ''
                    if cell_type == 's':
                        text = strings[int(text)] if text else ''
                    elif cell_type == 'inlineStr':
                        text = ''.join(t.text or '' for t in cell.findall('.//s:t', NS))
                    formula = cell.find('s:f', NS)
                    if formula is not None:
                        metadata['formula_count'] += 1
                        if value is None:
                            metadata['formulas_without_cached_value'] += 1
                        formula_writer.writerow([metadata['name'], address, formula.text or '', text, json.dumps(formula.attrib)])
                    if cell_type == 'e':
                        metadata['error_cells'].append({'cell': address, 'value': text})
                    cells[column_index(address)] = text
                metadata['xml_row_count'] += 1
                yield row_number, cells
                element.clear()


def read_csv(name):
    with (OUT / name).open(encoding='utf-8-sig', newline='') as handle:
        return list(csv.DictReader(handle))


def normalized_name(value):
    return ' '.join(unicodedata.normalize('NFKC', value).casefold().split())


def isin_valid(value):
    if not re.fullmatch(r'[A-Z]{2}[A-Z0-9]{9}[0-9]', value):
        return False
    digits = ''.join(str(ord(c) - 55) if c.isalpha() else c for c in value)
    total = 0
    for index, digit in enumerate(reversed(digits)):
        number = int(digit) * (2 if index % 2 else 1)
        total += number // 10 + number % 10
    return total % 10 == 0


def describe(values):
    ordered = sorted(values)
    def quantile(p):
        position = (len(ordered) - 1) * p
        lower = int(position)
        return ordered[lower] + (ordered[min(lower + 1, len(ordered) - 1)] - ordered[lower]) * (position - lower)
    return {
        'n': len(values), 'min': min(values), 'max': max(values),
        'mean': statistics.fmean(values), 'population_sd': statistics.pstdev(values),
        'q25_linear': quantile(.25), 'median': statistics.median(values), 'q75_linear': quantile(.75),
    } if values else {'n': 0}


def main():
    source_hash = sha256(WORKBOOK)
    if source_hash != EXPECTED_SHA256:
        raise ValueError('Source snapshot hash changed; review provenance before parsing.')
    metadata = []
    with zipfile.ZipFile(WORKBOOK) as archive, (OUT / 'formula_cells.csv').open('w', encoding='utf-8-sig', newline='') as formula_file:
        if archive.testzip() is not None:
            raise ValueError('Workbook ZIP CRC failure')
        formula_writer = csv.writer(formula_file)
        formula_writer.writerow(['sheet', 'excel_cell', 'formula', 'cached_value', 'formula_attributes'])
        strings = [''.join(t.text or '' for t in item.findall('.//s:t', NS)) for item in ET.fromstring(archive.read('xl/sharedStrings.xml'))]
        workbook = ET.fromstring(archive.read('xl/workbook.xml'))
        relations = {item.get('Id'): item.get('Target') for item in ET.fromstring(archive.read('xl/_rels/workbook.xml.rels'))}
        for sheet in workbook.find('s:sheets', NS):
            name = sheet.get('name')
            filename, header_row = EXPORTS[name]
            target = relations[sheet.get(REL)]
            part = target.lstrip('/') if target.startswith('/') else 'xl/' + target
            item = {
                'name': name, 'visibility': sheet.get('state', 'visible'), 'xml_part': part,
                'csv': filename, 'header_excel_row': header_row, 'rows_before_header': [],
                'merged_ranges': [], 'hidden_rows': [], 'hidden_columns': [],
                'cell_types': Counter(), 'xml_row_count': 0, 'formula_count': 0,
                'formulas_without_cached_value': 0, 'error_cells': [], 'data_row_count': 0,
                'omitted_empty_data_rows': [],
            }
            with (OUT / filename).open('w', encoding='utf-8-sig', newline='') as output:
                writer = csv.writer(output)
                for row_number, cells in read_sheet(archive, part, strings, item, formula_writer):
                    if header_row is None:
                        width = column_index(item['declared_dimension'].split(':')[-1]) + 1
                        if item['xml_row_count'] == 1:
                            writer.writerow(['_excel_row'] + [column_name(i) for i in range(width)])
                        writer.writerow([row_number] + [cells.get(i, '') for i in range(width)])
                        item['data_row_count'] += 1
                    elif row_number < header_row:
                        item['rows_before_header'].append({'excel_row': row_number, 'cells': {column_name(k): v for k, v in cells.items() if v}})
                    elif row_number == header_row:
                        width = max(cells) + 1
                        item['original_headers'] = [cells.get(i, '') for i in range(width)]
                        if len(set(item['original_headers'])) != width or '' in item['original_headers']:
                            raise ValueError('Blank/duplicate original header requires explicit review')
                        writer.writerow(item['original_headers'])
                    elif any(value for value in cells.values()):
                        if max(cells, default=0) >= width:
                            raise ValueError('Data beyond the original headers')
                        writer.writerow([cells.get(i, '') for i in range(width)])
                        item['data_row_count'] += 1
                    else:
                        item['omitted_empty_data_rows'].append(row_number)
            item['cell_types'] = dict(item['cell_types'])
            with (OUT / filename).open(encoding='utf-8-sig', newline='') as check:
                exported_rows = sum(1 for _ in csv.reader(check)) - 1
            if exported_rows != item['data_row_count']:
                raise ValueError('Export row count mismatch')
            metadata.append(item)
        core = ET.fromstring(archive.read('docProps/core.xml'))
        core_properties = {child.tag.rsplit('}', 1)[-1]: child.text for child in core}
        archive_info = {'members': len(archive.infolist()), 'uncompressed_bytes': sum(i.file_size for i in archive.infolist()), 'crc_valid': True}
    write_json(OUT / 'workbook_structure.json', {'source_sha256': source_hash, 'core_properties': core_properties, 'zip': archive_info, 'sheets': metadata})

    indicators = read_csv('latest_indicator_scores.csv')
    elements = read_csv('latest_element_scores.csv')
    indicator_by_id = {row['WBA ID']: row for row in indicators}
    element_by_id = {row['WBA ID']: row for row in elements}
    id_counts = Counter(row['WBA ID'] for row in indicators)
    names = defaultdict(list)
    isins = defaultdict(list)
    issues = []
    def issue(kind, sheet, excel_row, identifier, year, column, value, detail):
        issues.append([kind, sheet, excel_row, identifier, year, column, value, detail])
    for excel_row, row in enumerate(indicators, start=4):
        identifier = row['WBA ID']
        names[normalized_name(row['COMPANY NAME '])].append(identifier)
        isin = row['ISIN '].strip()
        if not isin:
            issue('missing_isin', '3. Latest indicator scores', excel_row, identifier, row['YEAR '], 'ISIN ', row['ISIN '], 'Do not infer private status from a missing identifier')
        else:
            isins[isin].append(identifier)
            if not isin_valid(isin):
                issue('invalid_isin_format_or_checksum', '3. Latest indicator scores', excel_row, identifier, row['YEAR '], 'ISIN ', row['ISIN '], 'Preserved; not auto-corrected or matched')
    duplicate_isins = {key: value for key, value in isins.items() if len(value) > 1}
    for isin, identifiers in duplicate_isins.items():
        for identifier in identifiers:
            row = indicator_by_id[identifier]
            issue('duplicate_isin', '3. Latest indicator scores', '', identifier, row['YEAR '], 'ISIN ', isin, '|'.join(identifiers))

    profiles = []
    numeric = {}
    year_scores = defaultdict(list)
    total_mismatches = []
    for filename, rows in [('latest_indicator_scores.csv', indicators), ('latest_element_scores.csv', elements)]:
        for field in rows[0]:
            counts = Counter(row[field] for row in rows)
            is_numeric = field == 'CSI Total (out of 20)' or field.startswith('CSI ')
            blank = sum(count for value, count in counts.items() if not value.strip())
            profiles.append([filename, field, len(rows), blank, len(counts), json.dumps(counts.most_common(8), ensure_ascii=False)])
            if filename == 'latest_indicator_scores.csv' and is_numeric:
                values = []
                for excel_row, row in enumerate(rows, start=4):
                    try:
                        value = float(row[field])
                    except ValueError:
                        issue('nonnumeric_score', '3. Latest indicator scores', excel_row, row['WBA ID'], row['YEAR '], field, row[field], 'No imputation')
                        continue
                    upper = 20 if field == 'CSI Total (out of 20)' else 2 if field in ('CSI 4', 'CSI 5') else 1
                    if not math.isfinite(value) or not 0 <= value <= upper:
                        issue('score_out_of_documented_bounds', '3. Latest indicator scores', excel_row, row['WBA ID'], row['YEAR '], field, row[field], f'[0,{upper}]')
                    values.append(value)
                numeric[field] = describe(values) | {'observed_values': dict(sorted(Counter(values).items())), 'documented_upper': upper}
    for row in indicators:
        total = float(row['CSI Total (out of 20)'])
        year_scores[row['YEAR ']].append(total)
        reconstructed = sum(float(row[f'CSI {i}']) for i in range(1, 19))
        if abs(total - reconstructed) > 1e-9:
            total_mismatches.append({'wba_id': row['WBA ID'], 'reported': total, 'sum_of_already_weighted_indicator_columns': reconstructed})
    shared_fields = [field for field in indicators[0] if field in elements[0]]
    cross_sheet_mismatches = []
    for identifier, row in indicator_by_id.items():
        for field in shared_fields:
            other = element_by_id.get(identifier, {}).get(field)
            if row[field] != other:
                cross_sheet_mismatches.append({'wba_id': identifier, 'field': field, 'indicator_value': row[field], 'element_value': other})

    long_keys = Counter()
    long_years = Counter()
    long_status = Counter()
    long_missing = Counter()
    long_coverage = defaultdict(set)
    long_score_mismatches = []
    with (OUT / 'latest_full_assessment.csv').open(encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        for excel_row, row in enumerate(reader, start=2):
            identifier, year, code = row['WBA ID'], row['Year'], row['Indicator element']
            long_keys[identifier, year, code] += 1
            long_years[year] += 1
            long_status[row['Score']] += 1
            long_coverage[identifier].add(code)
            for field, value in row.items():
                if not value.strip():
                    long_missing[field] += 1
            match = re.fullmatch(r'CSI\.(\d+)\.E([A-Z])', code)
            wide_field = str(int(match.group(1))) + match.group(2).lower() if match else None
            expected = element_by_id.get(identifier, {})
            if expected.get('YEAR ') != year or expected.get(wide_field) != row['Score']:
                long_score_mismatches.append({'excel_row': excel_row, 'wba_id': identifier, 'year': year, 'element': code, 'score': row['Score'], 'wide_score': expected.get(wide_field), 'wide_year': expected.get('YEAR ')})
    duplicate_long = [{'wba_id': key[0], 'year': key[1], 'element': key[2], 'count': count} for key, count in long_keys.items() if count > 1]
    with (OUT / 'column_quality.csv').open('w', encoding='utf-8-sig', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(['file', 'original_field', 'rows', 'blank_or_whitespace', 'distinct_including_blank', 'top_8_raw_values_json'])
        writer.writerows(profiles)
    with (OUT / 'identifier_issues.csv').open('w', encoding='utf-8-sig', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(['issue', 'sheet', 'excel_row', 'wba_id', 'assessment_year', 'original_field', 'original_value', 'detail'])
        writer.writerows(issues)
    summary = {
        'status': 'parsed_and_profiled_not_calibrated', 'source_sha256': source_hash,
        'scope': 'Social CSI; latest assessment per company across 2021-2023, not a balanced panel, a common-year cross-section, comprehensive ESG, or latent truth.',
        'transformations': 'UTF-8 BOM CSV; original header whitespace, string case, numeric XML lexemes and cell text retained. No imputation, deduplication, date conversion, formula evaluation, or merged-cell filling. Rich text formatting is flattened; formulas and merged ranges are preserved separately; original XLSX remains authoritative.',
        'company_rows': len(indicators), 'unique_wba_ids': len(id_counts),
        'duplicate_wba_ids': {key: count for key, count in id_counts.items() if count > 1},
        'duplicate_normalized_names': {key: value for key, value in names.items() if len(value) > 1},
        'assessment_year_counts': dict(sorted(Counter(row['YEAR '] for row in indicators).items())),
        'country_counts': dict(Counter(row['COUNTRY'] for row in indicators).most_common()),
        'region_counts': dict(Counter(row['REGION'] for row in indicators).most_common()),
        'industry_counts': dict(Counter(row['INDUSTRY'] for row in indicators).most_common()),
        'isin': {'nonblank_rows': sum(map(len, isins.values())), 'blank_rows': len(indicators) - sum(map(len, isins.values())), 'unique_nonblank_values': len(isins), 'duplicate_groups': duplicate_isins, 'format_or_checksum_invalid_rows': sum(row[0] == 'invalid_isin_format_or_checksum' for row in issues), 'matching_status': 'unmatched; ISIN is not CIK; duplicate or missing identifiers require entity review'},
        'numeric_scores': numeric, 'total_score_by_assessment_year': {year: describe(values) for year, values in sorted(year_scores.items())},
        'weighted_total_mismatches': total_mismatches, 'wide_sheet_shared_field_mismatches': cross_sheet_mismatches,
        'long_assessment': {'rows': sum(long_keys.values()), 'unique_keys': len(long_keys), 'duplicate_keys': duplicate_long, 'year_row_counts': dict(sorted(long_years.items())), 'score_counts': dict(long_status), 'blank_counts_by_original_field': dict(long_missing), 'elements_per_company_counts': dict(Counter(len(v) for v in long_coverage.values())), 'wide_score_or_year_mismatches': long_score_mismatches},
        'mechanical': {'source_hash_match': True, 'zip_crc_valid': True, 'all_export_row_counts_checked': True, 'formula_cells': sum(item['formula_count'] for item in metadata), 'formulas_without_cached_value': sum(item['formulas_without_cached_value'] for item in metadata), 'excel_error_cells': sum(len(item['error_cells']) for item in metadata)},
        'issue_counts': dict(Counter(row[0] for row in issues)),
        'cautions': ['CSI 4 and CSI 5 columns already contain double weights: do not weight them a second time.', 'Financial System Benchmark modifies CSI 3 and element 5a; benchmark membership is not an explicit table field.', 'Published evidence-based scores do not independently identify real capability, misrepresentation, audit probability, investment costs, financing response, or policy causal effects.', 'A pooled mean across assessment years is descriptive only; select a year/cohort and verify benchmark comparability before calibration.'],
    }
    write_json(REPORT / 'quality_summary.json', summary)
    artifacts = []
    for path in sorted(path for folder in (RAW, OUT, REPORT) for path in folder.iterdir() if path.is_file() and path.name != 'output_manifest.json'):
        artifacts.append({'path': path.relative_to(ROOT).as_posix(), 'bytes': path.stat().st_size, 'sha256': sha256(path)})
    write_json(REPORT / 'output_manifest.json', {'generated_utc': datetime.now(timezone.utc).isoformat(), 'python': sys.version, 'source_sha256': source_hash, 'self_hash_excluded': True, 'artifacts': artifacts})
    print(json.dumps({'companies': len(indicators), 'years': summary['assessment_year_counts'], 'long_rows': summary['long_assessment']['rows'], 'isin': summary['isin'], 'issue_counts': summary['issue_counts'], 'total_mismatches': len(total_mismatches), 'wide_mismatches': len(cross_sheet_mismatches), 'long_mismatches': len(long_score_mismatches)}, ensure_ascii=True))


if __name__ == '__main__':
    main()
