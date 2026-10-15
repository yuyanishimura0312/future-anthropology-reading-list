"""Embed figc SVG figures and HTML tables into the treatise HTML.

The treatise markdown carries placeholder comments on their own line:

    <!-- fig:fig1-procedure -->
    <!-- fig:fig2-quadrant -->
    <!-- fig:table1-overlaps -->

`inject(html)` replaces each placeholder with a <figure class="lit-fig"> block.
Figures: inline SVG from figures/<name>.svg (figc output, verify PASS) + figcaption (caption below).
  The SVG file itself is never modified (its verify envelope stays valid); accessibility text
  (<title>/<desc> from captions.json "alt") is inserted only into the inline copy.
Tables: figures/<name>.html as-is (figcaption above, written in the file).
Captions live in figures/captions.json so build.py (web) and render_paper.py (PDF) share one source.
Unknown placeholders are left untouched so a typo is visible in the output rather than silently dropped.
"""
import html as _html
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
_PLACEHOLDER = re.compile(r"<!--\s*(?:fig|FIG):([A-Za-z0-9-]+)\s*-->")
# short names used in the treatise md (<!--FIG:fig1--> / <!--FIG:fig2-->) → files in figures/
ALIAS = {"fig1": "fig1-procedure", "fig2": "fig2-quadrant", "table1": "table1-overlaps"}


def _captions():
    return json.loads((HERE / "captions.json").read_text(encoding="utf-8"))


def _svg_inline(name, meta):
    svg = (HERE / f"{name}.svg").read_text(encoding="utf-8").strip()
    svg = re.sub(r"^<\?xml[^>]*>\s*", "", svg)
    svg = re.sub(r"<text\b[^>]*></text>\s*", "", svg)  # figc leaves an empty title <text>
    # accessible name: replace figc's id-only aria-label with the figure label, add <title>/<desc>
    title = _html.escape(f'{meta["label"]} {meta["head"]}')
    desc = _html.escape(meta.get("alt", ""))
    svg = re.sub(r'aria-label="[^"]*"', f'aria-labelledby="{name}-t {name}-d"', svg, count=1)
    svg = re.sub(r"(<svg\b[^>]*>)", rf'\1<title id="{name}-t">{title}</title><desc id="{name}-d">{desc}</desc>', svg, count=1)
    return svg


def figure_html(name):
    meta = _captions()[name]
    if meta["kind"] == "table":
        return (HERE / meta["file"]).read_text(encoding="utf-8").strip()
    svg = _svg_inline(name, meta)
    shape = meta.get("shape", "wide")
    return (
        f'<figure class="lit-fig lit-fig-svg lit-fig-{shape}" id="{name}" tabindex="0" role="group" aria-labelledby="{name}-cap">\n'
        f"{svg}\n"
        f'<figcaption id="{name}-cap"><span class="num">{meta["label"]}</span>'
        f'<span class="head">{meta["head"]}</span>{meta["caption"]}</figcaption>\n'
        f"</figure>"
    )


def inject(html):
    def rep(m):
        name = ALIAS.get(m.group(1), m.group(1))
        try:
            return figure_html(name)
        except (KeyError, FileNotFoundError):
            return m.group(0)
    return _PLACEHOLDER.sub(rep, html)


def placeholders(text):
    """Return the placeholder names found in text (markdown or HTML)."""
    return _PLACEHOLDER.findall(text)
