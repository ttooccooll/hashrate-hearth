#!/usr/bin/env python3
"""Build site/index.html from hashrate-hearth.html.

The source is a page fragment (markup, styles and script without <html>, <head> or <body>);
this wraps it in a full document for any static host. Vercel runs it on every deploy.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
src = (ROOT / 'hashrate-hearth.html').read_text()

cut = src.index('</style>') + len('</style>')
head, body = src[:cut], src[cut:].strip()
head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')

DESC = ('How much home hashrate it takes to break the two template builders that pick most '
        'bitcoin blocks, with live network data and heat and solar math.')
ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
        "%3Crect width='32' height='32' rx='6' fill='%230e0a08'/%3E"
        "%3Cpath d='M16 4c1 6 8 8 8 15a8 8 0 0 1-16 0c0-4 2-6 4-8 0 3 1 5 3 6-1-5 0-9 1-13z' fill='%23ff6a1a'/%3E%3C/svg%3E")

page = f'''<!doctype html>
<html lang="en">
<head>
{head}
<meta name="description" content="{DESC}">
<meta property="og:title" content="Hashrate Hearth">
<meta property="og:description" content="{DESC}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#0e0a08">
<link rel="icon" href="{ICON}">
</head>
<body>
{body}
</body>
</html>
'''
out = ROOT / 'site' / 'index.html'
out.parent.mkdir(exist_ok=True)
out.write_text(page)
print(f'wrote {out} ({len(page):,} bytes)')
