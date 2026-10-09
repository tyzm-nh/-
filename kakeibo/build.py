"""index.html（あなた用）から demo.html（人に見せる用）を作る。

機能は同じで、DEMO を true にしたものがデモ版になる。
デモ版は最初に5つの質問をして、その答えから計画・予算・支払い予定を作る。
使い方: python3 kakeibo/build.py
"""
from pathlib import Path

here = Path(__file__).parent
src = (here / "index.html").read_text(encoding="utf-8")

swaps = [
    ("const DEMO=false;", "const DEMO=true;"),
    ("<title>200万円家計簿</title>", "<title>目標貯金の家計簿</title>"),
    ("<h1>200万円家計簿</h1>", '<h1>目標貯金の家計簿</h1><span class="pill mid">デモ</span>'),
    ("const LK='kakeibo200-v1';", "const LK='kakeibo-demo-v2';"),
]
out = src
for old, new in swaps:
    assert out.count(old) == 1, f"見つからない: {old}"
    out = out.replace(old, new)

(here / "demo.html").write_text(out, encoding="utf-8")
print("demo.html を作りました")
