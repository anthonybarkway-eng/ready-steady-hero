"""Build index.html and sw.js from src/body.html.

src/body.html is the game itself (what the claude.ai artifact shows).
This wrapper adds the head needed for an installable, offline, full-screen
iPad web app, and stamps the service worker with a content hash so devices
pick up each new build on their next launch.
"""
import hashlib
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
body = (ROOT / "src" / "body.html").read_text(encoding="utf-8")

# claude.ai-only meta tag; harmless elsewhere but not needed
body = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\s*', "", body)

# move <title> and the font <link>s that sit at the top of the body into the head
head_bits = []
for pat in (r"<title>.*?</title>\s*", r'<link rel="preconnect"[^>]*>\s*', r'<link rel="stylesheet"[^>]*>\s*'):
    for m in re.finditer(pat, body):
        head_bits.append(m.group(0).strip())
    body = re.sub(pat, "", body, count=0)

head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Hero">
<meta name="theme-color" content="#17213a">
<meta name="description" content="Ready, Steady, Hero! A calm-down, listening and early English game for a three to four year old.">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" type="image/png" href="icon-192.png">
{chr(10).join(head_bits)}
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);color-scheme:light}}body{{margin:0;font:14px system-ui}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
"""
tail = """
<script>if('serviceWorker' in navigator){addEventListener('load',function(){navigator.serviceWorker.register('./sw.js').catch(function(){});});}</script>
</body>
</html>
"""
index = head + body.strip() + "\n" + tail
(ROOT / "index.html").write_text(index, encoding="utf-8")

stamp = hashlib.sha256(index.encode("utf-8")).hexdigest()[:10]
sw = (ROOT / "src" / "sw.template.js").read_text(encoding="utf-8").replace("__VERSION__", stamp)
(ROOT / "sw.js").write_text(sw, encoding="utf-8")
print(f"index.html {len(index)} bytes, service worker cache rsh-{stamp}")
