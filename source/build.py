import base64, pathlib
root = pathlib.Path(__file__).parent
src = root / 'src'
b64 = lambda p: base64.b64encode((root / p).read_bytes()).decode()
html = (src / 'shell.html').read_text()
html = html.replace('{{ICON180}}', b64('build/icon-180.png')).replace('{{ICON64}}', b64('build/icon-64.png'))
html = html.replace('{{CSS}}', (src / 'style.css').read_text()).replace('{{JS}}', (src / 'app.js').read_text())
out = root / 'dist' / 'index.html'
out.parent.mkdir(exist_ok=True)
out.write_text(html)
print(out, len(html) // 1024, 'KB')
