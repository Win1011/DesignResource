# 资源决策树 — 什么场景用哪个库

> agent 内部查阅用，不要整份丢给用户。选型时优先用这里的映射，而非让用户自己挑库。

## 一、按"我要做什么效果"查

| 我想要… | 首选库 | 具体组件/能力 | 备选 |
|---------|--------|--------------|------|
| Hero 区文字逐字/分行出场 | React Bits | Split Text / Text Flip / Shiny Text | Aceternity Text Generate |
| 渐变流动标题 | React Bits | Gradient Text / Shiny Text | Magic UI Animated Gradient Text |
| 滚动驱动的揭示/视差 | GSAP | ScrollTrigger + scrub + stagger | Motion useScroll |
| 滚动横向/钉住章节 | GSAP | ScrollTrigger pin + horizontal | — |
| 卡片 3D 倾斜/聚光 | React Bits | Tilt Card / Spotlight Card | Magic UI Magic Card |
| 边框流光/扫描 | Magic UI | Border Beam / Animated Border | Aceternity Hover Border Gradient |
| 数字滚动计数 | Magic UI | NumberTicker | React Bits Counter |
| 背景粒子/星空/极光 | React Bits | Particles / Aurora / Starfield | Aceternity Sparkles / Vortex |
| 背景网格/点阵/涟漪 | Magic UI | Dot Pattern / Grid Pattern / Ripple | — |
| 鼠标跟随光斑 | Aceternity | Spotlight / Hero Highlight | — |
| 跑马灯/无限滚动列表 | Magic UI | Marquee | — |
| 能量束/连线动效 | Magic UI | Animated Beam | — |
| 流星/光点坠落 | Aceternity | Meteors / Sparkles | — |
| 背景波浪/液态 | Aceternity | Wavy Background / Vortex | — |
| Shader 渐变背景 | Shader Gradient | 着色器 3D 渐变（可导出 React） | — |
| 矢量动画/图标动效 | Lottie | LottieFiles + Text-to-Lottie skill | — |
| 编程式视频 | Remotion | Remotion skill | — |
| 基础 UI 组件（按钮/对话框/表单） | shadcn/ui | 官方组件 | — |

## 二、按"网站风格代号"查默认动效配比

| 风格代号 | 风格 | 动效配比建议 |
|---------|------|-------------|
| A 极简留白 | 克制 | Hero 文字分行淡入(Motion) + 滚动渐显(GSAP ScrollTrigger)。绝不过度。 |
| B Bento 网格 | 模块感 | 卡片入场 stagger + Tilt Card 悬停 + Border Beam 点缀。NumberTicker 展示数据。 |
| C 玻璃拟态 | 漂浮 | Aurora/Particles 背景 + 卡片浮动 + Spotlight 跟随。动效柔和慢节奏。 |
| D 暗黑高对比 | 大胆 | Text Flip/Gradient Text 标题 + Meteors/Sparkles 背景 + 滚动 pin 章节切换。 |
| E 3D/Shader | 空间感 | Shader Gradient 全屏背景 + GSAP 滚动驱动相机/参数 + Vortex。 |
| F 杂志编辑感 | 节奏 | SplitText 大标题 + 横向滚动画廊(GSAP pin) + 文字逐段揭示。动效服务排版。 |
| G 趣味交互 | playful | 弹性 spring + 鼠标跟随 + Marquee + 彩蛋动效。可以多但要有节奏。 |

## 三、按"网站类型"查默认板块与栈

| 网站类型 | 默认栈 | 核心板块 | 动效重点 |
|---------|--------|---------|---------|
| 落地页/产品页 | Next.js + Tailwind + shadcn | Hero → 特性 → 展示 → 社会证明 → CTA → Footer | Hero 抓眼 + 滚动叙事 |
| 作品集 | Next.js 或单文件 HTML | Hero → 精选项目 → 关于 → 联系 | 项目卡片交互 + 横向滚动 |
| 仪表盘 | Next.js + shadcn | 侧栏 → 概览 → 图表 → 表格 → 详情 | 数据计数 + 加载骨架 + 微交互 |
| 博客 | Next.js (MDX) | 文章列表 → 文章 → 关于 | 克制：阅读体验优先，动效退后 |
| 电商 | Next.js + shadcn | Hero → 商品网格 → 详情 → 购物车 | 商品图 hover + Marquee 推荐 + 加购反馈 |
| 活动页 | 单文件 HTML 或 Next.js | Hero(倒计时) → 嘉宾 → 议程 → 报名 | 倒计时 + 粒子背景 + 滚动揭示 |
| 文档站 | Next.js (MDX) | 侧栏目录 → 正文 → 导航 | 极简，几乎无动效 |

## 四、灵感与资源网站

完整资源目录见上级 DR 仓库 [`../README.md`](../README.md):INS 灵感 / CMP 组件 / MOT 动效工具 / DEV 前端技术 / SYS 设计规范 五大分类,每条带字段化详情与「我要做什么 → 用哪个」决策树。本表不重复,只保留 skill 专用的操作映射(按效果 / 按风格代号 / 按网站类型)。

## 五、设计提取能力（Phase 1 用）

| 能力 | 来源 | 何时用 |
|------|------|--------|
| 网站 → DESIGN.md | web-to-design-md (github.com/Paidax01/web-to-design-md) | 深度提取设计系统，产出可复用文档 |
| 设计 DNA + Taste | taste-skill (github.com/senlindesign/taste-skill) | 提取令牌 + "为什么这么设计"的取舍逻辑 |
| 像素级克隆 | clone-website (github.com/huangmingfu/clone-website) | 一条指令克隆成 Next.js 代码 |

> 本 skill 默认用 `agent-browser` 内置提取，不强制依赖上述外部 skill。但若环境已装，可调用增强。
