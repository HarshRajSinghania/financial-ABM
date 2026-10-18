# Working paper (English draft)

`main.tex` is the English working-paper draft on the stage F experiment. Red bracketed text in the PDF marks placeholders: the author line and the three robustness supplements still running.

Build from this directory:

```sh
python make_figures.py
latexmk -pdf main.tex
```

`make_figures.py` reads only committed analysis files under `reports/`. Entries in `references.bib` were written from memory or from the repository's evidence review; check each against the publisher page before circulating.
