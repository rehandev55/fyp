"""
Chart drawing for the project report.

Pillow is used rather than a plotting library because the project already
depends on Pillow and the report needs only four chart forms: vertical bars,
horizontal bars, a pie, and a multi-series line. Charts are drawn at three
times the final print size and downsampled, which gives clean edges and
readable text at 150 dpi.
"""

import os

from PIL import Image, ImageDraw, ImageFont

S = 3  # supersampling factor

WHITE = (255, 255, 255)
INK = (26, 26, 26)
GREY = (110, 110, 110)
GRID = (222, 222, 222)
AXIS = (140, 140, 140)

#: A print-safe categorical palette: distinct in colour and in lightness, so
#: the charts survive a greyscale photocopy of the bound report.
PALETTE = [
    (37, 99, 235),    # blue
    (5, 150, 105),    # green
    (217, 119, 6),    # amber
    (124, 58, 237),   # violet
    (220, 38, 38),    # red
    (13, 148, 136),   # teal
    (190, 24, 93),    # pink
    (100, 116, 139),  # slate
]

_FONT_DIRS = [r"C:\Windows\Fonts", "/usr/share/fonts/truetype/dejavu"]
_FONT_FILES = {
    (False, False): ["times.ttf", "DejaVuSerif.ttf"],
    (True, False): ["timesbd.ttf", "DejaVuSerif-Bold.ttf"],
}
_CACHE = {}


def font(size: int, bold: bool = False):
    key = (size, bold)
    if key in _CACHE:
        return _CACHE[key]
    for directory in _FONT_DIRS:
        for name in _FONT_FILES[(bold, False)]:
            path = os.path.join(directory, name)
            if os.path.exists(path):
                loaded = ImageFont.truetype(path, size * S)
                _CACHE[key] = loaded
                return loaded
    loaded = ImageFont.load_default()
    _CACHE[key] = loaded
    return loaded


class Chart:
    def __init__(self, w=900, h=520):
        self.w, self.h = w, h
        self.img = Image.new("RGB", (w * S, h * S), WHITE)
        self.d = ImageDraw.Draw(self.img)

    # ── primitives ──────────────────────────────────────────────────────────
    def text(self, x, y, s, size=13, bold=False, fill=INK, anchor="la"):
        self.d.text((x * S, y * S), s, font=font(size, bold), fill=fill,
                    anchor=anchor)

    def rect(self, x, y, w, h, fill=None, outline=None, width=1):
        self.d.rectangle([x * S, y * S, (x + w) * S, (y + h) * S],
                         fill=fill, outline=outline, width=width * S)

    def line(self, pts, fill=AXIS, width=1):
        self.d.line([(x * S, y * S) for x, y in pts], fill=fill,
                    width=width * S, joint="curve")

    def title(self, s, size=17):
        self.text(self.w / 2, 16, s, size=size, bold=True, anchor="ma")

    def save(self, path):
        out = self.img.resize((self.w, self.h), Image.LANCZOS)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        out.save(path, dpi=(150, 150))
        return path

    # ── helpers ─────────────────────────────────────────────────────────────
    def _text_w(self, s, size, bold=False):
        return self.d.textlength(s, font=font(size, bold)) / S

    def _wrap(self, s, size, max_w, bold=False):
        words, lines, cur = s.split(), [], ""
        for word in words:
            trial = f"{cur} {word}".strip()
            if self._text_w(trial, size, bold) <= max_w or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
        return lines


def _nice_ticks(vmax, target=5):
    """Round axis maximum up to a readable step."""
    if vmax <= 0:
        return 1, [0, 1]
    raw = vmax / target
    magnitude = 10 ** len(str(int(raw))) / 10 if raw >= 1 else 0.1
    for mult in (1, 2, 2.5, 5, 10):
        step = magnitude * mult
        if step >= raw:
            break
    top = step * (int(vmax / step) + (1 if vmax % step else 0))
    ticks, v = [], 0.0
    while v <= top + 1e-9:
        ticks.append(round(v, 6))
        v += step
    return top, ticks


def bar_chart(path, title, labels, values, *, w=900, h=520, ylabel="",
              colour=None, value_fmt="{:,.0f}", wrap=14):
    """Vertical bars — for counts across a handful of categories."""
    c = Chart(w, h)
    c.title(title)

    left, right, top, bottom = 90, 40, 62, 92
    pw, ph = w - left - right, h - top - bottom
    vmax, ticks = _nice_ticks(max(values) if values else 1)

    for tick in ticks:
        y = top + ph - (tick / vmax) * ph
        c.line([(left, y), (left + pw, y)], fill=GRID, width=1)
        c.text(left - 10, y, value_fmt.format(tick), size=12, fill=GREY,
               anchor="rm")
    c.line([(left, top), (left, top + ph)], fill=AXIS, width=1)
    c.line([(left, top + ph), (left + pw, top + ph)], fill=AXIS, width=1)

    n = len(values)
    slot = pw / max(n, 1)
    bw = min(slot * 0.62, 88)
    for i, (label, value) in enumerate(zip(labels, values)):
        cx = left + slot * (i + 0.5)
        bh = (value / vmax) * ph if vmax else 0
        fill = colour or PALETTE[i % len(PALETTE)]
        c.rect(cx - bw / 2, top + ph - bh, bw, bh, fill=fill)
        c.text(cx, top + ph - bh - 8, value_fmt.format(value), size=13,
               bold=True, anchor="md")
        for j, line in enumerate(c._wrap(label, 11, slot * 0.98)[:3]):
            c.text(cx, top + ph + 10 + j * 16, line, size=12, anchor="ma")

    if ylabel:
        c.text(left - 10, top - 16, ylabel, size=12, fill=GREY, anchor="rs")
    return c.save(path)


def hbar_chart(path, title, labels, values, *, w=900, h=None, colour=None,
               value_fmt="{:,.0f}", label_w=250, note=""):
    """Horizontal bars — for many categories or long labels."""
    rows = len(values)
    h = h or max(240, 96 + rows * 34 + (26 if note else 0))
    c = Chart(w, h)
    c.title(title)

    left, right, top = label_w, 70, 62
    bottom = 34 + (24 if note else 0)
    pw = w - left - right
    ph = h - top - bottom
    vmax, _ = _nice_ticks(max(values) if values else 1)
    slot = ph / max(rows, 1)
    bh = min(slot * 0.66, 24)

    c.line([(left, top), (left, top + ph)], fill=AXIS, width=1)

    for i, (label, value) in enumerate(zip(labels, values)):
        cy = top + slot * (i + 0.5)
        bw = (value / vmax) * pw if vmax else 0
        fill = colour or PALETTE[i % len(PALETTE)]
        c.rect(left, cy - bh / 2, bw, bh, fill=fill)
        c.text(left + bw + 8, cy, value_fmt.format(value), size=13, bold=True,
               anchor="lm")
        lines = c._wrap(label, 12, left - 16)[:2]
        y0 = cy - (len(lines) - 1) * 7
        for j, line in enumerate(lines):
            c.text(left - 12, y0 + j * 15, line, size=12, anchor="rm")

    if note:
        c.text(left, h - 16, note, size=11, fill=GREY, anchor="ls")
    return c.save(path)


def pie_chart(path, title, labels, values, *, w=900, h=380, note=""):
    """Pie with a side legend — for a single-choice question."""
    c = Chart(w, h)
    c.title(title)

    total = sum(values) or 1
    cx, cy, r = 240, h / 2 + 16, 132
    start = -90.0
    for i, value in enumerate(values):
        sweep = 360.0 * value / total
        c.d.pieslice(
            [(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
            start, start + sweep,
            fill=PALETTE[i % len(PALETTE)], outline=WHITE, width=2 * S,
        )
        start += sweep

    ly = cy - (len(values) * 34) / 2
    for i, (label, value) in enumerate(zip(labels, values)):
        y = ly + i * 34
        c.rect(450, y - 9, 19, 19, fill=PALETTE[i % len(PALETTE)])
        pct = 100.0 * value / total
        c.text(480, y + 1, f"{label}", size=14, anchor="lm")
        c.text(w - 40, y + 1, f"{value}  ({pct:.1f}%)", size=14, bold=True,
               fill=GREY, anchor="rm")

    if note:
        c.text(w / 2, h - 14, note, size=11, fill=GREY, anchor="ms")
    return c.save(path)


def line_chart(path, title, x_labels, series, *, w=900, h=520, ylabel="",
               xlabel="", value_fmt="{:,.0f}"):
    """Multi-series line chart. `series` is a list of (name, values)."""
    c = Chart(w, h)
    c.title(title)

    left, right, top, bottom = 92, 40, 74, 84
    pw, ph = w - left - right, h - top - bottom
    all_values = [v for _, values in series for v in values]
    vmax, ticks = _nice_ticks(max(all_values) if all_values else 1)

    for tick in ticks:
        y = top + ph - (tick / vmax) * ph
        c.line([(left, y), (left + pw, y)], fill=GRID, width=1)
        c.text(left - 10, y, value_fmt.format(tick), size=12, fill=GREY,
               anchor="rm")
    c.line([(left, top), (left, top + ph)], fill=AXIS, width=1)
    c.line([(left, top + ph), (left + pw, top + ph)], fill=AXIS, width=1)

    n = len(x_labels)
    step = pw / max(n - 1, 1)
    for i, label in enumerate(x_labels):
        x = left + i * step
        c.text(x, top + ph + 10, str(label), size=12, anchor="ma")

    for s, (name, values) in enumerate(series):
        colour = PALETTE[s % len(PALETTE)]
        pts = [(left + i * step, top + ph - (v / vmax) * ph)
               for i, v in enumerate(values)]
        c.line(pts, fill=colour, width=3)
        for x, y in pts:
            c.d.ellipse([(x - 4) * S, (y - 4) * S, (x + 4) * S, (y + 4) * S],
                        fill=colour, outline=WHITE, width=1 * S)
        c.rect(left + s * 210, top - 34, 14, 14, fill=colour)
        c.text(left + s * 210 + 22, top - 27, name, size=13, anchor="lm")

    if ylabel:
        c.text(left - 10, top - 16, ylabel, size=12, fill=GREY, anchor="rs")
    if xlabel:
        c.text(left + pw / 2, h - 16, xlabel, size=12, fill=GREY, anchor="ms")
    return c.save(path)


def grouped_bar_chart(path, title, group_labels, series, *, w=900, h=520,
                      ylabel="", value_fmt="{:.2f}", note=""):
    """Grouped vertical bars. `series` is a list of (name, values)."""
    c = Chart(w, h)
    c.title(title)

    left, right, top, bottom = 90, 40, 78, 92
    pw, ph = w - left - right, h - top - bottom
    all_values = [v for _, values in series for v in values]
    vmax, ticks = _nice_ticks(max(all_values) if all_values else 1)

    for tick in ticks:
        y = top + ph - (tick / vmax) * ph
        c.line([(left, y), (left + pw, y)], fill=GRID, width=1)
        c.text(left - 10, y, f"{tick:g}", size=12, fill=GREY, anchor="rm")
    c.line([(left, top), (left, top + ph)], fill=AXIS, width=1)
    c.line([(left, top + ph), (left + pw, top + ph)], fill=AXIS, width=1)

    groups = len(group_labels)
    slot = pw / max(groups, 1)
    k = len(series)
    bw = min(slot * 0.7 / k, 54)

    for gi, label in enumerate(group_labels):
        base = left + slot * (gi + 0.5) - (k * bw) / 2
        for si, (_, values) in enumerate(series):
            value = values[gi]
            bh = (value / vmax) * ph if vmax else 0
            c.rect(base + si * bw, top + ph - bh, bw - 3, bh,
                   fill=PALETTE[si % len(PALETTE)])
            c.text(base + si * bw + (bw - 3) / 2, top + ph - bh - 7,
                   value_fmt.format(value), size=11, bold=True, anchor="md")
        for j, line in enumerate(c._wrap(label, 11, slot * 0.95)[:2]):
            c.text(left + slot * (gi + 0.5), top + ph + 10 + j * 16, line,
                   size=12, anchor="ma")

    for si, (name, _) in enumerate(series):
        c.rect(left + si * 230, top - 36, 14, 14,
               fill=PALETTE[si % len(PALETTE)])
        c.text(left + si * 230 + 22, top - 29, name, size=13, anchor="lm")

    if ylabel:
        c.text(left - 10, top - 16, ylabel, size=12, fill=GREY, anchor="rs")
    if note:
        c.text(w / 2, h - 14, note, size=11, fill=GREY, anchor="ms")
    return c.save(path)
