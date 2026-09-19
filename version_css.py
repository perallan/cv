#!/usr/bin/env python3
"""Run before uploading: python3 version_css.py (standard library only)."""
from hashlib import sha256
from pathlib import Path
import re


def version_css(directory):
    html_path = directory / 'index.html'
    html = html_path.read_text(encoding='utf-8')
    outputs = []
    for stem in ('index', 'stack', 'print'):
        source = directory / f'{stem}.css'
        content = source.read_bytes()
        digest = sha256(content).hexdigest()[:12]
        filename = f'{stem}.{digest}.css'
        pattern = rf'(href=[\"\']){stem}(?:\.[0-9a-f]{{12}})?\.css(?:\?[^\"\']*)?([\"\'])'
        html, count = re.subn(pattern, lambda m: m[1] + filename + m[2], html)
        if count != 1:
            raise ValueError(f'Expected one stylesheet link for {stem}.css, found {count}')
        outputs.append((filename, content))
    # Validate every link before writing. Keep old versions for cached HTML.
    for filename, content in outputs:
        target = directory / filename
        if not target.exists() or target.read_bytes() != content:
            target.write_bytes(content)
    if html != html_path.read_text(encoding='utf-8'):
        html_path.write_text(html, encoding='utf-8')
    return [filename for filename, _ in outputs]


if __name__ == '__main__':
    for filename in version_css(Path(__file__).resolve().parent):
        print(filename)
    print('Upload these CSS files first, then index.html. Keep previous CSS versions.')
