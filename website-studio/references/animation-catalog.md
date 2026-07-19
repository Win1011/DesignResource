# 精选动效目录

> 画廊生成脚本 `scripts/build-gallery.py` 解析本文件，生成策展画廊 HTML。
> 格式约定：每个分类一节，`## <代号> — <名称>`，下面是严格 6 列表格：`| 编号 | 名称 | 来源库 | 效果 | 适用场景 | Demo |`。
> 编号前缀 = 分类代号。新增条目保持表格格式即可被脚本识别。

---

## H — Hero 区动效

| 编号 | 名称 | 来源库 | 效果 | 适用场景 | Demo |
|------|------|--------|------|---------|------|
| H01 | Split Text | React Bits | 标题逐字/逐词拆解，分行错峰淡入 | Hero 大标题、章节标题 | https://www.reactbits.dev/text-animations/split-text |
| H02 | Text Flip | React Bits | 文字翻转切换多个词，循环展示 | Hero 副标题强调卖点 | https://www.reactbits.dev/text-animations/text-flip |
| H03 | Shiny Text | React Bits | 文字表面流过高光，金属质感 | 标题点缀、CTA 文字 | https://www.reactbits.dev/text-animations/shiny-text |
| H04 | Gradient Text | React Bits | 渐变填充文字，可流动 | 品牌标题、关键词 | https://www.reactbits.dev/text-animations/gradient-text |
| H05 | Spotlight Hero | React Bits | Hero 区鼠标跟随聚光 + 内容揭示 | 首屏 Hero | https://www.reactbits.dev/components/spotlight |
| H06 | Lamp Effect | Aceternity | 标题上方光锥收束点亮 | Hero 章节切换 | https://ui.aceternity.com/components/lamp-effect |
| H07 | Hero Highlight | Aceternity | 鼠标划过文字高亮描线 | Hero 标题交互 | https://ui.aceternity.com/components/hero-highlight |

## S — 滚动驱动动效

| 编号 | 名称 | 来源库 | 效果 | 适用场景 | Demo |
|------|------|--------|------|---------|------|
| S01 | Scroll Reveal | GSAP | 元素滚入视口时上移淡入，stagger 错峰 | 全站通用揭示 | https://madewithgsap.com |
| S02 | Pin Section | GSAP | 钉住章节，滚动驱动内部内容推进 | 章节叙事、产品展示 | https://madewithgsap.com |
| S03 | Horizontal Scroll | GSAP | 垂直滚动转横向画幅平移 | 作品集、时间线 | https://madewithgsap.com |
| S04 | Scrub Timeline | GSAP | 滚动进度驱动多属性同步变化 | 长页连贯叙事 | https://madewithgsap.com |
| S05 | Blur In | Magic UI | 文字/卡片模糊到清晰滚入 | 章节标题揭示 | https://magicui.design/docs/components/blur-in |
| S06 | Fade Up | Magic UI | 上移淡入（轻量替代 GSAP） | 通用入场 | https://magicui.design/docs/components/fade-up |

## B — 背景动效

| 编号 | 名称 | 来源库 | 效果 | 适用场景 | Demo |
|------|------|--------|------|---------|------|
| B01 | Aurora | React Bits | 极光式柔和渐变流动 | 玻璃拟态/柔和 Hero 背景 | https://www.reactbits.dev/backgrounds/aurora |
| B02 | Particles | React Bits | 粒子场，可交互 | 科技感背景 | https://www.reactbits.dev/backgrounds/particles |
| B03 | Starfield | React Bits | 星空穿梭透视 | 太空/未来主题 | https://www.reactbits.dev/backgrounds/starfield |
| B04 | Grid Background | React Bits | 动态网格 + 渐变 | 极客/科技背景 | https://www.reactbits.dev/backgrounds/animated-grid |
| B05 | Wavy Background | Aceternity | SVG 波浪起伏 | 海洋/柔和主题 | https://ui.aceternity.com/components/wavy-background |
| B06 | Vortex | Aceternity | 粒子漩涡旋转 | 动态聚焦区背景 | https://ui.aceternity.com/components/vortex |
| B07 | Sparkles | Aceternity | 闪烁星点散布 | 节日/梦幻点缀 | https://ui.aceternity.com/components/sparkles |
| B08 | Meteors | Aceternity | 流星坠落 | 暗色页背景 | https://ui.aceternity.com/components/meteors |
| B09 | Dot/Grid Pattern | Magic UI | 静态点阵/网格底纹 | 卡片/容器底纹 | https://magicui.design/docs/components/dot-pattern |
| B10 | Ripple | Magic UI | 涟漪扩散 | CTA 区背景 | https://magicui.design/docs/components/ripple |
| B11 | Shader Gradient | Shader Gradient | 着色器 3D 渐变（可导出 React） | 全屏沉浸背景 | https://shadergradient.co |

## I — 交互动效

| 编号 | 名称 | 来源库 | 效果 | 适用场景 | Demo |
|------|------|--------|------|---------|------|
| I01 | Tilt Card | React Bits | 卡片随鼠标 3D 倾斜 | 作品/特性卡片 | https://www.reactbits.dev/components/tilt-card |
| I02 | Spotlight Card | React Bits | 卡片内聚光跟随鼠标 | 特性卡片 | https://www.reactbits.dev/components/spotlight-card |
| I03 | Border Beam | Magic UI | 边框流光扫描 | 高亮卡片/容器 | https://magicui.design/docs/components/border-beam |
| I04 | Magic Card | Magic UI | 鼠标处渐变聚光 | 卡片网格 | https://magicui.design/docs/components/magic-card |
| I05 | Hover Border Gradient | Aceternity | 悬停描边渐变 | 按钮/卡片悬停 | https://ui.aceternity.com/components/hover-border-gradient |
| I06 | Card Hover Effect | Aceternity | 卡片网格中聚焦项放大、其余退后 | 项目/案例展示 | https://ui.aceternity.com/components/card-hover-effect |
| I07 | Direction Aware Hover | Aceternity | 鼠标进入方向决定揭示方向 | 图片画廊 | https://ui.aceternity.com/components/direction-aware-hover |
| I08 | Animated Beam | Magic UI | 两点间能量束流动 | 流程/架构图 | https://magicui.design/docs/components/animated-beam |

## T — 文本动效

| 编号 | 名称 | 来源库 | 效果 | 适用场景 | Demo |
|------|------|--------|------|---------|------|
| T01 | Animated Gradient Text | Magic UI | 渐变文字流动 | 标题/标签高亮 | https://magicui.design/docs/components/animated-gradient-text |
| T02 | Text Shimmer | Magic UI | 文字表面光泽扫过 | 加载/等待文案、CTA | https://magicui.design/docs/components/text-shimmer |
| T03 | Word Rotate | Magic UI | 词汇轮播切换 | 卖点强调 | https://magicui.design/docs/components/word-rotate |
| T04 | Typing | React Bits | 打字机效果 | 终端感/叙事 | https://www.reactbits.dev/text-animations/typing-animation |
| T05 | Decrypt | React Bits | 文字加密解密收束 | 科技感标题 | https://www.reactbits.dev/text-animations/decrypt-text |
| T06 | Number Ticker | Magic UI | 数字滚动到目标值 | 数据/统计展示 | https://magicui.design/docs/components/number-ticker |
| T07 | Counter | React Bits | 数字计数动画 | 数据展示 | https://www.reactbits.dev/components/counter |

## L — 布局动效

| 编号 | 名称 | 来源库 | 效果 | 适用场景 | Demo |
|------|------|--------|------|---------|------|
| L01 | Marquee | Magic UI | 无缝跑马灯横滚 | Logo 墙/推荐流 | https://magicui.design/docs/components/marquee |
| L02 | Bento Grid | React Bits | Bento 卡片网格 stagger 入场 | 特性/概览区 | https://bentogrids.com |
| L03 | Orbiting Circles | Magic UI | 环绕轨道图标旋转 | 技术栈/生态展示 | https://magicui.design/docs/components/orbiting-circles |
| L04 | Globe | Magic UI | 3D 地球点标记 | 全球化/部署展示 | https://magicui.design/docs/components/globe |

## W — 加载与等待动效

| 编号 | 名称 | 来源库 | 效果 | 适用场景 | Demo |
|------|------|--------|------|---------|------|
| W01 | Shimmer Button | Magic UI | 按钮表面光泽循环 | CTA 按钮 | https://magicui.design/docs/components/shimmer-button |
| W02 | Animated List | Magic UI | 列表项滚入轮播 | 实时动态/日志 | https://magicui.design/docs/components/animated-list |
| W03 | Terminal | Magic UI | 终端打字输出 | 开发者向 Hero/演示 | https://magicui.design/docs/components/terminal |
