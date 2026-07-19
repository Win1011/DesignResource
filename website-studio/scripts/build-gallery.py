#!/usr/bin/env python3
"""
website-studio 动效策展画廊生成器

解析 references/animation-catalog.md，生成一个自包含的策展画廊 HTML。
用户在画廊里点选动效（按编号），用 preview 部署后浏览挑选。

用法:
    python3 build-gallery.py                          # 默认读 ../references/animation-catalog.md，输出 ./gallery.html
    python3 build-gallery.py --catalog path/to.md     # 指定目录文件
    python3 build-gallery.py --output gallery.html    # 指定输出路径
"""
import re
import sys
import argparse
from pathlib import Path

CATALOG_DEFAULT = Path(__file__).resolve().parent.parent / "references" / "animation-catalog.md"


def parse_catalog(md_text: str):
    """解析目录 markdown，返回 [(category_code, category_name, [rows]), ...]。
    rows = [(编号, 名称, 来源库, 效果, 适用场景, Demo链接)]
    """
    categories = []
    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^##\s+(\S+)\s+—\s+(.+)$", line)
        if m:
            code, name = m.group(1), m.group(2).strip()
            rows = []
            i += 1
            # 跳到表格数据行（越过表头与分隔行）
            while i < len(lines):
                l = lines[i].strip()
                if l.startswith("|") and not re.match(r"^\|[\s\-|:]+\|?$", l) and not l.startswith("| 编号"):
                    cells = [c.strip() for c in l.strip("|").split("|")]
                    if len(cells) >= 6:
                        rows.append(tuple(cells[:6]))
                elif l and not l.startswith("|"):
                    break
                i += 1
            if rows:
                categories.append((code, name, rows))
        else:
            i += 1
    return categories


# 来源库 → 标记色
LIB_COLOR = {
    "React Bits": "#61DAFB",
    "Magic UI": "#a855f7",
    "Aceternity": "#f97316",
    "GSAP": "#88CE02",
    "Shader Gradient": "#ec4899",
    "Lottie": "#00DDB3",
    "Remotion": "#61DAFB",
}


def lib_badge(lib: str) -> str:
    color = LIB_COLOR.get(lib, "#94a3b8")
    return f'<span class="lib-badge" style="--c:{color}">{lib}</span>'


def build_html(categories) -> str:
    total = sum(len(r) for _, _, r in categories)
    cards_html = []
    for code, name, rows in categories:
        cards_html.append(f'<section class="category"><h2><span class="cat-code">{code}</span> {name} <span class="cat-count">{len(rows)} 项</span></h2><div class="grid">')
        for (no, nm, lib, eff, scene, demo) in rows:
            demo_link = f'<a class="demo" href="{demo}" target="_blank" rel="noopener">看演示 ↗</a>' if demo.startswith("http") else ""
            cards_html.append(
                f'<article class="card" data-id="{no}" data-lib="{lib}" onclick="toggle(this)">'
                f'<div class="card-head"><span class="num">{no}</span>{lib_badge(lib)}</div>'
                f'<h3>{nm}</h3>'
                f'<p class="eff">{eff}</p>'
                f'<p class="scene">适用：{scene}</p>'
                f'<div class="card-foot"><button class="pick" onclick="event.stopPropagation();toggle(this.closest(\'.card\'))">＋ 选择</button>{demo_link}</div>'
                f'</article>'
            )
        cards_html.append('</div></section>')

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>动效策展画廊 · Website Studio</title>
<style>
  :root{{--bg:#0a0a0f;--surface:#13131c;--surface2:#1c1c28;--border:#272736;--text:#e8e8f0;--muted:#8b8ba0;--accent:#7c3aed;--accent2:#06b6d4;}}
  *{{margin:0;padding:0;box-sizing:border-box;}}
  body{{background:var(--bg);color:var(--text);font-family:-apple-system,'Inter',system-ui,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased;}}
  .hero{{text-align:center;padding:72px 24px 40px;background:radial-gradient(ellipse at 50% 0%,rgba(124,58,237,.18),transparent 60%);}}
  .hero h1{{font-size:clamp(32px,5vw,52px);font-weight:800;letter-spacing:-.02em;background:linear-gradient(135deg,#fff,#a78bfa);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}}
  .hero p{{color:var(--muted);margin-top:12px;font-size:17px;max-width:560px;margin-inline:auto;}}
  .hero .hint{{margin-top:18px;font-size:14px;color:var(--accent2);}}
  .filters{{position:sticky;top:0;z-index:10;background:rgba(10,10,15,.85);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);padding:14px 24px;display:flex;gap:8px;flex-wrap:wrap;justify-content:center;}}
  .filters button{{background:var(--surface);border:1px solid var(--border);color:var(--muted);padding:7px 16px;border-radius:999px;font-size:13px;cursor:pointer;transition:.2s;}}
  .filters button:hover,.filters button.active{{border-color:var(--accent);color:#fff;background:rgba(124,58,237,.15);}}
  main{{max-width:1240px;margin:0 auto;padding:40px 24px 140px;}}
  .category{{margin-bottom:56px;}}
  .category h2{{font-size:22px;font-weight:700;margin-bottom:20px;display:flex;align-items:center;gap:12px;}}
  .cat-code{{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;padding:3px 10px;border-radius:6px;font-size:14px;font-weight:700;}}
  .cat-count{{color:var(--muted);font-size:13px;font-weight:400;}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px;}}
  .card{{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:20px;cursor:pointer;transition:.25s;position:relative;overflow:hidden;}}
  .card::before{{content:"";position:absolute;inset:0;background:linear-gradient(135deg,rgba(124,58,237,.08),transparent 60%);opacity:0;transition:.25s;}}
  .card:hover{{transform:translateY(-4px);border-color:rgba(124,58,237,.5);box-shadow:0 12px 32px -12px rgba(124,58,237,.4);}}
  .card:hover::before{{opacity:1;}}
  .card.selected{{border-color:var(--accent2);background:linear-gradient(135deg,rgba(6,182,212,.08),var(--surface));box-shadow:0 0 0 1px var(--accent2);}}
  .card-head{{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;}}
  .num{{font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:700;color:var(--accent2);background:rgba(6,182,212,.12);padding:2px 8px;border-radius:6px;}}
  .lib-badge{{font-size:11px;padding:2px 8px;border-radius:999px;font-weight:600;border:1px solid;}}
  .lib-badge{{border-color:var(--c);color:var(--c);background:color-mix(in srgb,var(--c) 12%,transparent);}}
  .card h3{{font-size:16px;font-weight:600;margin-bottom:8px;}}
  .eff{{font-size:13px;color:var(--text);opacity:.9;margin-bottom:8px;}}
  .scene{{font-size:12px;color:var(--muted);}}
  .card-foot{{display:flex;justify-content:space-between;align-items:center;margin-top:14px;}}
  .pick{{background:transparent;border:1px solid var(--border);color:var(--muted);padding:5px 12px;border-radius:8px;font-size:12px;cursor:pointer;transition:.2s;}}
  .pick:hover{{border-color:var(--accent);color:#fff;}}
  .card.selected .pick{{background:var(--accent2);border-color:var(--accent2);color:#000;}}
  .demo{{font-size:12px;color:var(--muted);text-decoration:none;}}
  .demo:hover{{color:var(--accent2);}}
  .tray{{position:fixed;bottom:0;left:0;right:0;background:rgba(19,19,28,.95);backdrop-filter:blur(12px);border-top:1px solid var(--border);padding:16px 24px;z-index:50;transform:translateY(110%);transition:.35s cubic-bezier(.4,0,.2,1);}}
  .tray.show{{transform:translateY(0);}}
  .tray-inner{{max-width:1240px;margin:0 auto;display:flex;align-items:center;gap:16px;flex-wrap:wrap;}}
  .tray-label{{font-size:14px;color:var(--muted);}}
  .tray-ids{{display:flex;gap:8px;flex-wrap:wrap;flex:1;}}
  .chip{{background:rgba(6,182,212,.15);border:1px solid var(--accent2);color:var(--accent2);padding:4px 12px;border-radius:999px;font-size:13px;font-family:monospace;font-weight:600;}}
  .tray-empty{{color:var(--muted);font-size:14px;opacity:.6;}}
  .copy-btn{{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;padding:9px 20px;border-radius:10px;font-size:14px;font-weight:600;cursor:pointer;transition:.2s;}}
  .copy-btn:hover{{transform:translateY(-1px);box-shadow:0 6px 18px -4px rgba(124,58,237,.6);}}
  .copy-btn:disabled{{opacity:.4;cursor:not-allowed;transform:none;box-shadow:none;}}
  .clear-btn{{background:transparent;border:1px solid var(--border);color:var(--muted);padding:8px 16px;border-radius:10px;font-size:13px;cursor:pointer;}}
  @media(max-width:640px){{.grid{{grid-template-columns:1fr;}}}}
</style>
</head>
<body>
<div class="hero">
  <h1>动效策展画廊</h1>
  <p>从精选动效库里挑你喜欢的。点击卡片选择，选好把编号告诉我就行——或者让我帮你选。</p>
  <div class="hint">共 {total} 个动效 · 点卡片选择 · 可按来源库筛选</div>
</div>
<div class="filters" id="filters">
  <button class="active" data-lib="ALL">全部</button>
  {''.join(f'<button data-lib="{l}">{l}</button>' for l in LIB_COLOR)}
</div>
<main>
{''.join(cards_html)}
</main>
<div class="tray" id="tray">
  <div class="tray-inner">
    <span class="tray-label">我的选单：</span>
    <div class="tray-ids" id="trayIds"><span class="tray-empty">还没选，点上方卡片添加</span></div>
    <button class="clear-btn" onclick="clearAll()">清空</button>
    <button class="copy-btn" id="copyBtn" onclick="copyPicks()" disabled>复制编号</button>
  </div>
</div>
<script>
const picks = new Set();
function toggle(card){{
  const id = card.dataset.id;
  if(picks.has(id)){{picks.delete(id);card.classList.remove('selected');}}
  else{{picks.add(id);card.classList.add('selected');}}
  renderTray();
}}
function renderTray(){{
  const tray = document.getElementById('tray');
  const ids = document.getElementById('trayIds');
  const btn = document.getElementById('copyBtn');
  if(picks.size===0){{tray.classList.remove('show');ids.innerHTML='<span class="tray-empty">还没选，点上方卡片添加</span>';btn.disabled=true;return;}}
  tray.classList.add('show');
  ids.innerHTML=[...picks].sort().map(id=>`<span class="chip">${{id}}</span>`).join('');
  btn.disabled=false;
}}
function clearAll(){{picks.clear();document.querySelectorAll('.card.selected').forEach(c=>c.classList.remove('selected'));renderTray();}}
function copyPicks(){{
  const text = [...picks].sort().join('、');
  navigator.clipboard.writeText(text).then(()=>{{
    const b=document.getElementById('copyBtn');const t=b.textContent;b.textContent='已复制 ✓';setTimeout(()=>b.textContent=t,1500);
  }});
}}
// 筛选
document.getElementById('filters').addEventListener('click',e=>{{
  const btn=e.target.closest('button');if(!btn)return;
  document.querySelectorAll('.filters button').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  const lib=btn.dataset.lib;
  document.querySelectorAll('.card').forEach(c=>{{
    c.style.display=(lib==='ALL'||c.dataset.lib===lib)?'':'none';
  }});
}});
</script>
</body>
</html>"""


def main():
    ap = argparse.ArgumentParser(description="生成 website-studio 动效策展画廊")
    ap.add_argument("--catalog", default=str(CATALOG_DEFAULT), help="animation-catalog.md 路径")
    ap.add_argument("--output", default="gallery.html", help="输出 HTML 路径")
    args = ap.parse_args()

    md = Path(args.catalog).read_text(encoding="utf-8")
    cats = parse_catalog(md)
    if not cats:
        print(f"⚠️  未从 {args.catalog} 解析到任何动效条目", file=sys.stderr)
        sys.exit(1)

    html = build_html(cats)
    out = Path(args.output)
    out.write_text(html, encoding="utf-8")
    total = sum(len(r) for _, _, r in cats)
    print(f"✓ 画廊已生成：{out.resolve()}")
    print(f"  共 {len(cats)} 个分类，{total} 个动效条目")
    print(f"  用 preview 部署：python3 -m http.server 8000 --directory {out.parent}")


if __name__ == "__main__":
    main()
