---
title: 设计、动效与 AI 前端资源目录
version: "3.0"
updated_at: "2026-07-19"
language: zh-CN
entry_count: 21
catalog_type: design-resources
---

# 设计、动效与 AI 前端资源目录

一份面向设计师、开发者和 AI Agent 的策展型**设计资源目录**,覆盖设计灵感、UI 组件、动效制作工具、前端动画技术与设计规范参考。

> **范围说明**:本目录只收录**设计资源**(灵感站、组件库、动效工具、前端技术、设计系统参考)。Agent Skill(taste-skill、web-to-design-md、GSAP skill 等)不在本目录,设计提取与规范生成能力见各自 Skill 仓库。

> 本目录提供"发现与选型",不等同于对价格、许可证、安全性或长期可用性的背书。使用前请查看资源官方说明;安装第三方依赖前请审查其文档、许可证与权限。

## 快速导航

| 任务 | 优先查看 |
|---|---|
| 找网页视觉方向或案例 | [一、设计灵感与案例](#一设计灵感与案例) |
| 找可直接用于网页的组件 | [二、UI 组件与视觉资源](#二ui-组件与视觉资源) |
| 制作品牌动效、GIF、Lottie 或视频 | [三、动效设计与视觉制作工具](#三动效设计与视觉制作工具) |
| 在代码中实现动画或渲染视频 | [四、前端动画与视频技术](#四前端动画与视频技术) |
| 提取设计规范、研究设计系统或做原型 | [五、设计规范、参考与工作空间](#五设计规范参考与工作空间) |

## 给 AI Agent 的使用规则

1. 先根据用户目标选择分类,再从分类中挑选资源;不要把灵感站、可视化工具、代码库混为一谈。
2. 每次推荐优先给出 1 至 3 个资源,并说明选择原因、输入形式、输出形式和是否需要写代码。
3. 引用条目时优先使用稳定 ID,例如 `INS-001`,方便后续讨论与自动化处理。
4. 同一资源只归入一个主分类;跨领域能力通过标签表达。
5. 实施前重新核对官方文档、许可证、价格、框架版本和导出能力;这些信息可能变化。
6. 许可证与价格不确定时不要猜测,直接提示读者查看官方说明。

### 标签词表

`inspiration` · `gallery` · `prompt` · `component` · `react` · `animation` · `motion-design` · `lottie` · `video` · `shader` · `design-system` · `design-extraction`

## 决策树:我要做什么,用哪个

| 我想要… | 首选 | 备选 |
|---|---|---|
| 找整页 / Hero 视觉方向 | INS-001 MotionSites | INS-004 / INS-005 |
| 看滚动 / 复杂动效真实案例 | INS-002 Made with GSAP | INS-005 Awwwards |
| 找 Bento 网格布局 | INS-003 Bento Grids | 无 |
| Hero 文字逐字 / 分行出场 | CMP-003 React Bits | CMP-005 Aceternity |
| 卡片 3D 倾斜 / 聚光 | CMP-003 React Bits | CMP-004 Magic UI |
| 边框流光 / 扫描 | CMP-004 Magic UI | CMP-005 Aceternity |
| 数字滚动计数 | CMP-004 Magic UI | 无 |
| 背景粒子 / 极光 / 星空 | CMP-003 React Bits | CMP-005 Aceternity |
| 流星 / 漩涡 / 波浪背景 | CMP-005 Aceternity | 无 |
| Shader 渐变背景(可集成) | CMP-001 Shader Gradient | 无 |
| 单个微交互(按钮 / 加载器) | CMP-006 Uiverse | 无 |
| 找现成现代组件 | CMP-002 21st.dev | CMP-007 OriginKit |
| 品牌动效 / 社交视频(不写码) | MOT-001 Jitter | MOT-002 SuperOPC |
| ASCII / Dither / 故障风视觉 | MOT-002 SuperOPC | MOT-004 Flux Pic |
| 液态 / 墨滴 Shader 素材 | MOT-004 Flux Pic | CMP-001 Shader Gradient |
| Lottie 矢量动画 | MOT-005 LottieFiles | MOT-001 导出 |
| 设计与代码画布协作 | MOT-003 Paper | SYS-002 Open Design |
| React 组件级动画 | DEV-001 Motion | 无 |
| 编程式视频流水线 | DEV-002 HyperFrames | MOT-001 Jitter |
| 真实产品设计系统参考 | SYS-001 Refero Styles | 无 |
| 端到端 AI 设计工作空间 | SYS-002 Open Design | 无 |

---

## 一、设计灵感与案例

用于寻找视觉方向、页面结构、动效案例和布局参考。这里的资源主要帮助"看"和"选方向",不一定能直接产出代码。

### INS-001 · MotionSites

- **官网**: https://motionsites.ai
- **类型**: Prompt / 页面灵感库
- **用途**: 按 SaaS、Agency、Portfolio、Ecommerce 等��类浏览大量 Premium 落地页与 Hero 模板;另有独立的 Animated Backgrounds 动效背景库
- **输入 → 输出**: 浏览或按品类检索 → Hero 构图、整页叙事结构、动态背景方向
- **是否需写码**: 否(纯参考);标 "Copy" 的模板可复制源码
- **框架兼容**: 无(参考站,非组件)
- **许可证 / 价格**: 免费浏览;Premium 模板付费,见官网
- **何时选它**: 项目起步找视觉方向、Hero 构图、整页结构时
- **搭配**: 配 CMP-* 组件库把方向落地;配 SYS-* 约束设计规范
- **标签**: `inspiration` `prompt` `motion-design`

### INS-002 · Made with GSAP

- **官网**: https://madewithgsap.com
- **类型**: 动效案例画廊
- **用途**: 浏览用 GSAP 制作的滚动、拖拽、鼠标跟随、循环动画等真实案例
- **输入 → 输出**: 按动效模式筛选案例 → 交互逻辑参考与复现思路
- **是否需写码**: 是(参考用,落地需写 GSAP 代码)
- **框架兼容**: 框架无关(GSAP 原生 JS)
- **许可证 / 价格**: 免费浏览;GSAP 核心免费,部分插件 Club GreenSock 付费
- **何时选它**: 要做滚动叙事或复杂时间线动画、需要真实参考时
- **搭配**: 配 DEV-001 Motion 或 GSAP 落地;配 INS-005 看更高维案例
- **标签**: `inspiration` `gallery` `animation`

### INS-003 · Bento Grids

- **官网**: https://bentogrids.com
- **类型**: 布局灵感库
- **用途**: 浏览 Bento 网格布局、卡片组合与信息层级设计
- **输入 → 输出**: 浏览网格案例 → 布局规律与卡片尺寸配比
- **是否需写码**: 否(纯参考)
- **框架兼容**: 无(布局参考)
- **许可证 / 价格**: 免费浏览
- **何时选它**: 做 Bento 风格落地页或仪表盘、需要网格排版参考时
- **搭配**: 配 CMP-* 卡片组件落地;配 CMP-004 Border Beam 点缀
- **标签**: `inspiration` `gallery` `design-system`

### INS-004 · Godly / Recent

- **官网**: https://recent.design
- **类型**: 网站灵感画廊
- **用途**: 浏览高质量营销网站与数字产品案例,按风格或技术筛选
- **输入 → 输出**: 浏览或筛选 → 风格方向与案例对比
- **是否需写码**: 否(纯参考)
- **框架兼容**: 无
- **许可证 / 价格**: 免费浏览
- **何时选它**: 需要多个同类案例做风格对比、避免直接复刻时
- **搭配**: 配 INS-001 / INS-005 交叉参考
- **标签**: `inspiration` `gallery`

### INS-005 · Awwwards

- **官网**: https://www.awwwards.com
- **类型**: 设计奖项与案例平台
- **用途**: 研究行业级网页设计、交互与创意方向,浏览获奖案例
- **输入 → 输出**: 浏览获奖案例 → 创意方向与设计原则总结
- **是否需写码**: 否(纯参考)
- **框架兼容**: 无
- **许可证 / 价格**: 免费浏览;部分内容需注册
- **何时选它**: 需要顶级行业标杆、提炼多条案例共同原则时
- **搭配**: 配 INS-002 看具体动效实现
- **标签**: `inspiration` `gallery` `motion-design`

---

## 二、UI 组件与视觉资源

用于直接选择、组合或实现网页组件。部分资源提供复制代码、安装包或设计工具导出,具体方式以官方文档为准。

### CMP-001 · Shader Gradient

- **官网**: https://shadergradient.co
- **类型**: 3D 渐变生成器 / 组件
- **用途**: 创建可动画的着色器渐变背景,可视化调参并导出
- **输入 → 输出**: 调参(颜色 / 形状 / 动画) → Shader 渐变,可导出 React / Three.js 代码或视频
- **是否需写码**: 否(可视化调参);集成需写码
- **框架兼容**: React / Three.js / 原生
- **许可证 / 价格**: 免费使用;具体见官网
- **何时选它**: Hero 区需要高级动态渐变背景、3D / Shader 风格时
- **搭配**: 配 DEV-001 集成交互;适合风格代号 E(3D / Shader)
- **标签**: `component` `shader` `animation`

### CMP-002 · 21st.dev

- **官网**: https://21st.dev
- **类型**: AI 组件注册表
- **用途**: 搜索和复用现代 Web UI 组件,社区驱动
- **输入 → 输出**: 检索关键词 → 可复制 React 组件代码
- **是否需写码**: 是(复制代码集成)
- **框架兼容**: React / Tailwind 为主
- **许可证 / 价格**: 免费使用;部分组件见作者说明
- **何时选它**: 需要快速找现成现代组件、不想从零写时
- **搭配**: 配 CMP-003 / 004 / 005 互补选型
- **标签**: `component` `react`

### CMP-003 · React Bits

- **官网**: https://www.reactbits.dev
- **类型**: React 动画组件库
- **用途**: 使用可定制的文本、背景、交互动画组件(Split Text、Tilt Card、Particles、Aurora 等)
- **输入 → 输出**: 选组件 → 复制代码 + 安装依赖
- **是否需写码**: 是
- **框架兼容**: React + Tailwind
- **许可证 / 价格**: 免费
- **何时选它**: 需要丰富 Hero 文字动效、卡片 3D 倾斜、粒子 / 极光背景时
- **搭配**: 配 CMP-004 / 005 补足;配 GSAP 做滚动驱动
- **标签**: `component` `react` `animation`

### CMP-004 · Magic UI

- **官网**: https://magicui.design
- **类型**: 动画 UI 组件库
- **用途**: 构建营销页、展示区和高表现力交互(Border Beam、NumberTicker、Marquee、Animated Beam 等)
- **输入 → 输出**: 选组件 → 复制代码 + 安装
- **是否需写码**: 是
- **框架兼容**: React + Tailwind
- **许可证 / 价格**: 免费;部分高级组件付费
- **何时选它**: 需要边框流光、数字计数、跑马灯、能量束等点缀动效时
- **搭配**: 配 CMP-003 / 005
- **标签**: `component` `react` `animation`

### CMP-005 · Aceternity UI

- **官网**: https://ui.aceternity.com
- **类型**: Tailwind / React 组件库
- **用途**: 创建动态背景、卡片、导航和营销页面(Sparkles、Meteors、Wavy Background、Vortex 等)
- **输入 → 输出**: 选组件 → 复制代码 + 安装
- **是否需写码**: 是
- **框架兼容**: React + Tailwind
- **许可证 / 价格**: 免费
- **何时选它**: 需要流星、漩涡、波浪背景等大场面视觉、暗黑高对比风格时
- **搭配**: 配 CMP-003 / 004
- **标签**: `component` `react` `animation`

### CMP-006 · Uiverse

- **官网**: https://uiverse.io
- **类型**: 社区 UI 元素库
- **用途**: 查找按钮、加载器、开关、复选框等微交互元素
- **输入 → 输出**: 选元素 → 复制 HTML / CSS
- **是否需写码**: 是(但纯 CSS,易集成)
- **框架兼容**: 框架无关(纯 HTML / CSS)
- **许可证 / 价格**: 免费
- **何时选它**: 需要单个微交互元素(按钮 / 加载器 / 开关)、不想引整个库时
- **搭配**: 配 shadcn/ui 等基础组件库
- **标签**: `component` `animation`

### CMP-007 · OriginKit

- **官网**: https://www.originkit.dev
- **类型**: 动效组件库(Beta)
- **用途**: 查找文本、图库和高装饰性互动组件,免费
- **输入 → 输出**: 选组件 → 复制代码 + 安装
- **是否需写码**: 是
- **框架兼容**: React + Tailwind
- **许可证 / 价格**: 免费(Beta)
- **何时选它**: 需要免费、高装饰性动效组件、补充 React Bits / Magic UI 时
- **搭配**: 配 CMP-003 / 004 / 005
- **标签**: `component` `react` `motion-design`

---

## 三、动效设计与视觉制作工具

用于在可视化界面中制作品牌动效、社交内容、Shader、GIF、Lottie 或视频。它们不是前端组件库。

### MOT-001 · Jitter

- **官网**: https://jitter.video
- **类型**: 在线动效设计工具
- **用途**: 从静态设计制作品牌动画、社交视频和界面动效
- **输入 → 输出**: 导入 Figma 或上传图 → 可编辑动效 → 导出视频 / GIF / Lottie
- **是否需写码**: 否(可视化工具)
- **框架兼容**: 无(导出 Lottie 可集成)
- **许可证 / 价格**: 免费版可用;付费版导出更多格式与更高清
- **何时选它**: 需要品牌动效 / 社交视频 / Lottie、不想写码做动效时
- **搭配**: 导出 Lottie 配 MOT-005 校验;配 DEV-001 做网页交互
- **标签**: `motion-design` `video` `lottie`

### MOT-002 · SuperOPC

- **官网**: https://superopc.app
- **类型**: 设计灵感与动效工具集合
- **用途**: 浏览精选网页与品牌案例;使用 ASCII & Dither、Motion 动态模板、Tracker 目标追踪、Apple 风格 Logo 动效等可视化效果工具
- **输入 → 输出**: 浏览案例或选效果工具调参 → 视觉素材或动态模板
- **是否需写码**: 否(可视化工具)
- **框架兼容**: 无
- **许可证 / 价格**: 免费浏览;部分工具与品牌手册为 Exclusive / Pro 付费
- **何时选它**: 需要 ASCII / Dither / Tracker 等 Y2K 与故障风视觉、或品牌动效模板时
- **搭配**: 配 MOT-001 做更标准品牌动效
- **标签**: `motion-design` `shader` `inspiration`

### MOT-003 · Paper

- **官网**: https://paper.design
- **类型**: 画布式设计工具(agent 原生)
- **用途**: 在 HTML / CSS 画布上设计、编辑网页视觉;通过 MCP 与代码库双向同步 token / 样式 / 组件,连接 Claude Code、Codex 等 agent
- **输入 → 输出**: 在画布设计 → 导出代码;或从代码同步到画布
- **是否需写码**: 否(画布操作);与代码库同步时 agent 代写
- **框架兼容**: HTML / CSS 画布,导出 Web 标准
- **许可证 / 价格**: 见官网(桌面端 Windows)
- **何时选它**: 需要设计与代码连续闭环、agent 协作做设计时
- **搭配**: 配 SYS-002 工作空间理念
- **标签**: `motion-design` `design-system`

### MOT-004 · Shader(Flux Pic)

- **官网**: https://shaders.fluxpic.com
- **类型**: Shader 效果生成器
- **用途**: 为图片、Logo 和背景制作液态、墨滴、太阳、半色调等着色器效果,可调参
- **输入 → 输出**: 上传图 + 调参 → 着色器效果素材
- **是否需写码**: 否(可视化调参)
- **框架兼容**: 无
- **许可证 / 价格**: 见官网
- **何时选它**: 需要液态 / 墨滴 / 故障类 Shader 视觉素材、给图片加效果时
- **搭配**: 配 MOT-002 故障风;配 CMP-001 做可集成渐变
- **标签**: `shader` `motion-design`

### MOT-005 · LottieFiles

- **官网**: https://lottiefiles.com
- **类型**: Lottie 资源与编辑平台
- **用途**: 查找、预览、编辑和交付 Lottie 矢量动画
- **输入 → 输出**: 搜索或上传 → Lottie JSON → 网页 / 应用集成
- **是否需写码**: 否(平台编辑);集成需少量代码
- **框架兼容**: 框架无关(Lottie 通用)
- **许可证 / 价格**: 免费版;Pro 付费
- **何时选它**: 需要轻量跨端矢量动画、图标 / 插画动效时
- **搭配**: 配 MOT-001 导出 Lottie;配 DEV-001 网页集成
- **标签**: `lottie` `animation`

---

## 四、前端动画与视频技术

用于在代码中实现交互动画,或通过 Web 技术渲染视频。

### DEV-001 · Motion

- **官网**: https://motion.dev
- **类型**: Web / React 动画库
- **用途**: 实现组件过渡、手势、布局动画和时间线(useScroll、layout animation、drag 等)
- **输入 → 输出**: 写动画代码 → 运行时交互动画
- **是否需写码**: 是
- **框架兼容**: React / Vue / 原生(Framer Motion 为 React 版)
- **许可证 / 价格**: 免费(MIT)
- **何时选它**: 需要组件级过渡、手势、滚动驱动动画,React 项目首选
- **搭配**: 配 GSAP 做复杂时间线;配 CMP-* 组件
- **标签**: `animation` `react`

### DEV-002 · HyperFrames

- **官网**: https://github.com/heygen-com/hyperframes
- **类型**: HTML 视频渲染框架(为 AI Agent 设计)
- **用途**: 用 HTML + GSAP + 着色器编写场景,无头 Chrome + FFmpeg 渲染成视频;支持分布式云端渲染(AWS Lambda / GCP Cloud Run)、Studio 编辑器、浏览器播放器,内置面向 Claude Code / Codex / Cursor 的 skill
- **输入 → 输出**: 写 HTML 场景 → 确定性可重复渲染的视频
- **是否需写码**: 是(HTML / JS)
- **框架兼容**: Web 标准 + GSAP
- **许可证 / 价格**: 免费(Apache-2.0,开源)
- **何时选它**: 需要编程式、可重复渲染的视频流水线,或让 agent 自动产出视频时
- **搭配**: 配 SYS-002 Open Design 的视频模板
- **标签**: `video` `animation`

---

## 五、设计规范、参考与工作空间

用于研究真实产品的设计系统、提取设计规则,或在 AI 驱动的工作空间中完成原型。

### SYS-001 · Refero Styles

- **官网**: https://styles.refero.design/?sort=popular
- **类型**: 设计系统参考库 + AI DESIGN.md 示例
- **用途**: 查看真实产品网站的色彩、字体、间距和组件规范;提供面向 AI agent 的 DESIGN.md 示例
- **输入 → 输出**: 检索产品 → 设计令牌与规范;或参考 DESIGN.md 写法
- **是否需写码**: 否(参考)
- **框架兼容**: 无
- **许可证 / 价格**: 免费浏览
- **何时选它**: 需要真实产品设计系统参考、或学习 DESIGN.md 结构时
- **搭配**: 配 SYS-002 工作空间
- **标签**: `design-system` `design-extraction`

### SYS-002 · Open Design

- **官网**: https://open-design.ai
- **类型**: 开源 AI 设计工作空间(本地优先)
- **用途**: 把本地 coding agent(Claude Code / Codex / Cursor / Gemini CLI 等)接入完整设计流程,产出原型、落地页、仪表盘、Slides 和 HTML 视频;内置多套设计系统,Apache-2.0,BYOK
- **输入 → 输出**: 一句话或模板 → 可运行文件(原型 / 网页 / 视频)
- **是否需写码**: 否(agent 代写);需本地 agent 与桌面端
- **框架兼容**: 产物为 Web 标准 / React
- **许可证 / 价格**: 免费(Apache-2.0,开源);自付 LLM API 费用
- **何时选它**: 需要端到端 AI 设计工作空间、本地优先、自有产物时
- **搭配**: 配 DEV-002 做视频;配 SYS-001 设计系统
- **标签**: `design-system` `motion-design`

---

## 推荐工作流

### 1. 从产品概念到网页

1. 用产品文档和素材与 AI 对齐目标。
2. 从 `INS-*` 选择多个参考方向,不绑定单一参考。
3. 从 `CMP-*` 选择组件,把参考方向落地为真实组件,不直接复刻单一参考站。
4. 用 `SYS-001` 查找接近的真实设计系统,约束色彩 / 字体 / 间距。
5. 用 `DEV-*` 实现交互,最后反馈校准。

### 2. 从静态视觉到动效

1. 用 `MOT-001` Jitter 或其他 `MOT-*` 工具制作可视化动效素材。
2. 需要网页交互时使用 `DEV-001` Motion,复杂时间线结合 GSAP(参考 `INS-002` 案例)。
3. 需要跨端矢量动画时输出 Lottie,并用 `MOT-005` 检查。
4. 需要视频流水线时选择 `DEV-002` HyperFrames。

### 3. 从参考网站到设计规范

1. 从多个 `INS-*` 案例提取共同特征。
2. 用 `SYS-001` 查找接近的真实设计系统。
3. 整理成结构化规范(色彩 / 字体 / 间距 / 组件)。
4. 让 AI 按规范自主选择组件,并通过反馈迭代,而不是逐页硬抄。

---

## 贡献规范

新增资源时:

1. 选择唯一主分类和下一个稳定 ID(沿用现有前缀:INS / CMP / MOT / DEV / SYS)。
2. 使用官方主页或官方源码仓库链接。
3. 描述"适合解决什么问题",避免广告式形容词和易过时的数量。
4. 明确它是灵感、工具、代码库还是组件库。
5. 给出 2 至 3 个受控标签(见标签词表)。
6. 不确定许可证、价格或兼容性时不要猜测,直接提示读者查看官方说明。

---

## 更新记录

- **2026-07-19 · v3.0**:移除原"六、AI 设计与动效 Skills"与"七、Skills 生态与发现目录"共 14 条,使本目录成为纯设计资源库;保留的 21 条资源全量字段化增强(用途 / 输入输出 / 是否写码 / 框架兼容 / 许可证 / 何时选 / 搭配);新增"我要做什么,用哪个"决策树;合并为单文件 README;重写推荐工作流去除 Skill 依赖。
- **2026-07-14 · v2.0**:重新按任务分类;增加稳定 ID、AI 使用规则、标签词表和贡献规范;加入 Jitter;移除容易过时的数量与绝对化表述。
- **2026-07-10 · v1.0**:创建初始资源清单。
