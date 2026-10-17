'use strict';
// Policy desk visuals: the firm sphere, the decision spectrogram, avatars and sparklines.
// Drawing only. Every number arrives from app.js, which takes it from core.js; every label
// arrives already translated.
(function (root) {
  const TAU = Math.PI * 2;
  const GOLDEN = Math.PI * (3 - Math.sqrt(5));
  const clamp = (x, lo, hi) => Math.min(hi, Math.max(lo, x));
  const ease = t => 1 - (1 - t) ** 3;
  const rgba = (hex, a) => {
    const n = parseInt(hex.slice(1, 7), 16);
    return `rgba(${(n >> 16) & 255},${(n >> 8) & 255},${n & 255},${a})`;
  };
  const mix = (a, b, t) => {
    const p = parseInt(a.slice(1, 7), 16), q = parseInt(b.slice(1, 7), 16);
    const c = s => Math.round(((p >> s) & 255) * (1 - t) + ((q >> s) & 255) * t);
    return `#${((c(16) << 16) | (c(8) << 8) | c(0)).toString(16).padStart(6, '0')}`;
  };

  // Size a canvas backing store to its CSS box at the device pixel ratio (capped at 2).
  const fit = canvas => {
    const dpr = Math.min(root.devicePixelRatio || 1, 2);
    const box = canvas.getBoundingClientRect();
    const width = Math.max(1, Math.round(box.width * dpr)), height = Math.max(1, Math.round(box.height * dpr));
    if (canvas.width !== width || canvas.height !== height) { canvas.width = width; canvas.height = height; }
    const ctx = canvas.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx, w: box.width, h: box.height, dpr };
  };
  const setSpacing = (ctx, value) => { if ('letterSpacing' in ctx) ctx.letterSpacing = value; };

  // -- the firm sphere -----------------------------------------------------------------------
  // Firms sit in latitude bands by size class (large at the crown), spread by the golden angle
  // inside each band, so equal areas of the sphere hold equal numbers of firms.
  const layoutFirms = (groups, n) => {
    const total = groups.reduce((s, g) => s + g.length, 0);
    const top = 0.94, bottom = -0.94, gap = 0.06;
    const span = top - bottom - gap * (groups.length - 1);
    const points = new Array(n);
    const bands = [];
    let y0 = top, counter = 0;
    for (const group of groups) {
      const height = span * group.length / total;
      group.forEach((i, j) => {
        const y = y0 - height * (j + 0.5) / group.length;
        const r = Math.sqrt(1 - y * y), theta = counter++ * GOLDEN;
        points[i] = { x: r * Math.cos(theta), y, z: r * Math.sin(theta) };
      });
      bands.push({ top: y0, bottom: y0 - height, count: group.length });
      y0 -= height + gap;
    }
    return { points, bands };
  };

  const createSphere = (canvas, options) => {
    const reduced = !!options.reduced;
    const s = {
      points: [], bands: [], radii: [], colors: [], palette: options.palette, ink: options.ink, violet: options.violet,
      surface: options.surface, yaw: 0.9, pitch: 0.36, vx: 0, spin: 0.1, dragging: false, lastInteraction: -1e9,
      selected: -1, hover: -1, ripples: [], beams: [], boosts: new Map(), projected: [], bandLabels: [],
      geometry: null, last: 0, time: 0, pointer: null, orbit: { regulator: null, investors: null },
    };
    const meridianColors = Array.from({ length: 20 }, (_, m) => mix(options.violet, options.pink, 0.5 - 0.5 * Math.cos(m / 20 * TAU)));

    const view = () => {
      const cy = Math.cos(s.yaw), sy = Math.sin(s.yaw), cp = Math.cos(s.pitch), sp = Math.sin(s.pitch);
      const g = s.geometry;
      // Spin about the vertical axis, then tilt the north pole towards the viewer.
      const project = (x, y, z) => {
        const x1 = x * cy + z * sy, z1 = -x * sy + z * cy;
        return { x: g.cx + g.r * x1, y: g.cy - g.r * (y * cp - z1 * sp), z: y * sp + z1 * cp };
      };
      // Orbits do not spin with the firms; only the tilt applies.
      const projectFixed = (x, y, z) => ({ x: g.cx + g.r * x, y: g.cy - g.r * (y * cp - z * sp), z: y * sp + z * cp });
      return { project, projectFixed };
    };

    // Split a projected 3-D curve into front and back paths, cutting exactly at the limb.
    const curve = (samples, front, back) => {
      let previous = null;
      for (const p of samples) {
        if (!previous) { (p.z > 0 ? front : back).moveTo(p.x, p.y); previous = p; continue; }
        if ((previous.z > 0) !== (p.z > 0)) {
          const t = previous.z / (previous.z - p.z);
          const x = previous.x + (p.x - previous.x) * t, y = previous.y + (p.y - previous.y) * t;
          (previous.z > 0 ? front : back).lineTo(x, y);
          (p.z > 0 ? front : back).moveTo(x, y);
        }
        (p.z > 0 ? front : back).lineTo(p.x, p.y);
        previous = p;
      }
    };

    const orbitPoint = (radius, tiltX, tiltZ, angle) => {
      let x = radius * Math.cos(angle), y = 0, z = radius * Math.sin(angle);
      const cx = Math.cos(tiltX), sx = Math.sin(tiltX);
      [y, z] = [y * cx - z * sx, y * sx + z * cx];
      const cz = Math.cos(tiltZ), sz = Math.sin(tiltZ);
      [x, y] = [x * cz - y * sz, x * sz + y * cz];
      return { x, y, z };
    };
    const ORBITS = [
      { radius: 1.3, tiltX: 0.36, tiltZ: -0.2, speed: 0.3, offset: 2.4 },
      { radius: 1.18, tiltX: -0.52, tiltZ: 0.32, speed: 0.045, offset: 4.1 },
    ];

    const drawWires = (ctx, now) => {
      const g = s.geometry;
      if (!g.ports.length) return;
      g.ports.forEach((port, k) => {
        if (port.x > g.cx - g.r) return;
        const n = g.ports.length;
        const angle = Math.PI - 0.62 + 1.24 * (n === 1 ? 0.5 : k / (n - 1));
        const tx = g.cx + g.r * Math.cos(angle) * 1.01, ty = g.cy - g.r * Math.sin(angle) * 1.01;
        const c1x = port.x + Math.max(40, (tx - port.x) * 0.45), c2x = tx - Math.max(30, (tx - port.x) * 0.35);
        const boost = clamp(1 - (now - (s.boosts.get(k) ?? -1e9)) / 1800, 0, 1);
        ctx.beginPath();
        ctx.moveTo(port.x, port.y);
        ctx.bezierCurveTo(c1x, port.y, c2x, ty, tx, ty);
        ctx.strokeStyle = rgba(s.violet, 0.2 + 0.45 * boost);
        ctx.lineWidth = 1 + 0.8 * boost;
        ctx.stroke();
        if (reduced) return;
        const packets = 2 + Math.round(4 * boost);
        for (let m = 0; m < packets; m++) {
          const t = ((now / 1000) * (0.2 + 0.4 * boost) + k * 0.137 + m / packets) % 1;
          const u = 1 - t;
          const x = u * u * u * port.x + 3 * u * u * t * c1x + 3 * u * t * t * c2x + t * t * t * tx;
          const y = u * u * u * port.y + 3 * u * u * t * port.y + 3 * u * t * t * ty + t * t * t * ty;
          ctx.beginPath();
          ctx.arc(x, y, 1.6 + 1.2 * boost, 0, TAU);
          ctx.fillStyle = rgba(s.violet, Math.sin(Math.PI * t) * (0.55 + 0.45 * boost));
          ctx.fill();
        }
      });
    };

    const draw = now => {
      const { ctx, w, h } = fit(canvas);
      ctx.clearRect(0, 0, w, h);
      const g = s.geometry;
      if (!g || !s.points.length) return;
      const { project, projectFixed } = view();
      const R = g.r;
      drawWires(ctx, now);

      // Orbits: sample once, draw the far half before the sphere and the near half after it.
      const orbitPaths = ORBITS.map(o => {
        const front = new Path2D(), back = new Path2D();
        const samples = [];
        for (let k = 0; k <= 120; k++) { const p = orbitPoint(o.radius, o.tiltX, o.tiltZ, k / 120 * TAU); samples.push(projectFixed(p.x, p.y, p.z)); }
        curve(samples, front, back);
        return { front, back };
      });
      ctx.lineWidth = 1;
      orbitPaths.forEach((o, k) => { ctx.strokeStyle = k ? 'rgba(82,81,78,0.14)' : rgba(s.violet, 0.16); ctx.stroke(o.back); });

      // Wireframe paths.
      const meridians = meridianColors.map((color, m) => {
        const front = new Path2D(), back = new Path2D();
        const lon = m / meridianColors.length * TAU, samples = [];
        for (let k = 0; k <= 40; k++) {
          const lat = -Math.PI / 2 + Math.PI * k / 40;
          samples.push(project(Math.cos(lat) * Math.cos(lon), Math.sin(lat), Math.cos(lat) * Math.sin(lon)));
        }
        curve(samples, front, back);
        return { color, front, back };
      });
      const parallel = y => {
        const front = new Path2D(), back = new Path2D(), r = Math.sqrt(Math.max(0, 1 - y * y)), samples = [];
        for (let k = 0; k <= 72; k++) { const a = k / 72 * TAU; samples.push(project(r * Math.cos(a), y, r * Math.sin(a))); }
        curve(samples, front, back);
        return { front, back };
      };
      const parallels = [-0.866, -0.5, 0, 0.5, 0.866, -0.966, -0.707, -0.259, 0.259, 0.707, 0.966].map(parallel);
      const boundaries = s.bands.slice(0, -1).map(band => parallel(band.bottom - 0.03));

      for (const m of meridians) { ctx.strokeStyle = rgba(m.color, 0.09); ctx.stroke(m.back); }
      ctx.strokeStyle = 'rgba(60,58,80,0.06)';
      for (const p of parallels) ctx.stroke(p.back);

      // Project firms; draw the far side first.
      const projected = s.projected;
      for (let i = 0; i < s.points.length; i++) {
        const p = s.points[i];
        const q = project(p.x, p.y, p.z);
        q.i = i;
        q.r = s.radii[i] * (q.z > 0 ? 0.88 + 0.22 * q.z : 0.7);
        projected[i] = q;
      }
      const order = projected.slice().sort((a, b) => a.z - b.z);
      for (const q of order) {
        if (q.z > 0) break;
        ctx.beginPath();
        ctx.arc(q.x, q.y, q.r, 0, TAU);
        ctx.fillStyle = rgba(s.palette[s.colors[q.i] ?? 3], 0.22);
        ctx.fill();
      }

      // Glass: lifts the near hemisphere off the far one.
      const glass = ctx.createRadialGradient(g.cx - R * 0.35, g.cy - R * 0.4, R * 0.1, g.cx, g.cy, R);
      glass.addColorStop(0, 'rgba(255,255,255,0.82)');
      glass.addColorStop(0.7, 'rgba(255,255,255,0.62)');
      glass.addColorStop(1, rgba(s.violet, 0.07));
      ctx.beginPath();
      ctx.arc(g.cx, g.cy, R, 0, TAU);
      ctx.fillStyle = glass;
      ctx.fill();
      ctx.lineWidth = 6;
      ctx.strokeStyle = rgba(s.violet, 0.05);
      ctx.stroke();
      ctx.lineWidth = 1;
      ctx.strokeStyle = 'rgba(11,11,11,0.16)';
      ctx.stroke();

      for (const m of meridians) { ctx.strokeStyle = rgba(m.color, 0.4); ctx.stroke(m.front); }
      ctx.strokeStyle = 'rgba(60,58,80,0.11)';
      for (const p of parallels) ctx.stroke(p.front);
      ctx.strokeStyle = 'rgba(11,11,11,0.22)';
      ctx.lineWidth = 1.2;
      for (const b of boundaries) ctx.stroke(b.front);
      ctx.lineWidth = 1;

      // Leader from the selected firm to its ticket, under the near firms.
      const chosenPoint = s.selected >= 0 ? projected[s.selected] : null;
      if (chosenPoint && g.ticket && g.ticket.x > g.cx + R) {
        const alpha = chosenPoint.z > 0 ? 0.5 : 0.14;
        ctx.beginPath();
        ctx.moveTo(chosenPoint.x, chosenPoint.y);
        ctx.bezierCurveTo(chosenPoint.x + 90, chosenPoint.y, g.ticket.x - 90, g.ticket.y, g.ticket.x, g.ticket.y);
        ctx.strokeStyle = rgba(s.ink, alpha);
        ctx.lineWidth = 1;
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(g.ticket.x, g.ticket.y, 3, 0, TAU);
        ctx.fillStyle = rgba(s.ink, alpha + 0.2);
        ctx.fill();
      }

      // Near firms: a soft halo for the two actions, then the dot with a surface ring.
      for (const q of order) {
        if (q.z <= 0) continue;
        const color = s.palette[s.colors[q.i] ?? 3];
        if (s.colors[q.i] === 0 || s.colors[q.i] === 1) {
          ctx.beginPath();
          ctx.arc(q.x, q.y, q.r * 2.3, 0, TAU);
          ctx.fillStyle = rgba(color, 0.13 * q.z + 0.03);
          ctx.fill();
        }
        ctx.beginPath();
        ctx.arc(q.x, q.y, q.r, 0, TAU);
        ctx.fillStyle = color;
        ctx.fill();
        ctx.lineWidth = 1.3;
        ctx.strokeStyle = s.surface;
        ctx.stroke();
      }

      // Ripples where a firm changed its choice; beams where an audit caught one.
      s.ripples = s.ripples.filter(r => now - r.t0 < 900);
      for (const r of s.ripples) {
        const q = projected[r.i];
        if (!q || q.z <= 0 || now < r.t0) continue;
        const p = (now - r.t0) / 900;
        ctx.beginPath();
        ctx.arc(q.x, q.y, q.r + 3 + 16 * ease(p), 0, TAU);
        ctx.strokeStyle = rgba(r.color, 0.75 * (1 - p));
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }
      const regulator = s.orbit.regulator;
      s.beams = s.beams.filter(b => now - b.t0 < 1300);
      for (const b of s.beams) {
        const q = projected[b.i];
        if (!q || now < b.t0) continue;
        const p = (now - b.t0) / 1300;
        if (regulator) {
          const grad = ctx.createLinearGradient(regulator.x, regulator.y, q.x, q.y);
          grad.addColorStop(0, rgba(s.violet, 0.0));
          grad.addColorStop(1, rgba(s.ink, 0.75 * (1 - p)));
          ctx.beginPath();
          ctx.moveTo(regulator.x, regulator.y);
          ctx.lineTo(q.x, q.y);
          ctx.strokeStyle = grad;
          ctx.lineWidth = 1.3;
          ctx.stroke();
        }
        ctx.beginPath();
        ctx.arc(q.x, q.y, q.r + 2 + 9 * ease(p), 0, TAU);
        ctx.strokeStyle = rgba(s.ink, 0.85 * (1 - p));
        ctx.lineWidth = 2;
        ctx.stroke();
      }
      ctx.lineWidth = 1;
      orbitPaths.forEach((o, k) => { ctx.strokeStyle = k ? 'rgba(82,81,78,0.3)' : rgba(s.violet, 0.42); ctx.stroke(o.front); });

      // Band labels at the right limb of each latitude band.
      if (s.bandLabels.length && g.cx + R + 120 < g.right) {
        ctx.font = '600 10px Bahnschrift, "DIN Alternate", "Segoe UI", "Microsoft YaHei UI", sans-serif';
        setSpacing(ctx, '1.2px');
        ctx.textBaseline = 'middle';
        s.bands.forEach((band, k) => {
          const y = (band.top + band.bottom) / 2, lat = Math.asin(clamp(y, -1, 1));
          const ax = g.cx + R * Math.cos(lat), ay = g.cy - R * Math.sin(lat) * Math.cos(s.pitch);
          const lx = g.cx + R + 26;
          ctx.beginPath();
          ctx.moveTo(ax + 4, ay);
          ctx.lineTo(lx - 6, ay);
          ctx.strokeStyle = 'rgba(11,11,11,0.28)';
          ctx.stroke();
          ctx.beginPath();
          ctx.arc(ax + 2, ay, 1.8, 0, TAU);
          ctx.fillStyle = s.ink;
          ctx.fill();
          ctx.fillStyle = 'rgba(82,81,78,1)';
          ctx.fillText(s.bandLabels[k] ?? '', lx, ay);
        });
        setSpacing(ctx, '0px');
      }

      // Selection and hover.
      const ring = (i, alpha, extra) => {
        const q = projected[i];
        if (!q) return null;
        ctx.beginPath();
        ctx.arc(q.x, q.y, q.r + extra, 0, TAU);
        ctx.strokeStyle = rgba(s.ink, q.z > 0 ? alpha : alpha * 0.3);
        ctx.lineWidth = 1.6;
        ctx.stroke();
        return q;
      };
      if (s.hover >= 0 && s.hover !== s.selected) ring(s.hover, 0.6, 3.5);
      if (s.selected >= 0) ring(s.selected, 1, 4.5);

      // Orbiting characters (DOM): the regulator patrols; investors doze on the inner orbit.
      ['regulator', 'investors'].forEach((key, k) => {
        const element = options.orbiters?.[key];
        if (!element) return;
        const o = ORBITS[k];
        const p = orbitPoint(o.radius, o.tiltX, o.tiltZ, o.offset + (reduced ? 0 : s.time * o.speed));
        const q = projectFixed(p.x, p.y, p.z);
        const hidden = q.z < 0 && Math.hypot(q.x - g.cx, q.y - g.cy) < R;
        s.orbit[key] = q;
        element.style.transform = `translate(${q.x.toFixed(1)}px, ${q.y.toFixed(1)}px) scale(${(0.82 + 0.18 * (q.z + 1) / 2).toFixed(3)})`;
        element.style.opacity = hidden ? '0.28' : '1';
      });
    };

    const frame = now => {
      const dt = s.last ? Math.min(0.05, (now - s.last) / 1000) : 0;
      s.last = now;
      if (!reduced) s.time += dt;
      if (!s.dragging) {
        if (Math.abs(s.vx) > 1e-4) { s.yaw += s.vx; s.vx *= 0.93; }
        else if (!reduced && now - s.lastInteraction > 1600) s.yaw += s.spin * dt;
      }
      draw(now);
    };

    // Pointer: drag to rotate, hover for a tooltip, click to select.
    const local = event => { const box = canvas.getBoundingClientRect(); return { x: event.clientX - box.left, y: event.clientY - box.top }; };
    const nearest = (at, limit) => {
      let best = -1, distance = limit * limit;
      for (const q of s.projected) {
        if (!q || q.z <= 0) continue;
        const d = (q.x - at.x) ** 2 + (q.y - at.y) ** 2;
        if (d < distance) { distance = d; best = q.i; }
      }
      return best;
    };
    const onSphere = at => s.geometry && Math.hypot(at.x - s.geometry.cx, at.y - s.geometry.cy) < s.geometry.r * 1.12;
    canvas.addEventListener('pointerdown', event => {
      const at = local(event);
      if (!onSphere(at)) return;
      s.pointer = { id: event.pointerId, x: at.x, y: at.y, moved: 0, t: performance.now() };
      s.dragging = true;
      s.vx = 0;
      canvas.setPointerCapture(event.pointerId);
      canvas.classList.add('dragging');
    });
    canvas.addEventListener('pointermove', event => {
      const at = local(event);
      if (s.dragging && s.pointer && event.pointerId === s.pointer.id) {
        const dx = at.x - s.pointer.x, dy = at.y - s.pointer.y;
        s.pointer.moved += Math.abs(dx) + Math.abs(dy);
        s.yaw += dx * 0.0065;
        s.pitch = clamp(s.pitch + dy * 0.0045, 0.02, 0.9);
        s.vx = dx * 0.0065;
        s.pointer.x = at.x; s.pointer.y = at.y;
        s.lastInteraction = performance.now();
        options.onHover?.(-1, event);
        return;
      }
      const i = onSphere(at) ? nearest(at, 14) : -1;
      if (i !== s.hover) s.hover = i;
      canvas.style.cursor = i >= 0 ? 'pointer' : '';
      options.onHover?.(i, event);
    });
    const release = event => {
      if (!s.pointer || event.pointerId !== s.pointer.id) return;
      const click = s.pointer.moved < 5;
      s.dragging = false;
      s.pointer = null;
      canvas.classList.remove('dragging');
      s.lastInteraction = performance.now();
      if (click) {
        s.vx = 0;
        const i = nearest(local(event), 18);
        if (i >= 0) options.onSelect?.(i);
      }
    };
    canvas.addEventListener('pointerup', release);
    canvas.addEventListener('pointercancel', release);
    canvas.addEventListener('pointerleave', () => { if (!s.dragging) { s.hover = -1; options.onHover?.(-1); } });

    return {
      setFirms(groups, radii) {
        const layout = layoutFirms(groups, radii.length);
        s.points = layout.points; s.bands = layout.bands; s.radii = radii;
        s.projected = new Array(radii.length);
      },
      setColors(colors, { ripple = false } = {}) {
        if (ripple && !reduced) {
          const now = performance.now();
          for (let i = 0; i < colors.length; i++) {
            if (s.colors[i] !== undefined && s.colors[i] !== colors[i] && colors[i] !== 3) {
              s.ripples.push({ i, t0: now + Math.random() * 220, color: s.palette[colors[i]] });
            }
          }
        }
        s.colors = Array.from(colors);
      },
      beam(firms) { if (reduced) return; const now = performance.now(); firms.forEach((i, k) => s.beams.push({ i, t0: now + k * 120 })); },
      boost(k) { s.boosts.set(k, performance.now()); },
      select(i) { s.selected = i; },
      setBandLabels(labels) { s.bandLabels = labels; },
      setGeometry(geometry) { s.geometry = geometry; },
      frame,
      draw: () => draw(performance.now()),
    };
  };

  // -- the decision spectrogram ----------------------------------------------------------------
  const spectrogram = (canvas, d) => {
    const { ctx, w, h, dpr } = fit(canvas);
    ctx.clearRect(0, 0, w, h);
    const left = 46, right = 4, top = 30, bottom = 20, gap = 5;
    const periods = d.actions.length, rows = d.order.length;
    const groupGaps = d.groupStarts.length - 1;
    const cw = (w - left - right) / periods;
    const rh = (h - top - bottom - gap * groupGaps) / rows;
    const snap = v => Math.round(v * dpr) / dpr;
    const rowTop = new Float64Array(rows + 1);
    let group = 0;
    for (let j = 0; j <= rows; j++) {
      while (group + 1 < d.groupStarts.length && j >= d.groupStarts[group + 1]) group++;
      rowTop[j] = top + j * rh + group * gap;
    }
    const columnX = k => snap(left + k * cw);
    for (let k = 0; k < periods; k++) {
      const x0 = columnX(k), x1 = columnX(k + 1) - Math.min(1, cw * 0.12);
      const future = k > d.current;
      ctx.globalAlpha = future ? 0.13 : 1;
      const actions = d.actions[k];
      let j = 0;
      while (j < rows) {
        let g0 = 0;
        while (g0 + 1 < d.groupStarts.length && j >= d.groupStarts[g0 + 1]) g0++;
        const groupEnd = d.groupStarts[g0 + 1] ?? rows;
        const color = actions[d.order[j]];
        let end = j + 1;
        while (end < groupEnd && actions[d.order[end]] === color) end++;
        ctx.fillStyle = d.palette[color];
        const y0 = snap(rowTop[j]), y1 = snap(rowTop[end - 1] + rh);
        ctx.fillRect(x0, y0, x1 - x0, Math.max(1 / dpr, y1 - y0));
        j = end;
      }
      // Audit hits: a ringed dot in the cell, visible at any row height.
      if (!future) {
        const caught = d.detections[k];
        for (let r = 0; r < rows; r++) {
          if (!caught[d.order[r]]) continue;
          const cx = (x0 + x1) / 2, cy = rowTop[r] + rh / 2;
          ctx.beginPath();
          ctx.arc(cx, cy, Math.min(2.6, cw * 0.32), 0, TAU);
          ctx.fillStyle = d.surface;
          ctx.fill();
          ctx.lineWidth = 1.4;
          ctx.strokeStyle = d.ink;
          ctx.stroke();
        }
      }
    }
    ctx.globalAlpha = 1;
    ctx.font = '600 9.5px Bahnschrift, "DIN Alternate", "Segoe UI", "Microsoft YaHei UI", sans-serif';
    ctx.textBaseline = 'middle';
    setSpacing(ctx, '0.8px');
    // Size-class labels with brackets.
    d.groupStarts.forEach((start, k) => {
      const end = (d.groupStarts[k + 1] ?? rows) - 1;
      const y0 = rowTop[start], y1 = rowTop[end] + rh;
      ctx.fillStyle = 'rgba(82,81,78,1)';
      ctx.textAlign = 'right';
      ctx.fillText(d.groupLabels[k] ?? '', left - 9, (y0 + y1) / 2);
      ctx.fillRect(left - 5, y0, 1, y1 - y0);
    });
    // Policy switch.
    if (d.switchK > 0 && d.switchK < periods) {
      const x = columnX(d.switchK) - 0.5;
      ctx.fillStyle = d.violet;
      ctx.fillRect(x - 0.5, 3, 1.5, h - bottom - 1);
      ctx.textAlign = 'left';
      ctx.textBaseline = 'alphabetic';
      ctx.fillText(d.switchLabel.toUpperCase(), x + 5, 11);
    }
    // Playhead.
    if (d.current >= 0 && d.current < periods) {
      const x0 = columnX(d.current) - 1, x1 = columnX(d.current + 1);
      ctx.strokeStyle = d.ink;
      ctx.lineWidth = 1.2;
      ctx.strokeRect(x0, top - 2, x1 - x0, rowTop[rows - 1] + rh - top + 4);
      ctx.beginPath();
      ctx.moveTo((x0 + x1) / 2 - 4.5, top - 12);
      ctx.lineTo((x0 + x1) / 2 + 4.5, top - 12);
      ctx.lineTo((x0 + x1) / 2, top - 5);
      ctx.fillStyle = d.ink;
      ctx.fill();
    }
    // Selected firm: ticks on both edges.
    if (d.selectedRow >= 0) {
      const y = rowTop[d.selectedRow] + rh / 2;
      ctx.fillStyle = d.ink;
      ctx.beginPath(); ctx.moveTo(left - 1, y); ctx.lineTo(left - 6, y - 4); ctx.lineTo(left - 6, y + 4); ctx.fill();
      ctx.beginPath(); ctx.moveTo(w - right + 1, y); ctx.lineTo(w, y - 4); ctx.lineTo(w, y + 4); ctx.fill();
      ctx.fillStyle = 'rgba(11,11,11,0.35)';
      ctx.fillRect(left, y - 0.5, w - left - right, 1);
    }
    // Year axis.
    ctx.textAlign = 'center';
    ctx.textBaseline = 'alphabetic';
    ctx.fillStyle = 'rgba(137,135,129,1)';
    ctx.font = '500 9.5px "JetBrains Mono", "Cascadia Mono", Consolas, monospace';
    setSpacing(ctx, '0px');
    for (let year = 0; year * 252 <= d.days; year += 2) {
      const x = left + (year * 252 / d.interval) * cw;
      ctx.fillRect(x, h - bottom + 2, 1, 4);
      ctx.fillText(String(year), x, h - 4);
    }
    ctx.textAlign = 'right';
    ctx.fillText(d.yearLabel, w - right, h - 4);
    return {
      hit(x, y) {
        const k = Math.floor((x - left) / cw);
        if (k < 0 || k >= periods || y < top || y > rowTop[rows - 1] + rh) return null;
        let lo = 0, hi = rows - 1;
        while (lo < hi) { const mid = (lo + hi + 1) >> 1; if (rowTop[mid] <= y) lo = mid; else hi = mid - 1; }
        if (y > rowTop[lo] + rh + 0.5) return null;
        return { k, row: lo, i: d.order[lo] };
      },
    };
  };

  // -- avatars ------------------------------------------------------------------------------------
  const eyes = (mood, x1, x2, y, tone = '#fff') => {
    if (mood === 'happy') return `<g class="eyes" fill="none" stroke="${tone}" stroke-width="2.3" stroke-linecap="round"><path d="M${x1 - 3.6} ${y + 1.6}q3.6-5.4 7.2 0"/><path d="M${x2 - 3.6} ${y + 1.6}q3.6-5.4 7.2 0"/></g>`;
    if (mood === 'sleep') return `<g fill="none" stroke="${tone}" stroke-width="2.2" stroke-linecap="round"><path d="M${x1 - 3.6} ${y}q3.6 4.2 7.2 0"/><path d="M${x2 - 3.6} ${y}q3.6 4.2 7.2 0"/></g>`;
    const look = mood === 'shifty' ? 1.9 : 0.5;
    const lid = mood === 'shifty'
      ? `<path d="M${x1 - 4.6} ${y - 1}h9.2v-5.4h-9.2zM${x2 - 4.6} ${y - 1}h9.2v-5.4h-9.2z" fill="currentColor"/><path d="M${x1 - 4.4} ${y - 0.9}h8.8M${x2 - 4.4} ${y - 0.9}h8.8" stroke="${tone}" stroke-width="1.1" stroke-linecap="round"/>` : '';
    return `<g class="eyes"><ellipse cx="${x1}" cy="${y}" rx="4.2" ry="5" fill="${tone}"/><ellipse cx="${x2}" cy="${y}" rx="4.2" ry="5" fill="${tone}"/>`
      + `<circle cx="${x1 + look}" cy="${y + 0.8}" r="2.3" fill="#111"/><circle cx="${x2 + look}" cy="${y + 0.8}" r="2.3" fill="#111"/>`
      + `<circle cx="${x1 + look + 0.8}" cy="${y - 0.2}" r="0.8" fill="${tone}"/><circle cx="${x2 + look + 0.8}" cy="${y - 0.2}" r="0.8" fill="${tone}"/>${lid}</g>`;
  };
  const mouth = (mood, x, y) => {
    if (mood === 'happy') return `<path d="M${x - 3.6} ${y}q3.6 3.4 7.2 0" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round"/>`;
    if (mood === 'shifty') return `<path d="M${x - 3} ${y + 1}q1.5-1.2 3 0t3 0" fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round"/>`;
    return `<path d="M${x - 2.4} ${y + 0.6}h4.8" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/>`;
  };
  const FIRM = {
    large: { x: 6, y: 7, w: 36, h: 37, r: 11 },
    mid: { x: 9.5, y: 12, w: 29, h: 32, r: 10 },
    small: { x: 13, y: 18, w: 22, h: 26, r: 8.5 },
  };
  const avatar = (kind, mood = 'open', colors = {}) => {
    const ink = colors.ink ?? '#24232b';
    if (kind === 'regulator') {
      const body = colors.regulator ?? '#6250d6';
      return `<svg viewBox="0 0 48 48" style="color:${body}"><path d="M24 3.5 39.5 9v13.2c0 10.1-6.4 17.9-15.5 21.3C14.9 40.1 8.5 32.3 8.5 22.2V9z" fill="${body}"/>`
        + `<path d="M24 3.5 39.5 9v13.2c0 10.1-6.4 17.9-15.5 21.3z" fill="#fff" opacity=".1"/>${eyes(mood, 18.6, 29.4, 20.5)}`
        + `<path d="M20.5 31.2h7" stroke="#fff" stroke-width="1.9" stroke-linecap="round"/>`
        + `<circle cx="38.5" cy="35.5" r="5.4" fill="#fcfcfb" stroke="#111" stroke-width="2"/><circle cx="37" cy="34" r="1.5" fill="#fff"/><path d="m42.4 39.4 3.8 3.8" stroke="#111" stroke-width="2.6" stroke-linecap="round"/></svg>`;
    }
    if (kind === 'investors') {
      const body = colors.investor ?? '#1baf7a';
      return `<svg viewBox="0 0 48 48" style="color:${body}"><ellipse cx="24" cy="27" rx="17.5" ry="16" fill="${body}"/><path d="M12 22q12-11 24 0" fill="#fff" opacity=".12"/>`
        + `${eyes('sleep', 18, 30, 25)}<ellipse cx="24" cy="33.4" rx="2.2" ry="1.6" fill="#0b4f37"/></svg>`;
    }
    const f = FIRM[kind];
    const cx = f.x + f.w / 2, ey = f.y + f.h * 0.42, gap = f.w * 0.21;
    const antenna = kind === 'large' ? `<path d="M${cx} ${f.y}V2.6" stroke="${ink}" stroke-width="1.8"/><circle cx="${cx}" cy="2.6" r="2" fill="${ink}"/>` : '';
    const drop = mood === 'shifty' ? `<path d="M${f.x + f.w + 1.5} ${f.y + 3}q2.6 4 0 5.6q-2.6-1.6 0-5.6z" fill="#86b6ef"/>` : '';
    const scale = kind === 'small' ? 0.82 : kind === 'mid' ? 0.92 : 1;
    const e = eyes(mood, cx - gap, cx + gap, ey).replace(/rx="4.2" ry="5"/g, `rx="${(4.2 * scale).toFixed(2)}" ry="${(5 * scale).toFixed(2)}"`);
    return `<svg viewBox="0 0 48 48" style="color:${ink}">${antenna}<rect x="${f.x}" y="${f.y}" width="${f.w}" height="${f.h}" rx="${f.r}" fill="${ink}"/>`
      + `<rect x="${f.x + 3}" y="${f.y + 3}" width="${f.w * 0.42}" height="${f.h * 0.22}" rx="${f.r * 0.6}" fill="#fff" opacity=".08"/>${e}${mouth(mood, cx, f.y + f.h * 0.7)}${drop}`
      + `<rect x="${cx - f.w * 0.3}" y="${f.y + f.h - 1}" width="${f.w * 0.18}" height="3.2" rx="1.6" fill="${ink}"/><rect x="${cx + f.w * 0.12}" y="${f.y + f.h - 1}" width="${f.w * 0.18}" height="3.2" rx="1.6" fill="${ink}"/></svg>`;
  };

  // Semicircle gauge: the policy's transparency against the threshold τ*.
  const gauge = (tau, star, colors) => {
    const cx = 24, cy = 30, r = 19;
    const point = v => { const a = Math.PI * (1 - clamp(v, 0, 1)); return [cx + r * Math.cos(a), cy - r * Math.sin(a)]; };
    const arc = (a, b, color, width, opacity = 1) => {
      const [x0, y0] = point(a), [x1, y1] = point(b);
      return `<path d="M${x0.toFixed(2)} ${y0.toFixed(2)}A${r} ${r} 0 0 1 ${x1.toFixed(2)} ${y1.toFixed(2)}" fill="none" stroke="${color}" stroke-width="${width}" stroke-linecap="butt" opacity="${opacity}"/>`;
    };
    const hasStar = star > 0 && star < 1;
    const [nx, ny] = point(tau);
    const [sx0, sy0] = hasStar ? point(star) : [0, 0];
    return `<svg viewBox="0 0 48 48">${hasStar ? arc(0, star, colors.wash, 5, 0.5) + arc(star, 1, colors.improve, 5, 0.5) : arc(0, 1, colors.axis, 5)}`
      + (hasStar ? `<path d="M${sx0.toFixed(2)} ${sy0.toFixed(2)}L${(cx + (sx0 - cx) * 1.28).toFixed(2)} ${(cy + (sy0 - cy) * 1.28).toFixed(2)}" stroke="${colors.ink}" stroke-width="1.6"/>` : '')
      + `<path d="M${cx} ${cy}L${nx.toFixed(2)} ${ny.toFixed(2)}" stroke="${colors.ink}" stroke-width="2.2" stroke-linecap="round"/><circle cx="${cx}" cy="${cy}" r="3.2" fill="${colors.ink}"/>`
      + `<text x="4" y="44" font-size="7" font-family="JetBrains Mono, Consolas, monospace" fill="#898781">0</text><text x="40" y="44" font-size="7" font-family="JetBrains Mono, Consolas, monospace" fill="#898781">1</text></svg>`;
  };

  // Sparkline into an <svg>: the series up to the playhead, the rest faint.
  const spark = (svg, values, { color, current, max = null, bars = false }) => {
    const w = 56, h = 18, n = values.length;
    svg.setAttribute('viewBox', `0 0 ${w} ${h}`);
    const top = max ?? Math.max(1e-9, ...values);
    const x = k => (n <= 1 ? 0 : k / (n - 1) * w), y = v => h - 1 - (v / top) * (h - 3);
    if (bars) {
      let shapes = '';
      values.forEach((v, k) => { if (v > 0) shapes += `<rect x="${(x(k) - 0.6).toFixed(2)}" y="${y(v).toFixed(2)}" width="1.4" height="${(h - 1 - y(v)).toFixed(2)}" fill="${color}" opacity="${k <= current ? 1 : 0.2}"/>`; });
      svg.innerHTML = `<path d="M0 ${h - 0.5}H${w}" stroke="#dad8d0" stroke-width="1"/>${shapes}`;
      return;
    }
    const line = upto => values.slice(0, upto + 1).map((v, k) => `${k ? 'L' : 'M'}${x(k).toFixed(2)} ${y(v).toFixed(2)}`).join('');
    const all = values.map((v, k) => `${k ? 'L' : 'M'}${x(k).toFixed(2)} ${y(v).toFixed(2)}`).join('');
    const end = Math.min(Math.max(current, 0), n - 1);
    svg.innerHTML = `<path d="${all}" stroke="${color}" opacity=".2"/>`
      + (current >= 0 ? `<path d="${line(end)}" stroke="${color}"/><circle cx="${x(end).toFixed(2)}" cy="${y(values[end]).toFixed(2)}" r="2.2" fill="${color}" stroke="#fcfcfb" stroke-width="1.2"/>` : '');
  };

  root.SandboxDesk = { createSphere, spectrogram, avatar, gauge, spark, fit };
})(typeof globalThis !== 'undefined' ? globalThis : this);
