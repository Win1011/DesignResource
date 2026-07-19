---
title: 设计、动效与 AI 前端资源目录
version: "3.3"
updated_at: "2026-07-19"
language: zh-CN
entry_count: 47
catalog_type: design-resources
---

# 设计、动效与 AI 前端资源目录

一份面向设计师、开发者和 AI Agent 的策展型**设计资源与 Skill 目录**,覆盖设计灵感、UI 组件、动效制作工具、前端动画技术、设计规范参考,以及 AI 设计与动效 Skill。

> **范围说明**:本目录收录**设计资源**(灵感站、组件库、动效工具、前端技术、设计系统参考)与 **AI Skill**(设计提取、动效编码、视频生成等能力扩展)。旗舰 skill `website-studio`(本仓库维护)见 [Skills 分类](#六ai-设计与动效-skills)顶部。

> 本目录提供"发现与选型",不等同于对价格、许可证、安全性或长期可用性的背书。使用前请查看资源官方说明;安装第三方依赖前请审查其文档、许可证与权限。

## 快速导航

| 任务 | 优先查看 |
|---|---|
| 找网页视觉方向或案例 | [一、设计灵感与案例](#一设计灵感与案例) |
| 找可直接用于网页的组件 | [二、UI 组件与视觉资源](#二ui-组件与视觉资源) |
| 制作品牌动效、GIF、Lottie 或视频 | [三、动效设计与视觉制作工具](#三动效设计与视觉制作工具) |
| 在代码中实现动画或渲染视频 | [四、前端动画与视频技术](#四前端动画与视频技术) |
| 提取设计规范、研究设计系统或做原型 | [五、设计规范、参考与工作空间](#五设计规范参考与工作空间) |
| 给 AI Agent 增加设计或动效能力 | [六、AI 设计与动效 Skills](#六ai-设计与动效-skills) |
| 继续寻找更多 Skills | [七、Skills 生态与发现目录](#七skills-生态与发现目录) |

## 给 AI Agent 的使用规则

1. 先根据用户目标选择分类,再从分类中挑选资源;不要把灵感站、可视化工具、代码库混为一谈。
2. 每次推荐优先给出 1 至 3 个资源,并说明选择原因、输入形式、输出形式和是否需要写代码。
3. 引用条目时优先使用稳定 ID,例如 `INS-001`,方便后续讨论与自动化处理。
4. 同一资源只归入一个主分类;跨领域能力通过标签表达。
5. 实施前重新核对官方文档、许可证、价格、框架版本和导出能力;这些信息可能变化。
6. 许可证与价格不确定时不要猜测,直接提示读者查看官方说明。

### 标签词表

`inspiration` · `gallery` · `prompt` · `component` · `react` · `animation` · `motion-design` · `lottie` · `video` · `shader` · `design-system` · `design-extraction` · `font` · `icon` · `3d` · `agent-skill` · `directory`

## 决策树:我要做什么,用哪个

| 我想要… | 首选 | 备选 |
|---|---|---|
| 找整页 / Hero 视觉方向 | INS-001 MotionSites | INS-004 / INS-005 / INS-006 |
| 看策展级网站合集 | INS-006 Siteinspire | INS-005 Awwwards |
| 看滚动 / 复杂动效真实案例 | INS-002 Made with GSAP | INS-005 Awwwards |
| 找 Bento 网格布局 | INS-003 Bento Grids | 无 |
| 研究微交互 / 细节魔法 | INS-007 Design Spells | INS-002 |
| 复制网页设计 Prompt | INS-008 Website Prompts | INS-001 MotionSites |
| Hero 文字逐字 / 分行出场 | CMP-003 React Bits | CMP-005 Aceternity |
| 卡片 3D 倾斜 / 聚光 | CMP-003 React Bits | CMP-004 Magic UI |
| 边框流光 / 扫描 | CMP-004 Magic UI | CMP-005 Aceternity |
| 数字滚动计数 | CMP-004 Magic UI | 无 |
| 背景粒子 / 极光 / 星空 | CMP-003 React Bits | CMP-005 Aceternity |
| 流星 / 漩涡 / 波浪背景 | CMP-005 Aceternity | 无 |
| Shader 渐变背景(可集成) | CMP-001 Shader Gradient | 无 |
| 单个微交互(按钮 / 加载器) | CMP-006 Uiverse | 无 |
| 找现成现代组件 | CMP-002 21st.dev | CMP-007 OriginKit |
| 可复制的基础组件体系 | CMP-008 shadcn/ui | CMP-002 21st.dev |
| 高质量图标集 | CMP-009 Lucide | 无 |
| 免费商用字体 | CMP-010 Fontshare | 无 |
| 海量字体浏览 / 个人下载 | CMP-011 1001 Free Fonts | CMP-010 Fontshare |
| 品牌动效 / 社交视频(不写码) | MOT-001 Jitter | MOT-002 SuperOPC |
| ASCII / Dither / 故障风视觉 | MOT-002 SuperOPC | MOT-004 Flux Pic |
| 液态 / 墨滴 Shader 素材 | MOT-004 Flux Pic | CMP-001 Shader Gradient |
| Lottie 矢量动画 | MOT-005 LottieFiles | MOT-001 导出 |
| 可交互状态机动效 | MOT-006 Rive | MOT-005 LottieFiles |
| Web 3D 场景 / 物件 | MOT-007 Spline | CMP-001 Shader Gradient |
| 设计与代码画布协作 | MOT-003 Paper | SYS-002 Open Design |
| React 组件级动画 | DEV-001 Motion | 无 |
| 复杂时间线 / 滚动叙事动画 | DEV-003 GSAP | DEV-001 Motion |
| 编程式视频流水线 | DEV-002 HyperFrames | MOT-001 Jitter |
| 真实产品设计系统参考 | SYS-001 Refero Styles | 无 |
| 真实 App / Web 界面与流程 | SYS-003 Mobbin | SYS-001 Refero Styles |
| 端到端 AI 设计工作空间 | SYS-002 Open Design | 无 |
| 扩展 agent 设计 / 动效能力 | website-studio(首选) | SKL-* 外部 skill |

---

## 一、设计灵感与案例

用于寻找视觉方向、页面结构、动效案例和布局参考。这里的资源主要帮助"看"和"选方向",不一定能直接产出代码。

### INS-001 · MotionSites

- **官网**: https://motionsites.ai
- **类型**: Prompt / 页面灵感库
- **用途**: 按 SaaS、Agency、Portfolio、Ecommerce 等品类浏览大量 Premium 落地页与 Hero 模板;另有独立的 Animated Backgrounds 动效背景库
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
- **搭配**: 配 DEV-001 Motion 或 DEV-003 GSAP 落地;配 INS-005 看更高维案例
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

### INS-006 · Siteinspire

- **官网**: https://www.siteinspire.com
- **类型**: 策展型网站灵感画廊
- **用途**: 按风格、类型、主题筛选高质量网站案例,偏工作室、作品集、品牌与排版向
- **输入 → 输出**: 按分类 / 风格筛选 → 可收藏的网站案例列表
- **是否需写码**: 否(纯参考)
- **框架兼容**: 无
- **许可证 / 价格**: 免费浏览;收藏等功能可能需注册
- **何时选它**: 需要比奖项站更偏「可长期收藏」的策展合集、看排版与艺术指导时
- **搭配**: 配 INS-004 / INS-005 交叉对比;配 CMP-* 落地
- **标签**: `inspiration` `gallery`

### INS-007 · Design Spells

- **官网**: https://www.designspells.com
- **类型**: 设计细节 / 微交互灵感库
- **用途**: 收集「细节像魔法」的界面片段:微交互、过渡、彩蛋、拟物、动态岛等
- **输入 → 输出**: 按标签浏览 → 具体交互细节与实现灵感
- **是否需写码**: 否(参考);落地需自行实现
- **框架兼容**: 无
- **许可证 / 价格**: 免费浏览
- **何时选它**: 大结构已定、要打磨按钮 / 过渡 / 趣味细节时
- **搭配**: 配 CMP-003 / 004 / 006 找可复用实现;配 DEV-001 / DEV-003 写交互
- **标签**: `inspiration` `gallery` `animation`

### INS-008 · Website Prompts

- **官网**: https://websiteprompts.ai
- **类型**: Web Prompt 库
- **用途**: 按行业 / 站点类型浏览完整网页 Prompt,复制后用于 Lovable、Bolt、v0、Claude 等生成落地页
- **输入 → 输出**: 选品类 → 可复制的整页设计 Prompt
- **是否需写码**: 否(Prompt 工作流);生成后再视工具改代码
- **框架兼容**: 取决于下游 AI 建站工具
- **许可证 / 价格**: 免费复制使用(以官网说明为准)
- **何时选它**: 要用自然语言直接生成整页、需要现成高质量 Prompt 时
- **搭配**: 配 INS-001 看更偏动效的结构化 Prompt;生成后用 SYS-* 约束规范
- **标签**: `inspiration` `prompt`

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

### CMP-008 · shadcn/ui

- **官网**: https://ui.shadcn.com
- **类型**: 可复制的基础 UI 组件体系
- **用途**: 以 Radix + Tailwind 为基础,按需复制 Button、Dialog、Form、Data Table 等高质量基础组件,而不是安装整包 npm 依赖
- **输入 → 输出**: CLI 添加组件 → 项目内可改的 React 组件源码
- **是否需写码**: 是
- **框架兼容**: React + Tailwind;支持多个主流框架文档
- **许可证 / 价格**: 免费(MIT,以官网为准)
- **何时选它**: 需要可维护的基础组件层、再在其上叠加营销动效组件时
- **搭配**: 配 CMP-003 / 004 / 005 做高表现力区块;配 CMP-009 图标
- **标签**: `component` `react`

### CMP-009 · Lucide

- **官网**: https://lucide.dev
- **类型**: 开源图标集
- **用途**: 提供风格统一、笔画清晰的 SVG 图标,覆盖 Web / 产品界面常用符号
- **输入 → 输出**: 搜索图标 → SVG / React / Vue 等组件用法
- **是否需写码**: 是(嵌入图标);也可导出 SVG
- **框架兼容**: React / Vue / Svelte / 原生 SVG 等
- **许可证 / 价格**: 免费(ISC,以官网为准)
- **何时选它**: 需要一致、现代、可商用的界面图标体系时
- **搭配**: 配 CMP-008 shadcn/ui;避免同一页混用多种图标风格
- **标签**: `component` `icon`

### CMP-010 · Fontshare

- **官网**: https://www.fontshare.com
- **类型**: 免费商用字体库
- **用途**: 由 Indian Type Foundry 策展的高质量免费字体,适合品牌与产品界面选型
- **输入 → 输出**: 浏览 / 配对字体 → 下载字体文件或获取使用方式
- **是否需写码**: 否(选型);上线需接入字体文件或托管
- **框架兼容**: 无(字体资源)
- **许可证 / 价格**: 免费商用(以各字体许可证为准)
- **何时选它**: 需要比系统字体更有辨识度、又要可商用的西文 / 多文体时
- **搭配**: 配 SYS-001 看真实产品字体搭配;中文项目需另配中文字体方案
- **标签**: `component` `font`

### CMP-011 · 1001 Free Fonts

- **官网**: https://www.1001freefonts.com/
- **类型**: 免费字体下载库(个人免费)
- **用途**: 浏览海量分类字体(Comic / Calligraphy / Script / Retro / Horror / Blackletter 等),下载用于个人项目或字体选型参考
- **输入 → 输出**: 按分类或关键词浏览 → 下载字体文件(zip)
- **是否需写码**: 否(选型 / 下载)
- **框架兼容**: 无(字体资源)
- **许可证 / 价格**: 个人使用免费;**商用需单独购买许可**(每款字体旁有 Buy Commercial License 入口,以官网为准)
- **何时选它**: 需要大量风格化字体做选型浏览、个人项目或原型时;商用项目优先用 CMP-010 Fontshare
- **搭配**: 商用选 CMP-010 Fontshare;配 SYS-001 看真实产品字体搭配
- **标签**: `component` `font`

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

### MOT-006 · Rive

- **官网**: https://rive.app
- **类型**: 交互式状态机动效工具
- **用途**: 设计可响应状态 / 输入的矢量动效(按钮、图标、角色、加载态),导出到 App 与 Web 运行时
- **输入 → 输出**: 在编辑器做动画与状态机 → Rive 文件 + 运行时集成
- **是否需写码**: 设计阶段否;产品集成需写码
- **框架兼容**: Web / iOS / Android / Flutter / React Native 等(见官网运行时)
- **许可证 / 价格**: 有免费档;团队与高级能力见官网定价
- **何时选它**: 需要比 Lottie 更强的交互状态、运行时可控动效时
- **搭配**: 简单循环动画可先看 MOT-005;网页交接可配 DEV-001
- **标签**: `motion-design` `animation`

### MOT-007 · Spline

- **官网**: https://spline.design
- **类型**: Web 3D 设计工具
- **用途**: 在浏览器中设计 3D 场景与物件,导出到网页或 React 集成
- **输入 → 输出**: 可视化搭建 3D → 可嵌入的 3D 场景 / 代码集成
- **是否需写码**: 设计阶段否;深度集成需写码
- **框架兼容**: Web / React 等导出方式见官网
- **许可证 / 价格**: 有免费档;付费计划见官网
- **何时选它**: Hero 或产品展示需要实时 3D、又不想从 Zero 写 Three.js 时
- **搭配**: 配 CMP-001 做非 3D 的 Shader 渐变;注意性能与移动端兜底
- **标签**: `motion-design` `3d` `shader`

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
- **搭配**: 配 DEV-003 GSAP 做复杂时间线;配 CMP-* 组件
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
- **搭配**: 配 SYS-002 Open Design 的视频模板;时间线能力可参考 DEV-003
- **标签**: `video` `animation`

### DEV-003 · GSAP

- **官网**: https://gsap.com
- **类型**: 专业级 Web 动画库
- **用途**: 用 Tween / Timeline / ScrollTrigger 等实现复杂时间线、滚动叙事与高性能网页动画
- **输入 → 输出**: 编写 GSAP 代码 → 时间线驱动的页面动画
- **是否需写码**: 是
- **框架兼容**: 框架无关(原生 JS);可与 React / Vue 等集成
- **许可证 / 价格**: 核心免费;部分插件需付费订阅(以官网为准)
- **何时选它**: 滚动叙事、复杂编排、对性能与时间线控制要求高时
- **搭配**: 先用 INS-002 找案例模式;组件级微交互可优先 DEV-001
- **标签**: `animation`

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

### SYS-003 · Mobbin

- **官网**: https://mobbin.com
- **类型**: 真实产品 UI / UX 参考库
- **用途**: 检索 iOS、Web App 与网站的真实界面、组件模式与用户流程;也可通过 MCP 供 AI agent 查阅
- **输入 → 输出**: 按模式 / 流程 / 截图检索 → 可参考的真实产品界面与流程
- **是否需写码**: 否(参考);落地需自行设计或实现
- **框架兼容**: 无
- **许可证 / 价格**: 有免费浏览限制;Pro / Team 等付费计划见官网
- **何时选它**: 做产品界面、 onboard / 支付 / 设置等流程,需要看头部 App 怎么做时
- **搭配**: 配 SYS-001 看设计令牌;配 INS-* 看营销站风格(二者不要混用场景)
- **标签**: `design-system` `gallery` `design-extraction`

---

## 六、AI 设计与动效 Skills

用于扩展 AI Agent 的设计、动效与前端能力。安装路径与兼容性取决于具体工具;不要默认所有 Skill 都能跨平台无修改运行。

### 推荐首选 · website-studio(本仓库维护)

- **位置**: [`./website-studio/SKILL.md`](./website-studio/SKILL.md)(本仓库内置,无需另装)
- **类型**: 全自动建站方法论 Skill
- **用途**: 把"我想做个网站"变成有品味、可上线的成品;覆盖意图捕获、参考 DNA 提取、设计文档契约、动效策展、实现与验收六阶段;内置反默认纪律、Hero 构图原型库、丰富度等级、高级感物理层、反廉价黑名单
- **输入 → 输出**: 一句话需求 + 可选参考 → 可上线的网页成品 + DESIGN.md
- **是否需写码**: 否(agent 全权决策工程,用户只参与审美)
- **框架兼容**: Vite / Next.js + React + Tailwind 为主,可适配单文件 HTML
- **许可证 / 价格**: 免费(以仓库 LICENSE 为准)
- **何时选它**: 用户要做任何网页类产物(网站 / 落地页 / 作品集 / 仪表盘 / 活动页)时,首选此 skill
- **搭配**: 内部 `resource-map.md` 指向本目录资源;配 SKL-001 / SKL-009 做设计提取
- **标签**: `agent-skill` `motion-design` `design-system`

### SKL-001 · Taste Skill

- **位置**: https://github.com/senlindesign/taste-skill
- **类型**: 设计分析 Skill
- **用途**: 提取网站的设计令牌和"为什么这么设计"的取舍逻辑,转成可解释的设计 DNA
- **输入 → 输出**: 网站 URL → 设计令牌 + 取舍说明
- **是否需写码**: 否
- **框架兼容**: Agent Skill(见仓库说明)
- **许可证 / 价格**: 见仓库
- **何时选它**: Phase 1 要把参考站转成结构化设计 DNA 时
- **搭配**: 配 SKL-009 产出 DESIGN.md;配 website-studio
- **标签**: `agent-skill` `design-extraction`

### SKL-002 · Impeccable

- **位置**: https://github.com/pbakaus/impeccable
- **类型**: 前端设计 Skill 包
- **用途**: 改善 AI 生成界面的视觉判断与设计语言,在生成或审查前端页面时提供设计约束
- **输入 → 输出**: 页面或设计意图 → 设计约束 + 审查反馈
- **是否需写码**: 否(约束层)
- **框架兼容**: Agent Skill
- **许可证 / 价格**: 见仓库
- **何时选它**: 要提升 AI 生成界面的视觉品质、或审查前端设计时
- **搭配**: 配 website-studio 的反廉价黑名单
- **标签**: `agent-skill` `design-system`

### SKL-003 · shadcn/ui Skill

- **位置**: https://ui.shadcn.com/docs/skills
- **类型**: 组件知识 Skill
- **用途**: 按官方模式使用 shadcn/ui 的组件、模式与最佳实践
- **输入 → 输出**: 组件需求 → 选型 + 安装 + 组合方式
- **是否需写码**: 是(组件集成)
- **框架兼容**: React + Tailwind
- **许可证 / 价格**: 见官网
- **何时选它**: 用 shadcn/ui 做基础组件层时
- **搭配**: 配 CMP-008 shadcn/ui
- **标签**: `agent-skill` `component` `react`

### SKL-004 · AI Website Clone

- **位置**: https://github.com/nelakay/ai-website-cloner-claudeskill
- **类型**: 网站复刻 Skill
- **用途**: 从现有网页提取结构并生成前端实现;用于经授权的页面实现或内部原型,避免侵权复制
- **输入 → 输出**: 网站 URL → 前端实现代码
- **是否需写码**: 否(agent 生成)
- **框架兼容**: 见仓库
- **许可证 / 价格**: 见仓库
- **何时选它**: 需要快速复刻某站结构做原型时(注意版权)
- **搭配**: 配 SKL-001 提取 DNA 再复刻更稳
- **标签**: `agent-skill` `design-extraction`

### SKL-005 · Guizang Social Card

- **位置**: https://github.com/op7418/guizang-social-card-skill
- **类型**: 社交视觉 Skill
- **用途**: 按平台尺寸与内容结构生成社交卡片、封面和动态内容
- **输入 → 输出**: 文案或主题 → 社交卡片视觉
- **是否需写码**: 否
- **框架兼容**: Agent Skill
- **许可证 / 价格**: 见仓库
- **何时选它**: 需要生成社交分享卡片或封面时
- **搭配**: 配 MOT-* 做动态版
- **标签**: `agent-skill` `motion-design`

### SKL-006 · Pixel2Motion

- **位置**: https://github.com/nolangz/pixel2motion
- **类型**: Logo 动效 Skill
- **用途**: 将位图 Logo 转成 SVG 并生成动效预览
- **输入 → 输出**: 位图 Logo → SVG + 动效预览
- **是否需写码**: 否
- **框架兼容**: Agent Skill
- **许可证 / 价格**: 见仓库
- **何时选它**: 需要把客户给的位图 Logo 做成动效时
- **搭配**: 配 MOT-001 Jitter
- **标签**: `agent-skill` `animation`

### SKL-007 · Text-to-Lottie

- **位置**: https://github.com/diffusionstudio/lottie
- **类型**: Lottie 生成 Skill / 工具
- **用途**: 从自然语言生成和预览 Lottie 动画
- **输入 → 输出**: 自然语言描述 → Lottie JSON + 预览
- **是否需写码**: 否
- **框架兼容**: Agent Skill
- **许可证 / 价格**: 见仓库
- **何时选它**: 需要快速生成矢量动画、不想手画 Lottie 时
- **搭配**: 配 MOT-005 LottieFiles 校验
- **标签**: `agent-skill` `lottie`

### SKL-008 · GSAP Skill(官方)

- **位置**: https://github.com/greensock/gsap-skills
- **类型**: GSAP 编码 Skill
- **用途**: 使用 GSAP、Timeline 和 ScrollTrigger 实现网页动效;为 agent 提供官方动画模式与框架集成指导
- **输入 → 输出**: 动效需求 → GSAP 代码
- **是否需写码**: 是
- **框架兼容**: 框架无关(GSAP 原生 JS)
- **许可证 / 价格**: 见仓库
- **何时选它**: 用 DEV-003 GSAP 做复杂动画时,加载此 skill 给 agent 官方模式
- **搭配**: 配 DEV-003 GSAP;配 INS-002 案例
- **标签**: `agent-skill` `animation`

### SKL-009 · Web to Design MD

- **位置**: https://github.com/Paidax01/web-to-design-md
- **类型**: 设计提取 Skill
- **用途**: 将网页整理成可复用的 DESIGN.md 与预览
- **输入 → 输出**: 网站 URL → DESIGN.md + 预览
- **是否需写码**: 否
- **框架兼容**: Agent Skill
- **许可证 / 价格**: 见仓库
- **何时选它**: 要把视觉参考转成结构化设计规范时
- **搭配**: 配 SKL-001;配 website-studio Phase 2
- **标签**: `agent-skill` `design-extraction`

### SKL-010 · Remotion Skill

- **位置**: https://github.com/wshuyi/remotion-video-skill
- **类型**: 编程视频 Skill
- **用途**: 使用 React 和 Remotion 生成视频;让 agent 编写场景、时间线和渲染流程
- **输入 → 输出**: 视频需求 → Remotion 场景代码 + 渲染流程
- **是否需写码**: 是(React)
- **框架兼容**: React + Remotion
- **许可证 / 价格**: 见仓库
- **何时选它**: 需要编程式视频、且选用 Remotion 而非 HyperFrames 时
- **搭配**: 配 DEV-002 HyperFrames(另一种视频方案)
- **标签**: `agent-skill` `video` `react`

### SKL-011 · Motion Design Director

- **位置**: https://github.com/liangming99/motion-design-director-skill
- **类型**: 动效指导 Skill
- **用途**: 规划、批评和优化动效方案;让 agent 先制定动效语言和节奏,再生成实现草图
- **输入 → 输出**: 项目需求 → 动效方案 + 节奏规范 + 草图
- **是否需写码**: 否(指导层)
- **框架兼容**: Agent Skill
- **许可证 / 价格**: 见仓库
- **何时选它**: 动效方向不清、需要先定语言和节奏再动手时
- **搭配**: 配 website-studio 的丰富度等级
- **标签**: `agent-skill` `motion-design`

---

## 七、Skills 生态与发现目录

用于寻找更多 Skill、参考规范或组合式技能包。

### ECO-001 · Anthropic 官方 Skills

- **位置**: https://github.com/anthropics/skills
- **类型**: 官方 Skill 仓库
- **用途**: 参考 Agent Skill 的结构和官方示例;让 agent 优先学习权威实现与安全边界
- **输入 → 输出**: 浏览示例 → Skill 结构参考
- **是否需写码**: 否(参考)
- **框架兼容**: Claude 生态
- **许可证 / 价格**: 见仓库
- **何时选它**: 学习 Skill 规范、看官方示例时
- **搭配**: 配 ECO-002 / ECO-003
- **标签**: `directory` `agent-skill`

### ECO-002 · Claude Design Skillstack

- **位置**: https://github.com/freshtechbro/claudedesignskills
- **类型**: 设计技能集合
- **用途**: 获取 3D、WebGL、动效和现代前端相关能力;按任务选取子 Skill
- **输入 → 输出**: 浏览子 Skill → 按需安装
- **是否需写码**: 视子 Skill 而定
- **框架兼容**: Claude 生态
- **许可证 / 价格**: 见仓库
- **何时选它**: 需要多个设计相关子 Skill 组合时
- **搭配**: 按任务选,不要一次加载无关能力
- **标签**: `directory` `agent-skill` `motion-design`

### ECO-003 · The Skills Directory

- **位置**: https://theskills.directory
- **类型**: Skill 搜索目录
- **用途**: 搜索不同生态中的 Agent Skills;用作发现入口
- **输入 → 输出**: 关键词搜索 → Skill 列表
- **是否需写码**: 否
- **框架兼容**: 跨生态
- **许可证 / 价格**: 免费浏览
- **何时选它**: 要发现更多 Skill、跨生态搜索时
- **搭配**: 安装前回到源码仓库审查
- **标签**: `directory` `agent-skill`

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
2. 需要网页交互时使用 `DEV-001` Motion;复杂时间线 / 滚动叙事优先 `DEV-003` GSAP(案例可参考 `INS-002`)。
3. 需要跨端矢量动画时输出 Lottie,并用 `MOT-005` 检查;需要状态机交互动效用 `MOT-006` Rive。
4. 需要 Web 3D 展示时考虑 `MOT-007` Spline。
5. 需要视频流水线时选择 `DEV-002` HyperFrames。

### 3. 从参考网站到设计规范

1. 从多个 `INS-*` 案例提取共同特征。
2. 用 `SYS-001` 查找接近的真实设计系统;做产品流程时用 `SYS-003` Mobbin。
3. 整理成结构化规范(色彩 / 字体 / 间距 / 组件)。
4. 让 AI 按规范自主选择组件,并通过反馈迭代,而不是逐页硬抄。

---

## 贡献规范

新增资源时:

1. 选择唯一主分类和下一个稳定 ID(沿用现有前缀:INS / CMP / MOT / DEV / SYS / SKL / ECO)。
2. 使用官方主页或官方源码仓库链接。
3. 描述"适合解决什么问题",避免广告式形容词和易过时的数量。
4. 明确它是灵感、工具、代码库还是组件库。
5. 给出 2 至 3 个受控标签(见标签词表)。
6. 不确定许可证、价格或兼容性时不要猜测,直接提示读者查看官方说明。

---

## 更新记录

- **2026-07-19 · v3.3**:恢复 Skills 分类(原 v3.0 移除的 14 条外部 skill 全部回归,链接已核验有效);旗舰 skill `website-studio` 作为"推荐首选"置顶 Skills 分类,完整文件打包进 `website-studio/` 子目录(克隆即用);范围说明、导航、标签词表、决策树同步更新;skill 内部 `resource-map.md` 去重,灵感站列表改为指向上级 README;条目总数 32 → 47。
- **2026-07-19 · v3.2**:新增 CMP-011 1001 Free Fonts(海量免费字体下载库,个人免费、商用需购许可),与 CMP-010 Fontshare(免费商用)区分定位;决策树同步加"海量字体浏览 / 个人下载"行;条目总数 31 → 32。
- **2026-07-19 · v3.1**:新增 10 条高质量资源,补齐策展灵感、Web Prompt、基础组件、图标字体、Rive / Spline、GSAP、Mobbin 等缺口;决策树与工作流同步更新;修复 MotionSites 用途字段乱码;条目总数 21 → 31。
- **2026-07-19 · v3.0**:移除原"六、AI 设计与动效 Skills"与"七、Skills 生态与发现目录"共 14 条,使本目录成为纯设计资源库;保留的 21 条资源全量字段化增强(用途 / 输入输出 / 是否写码 / 框架兼容 / 许可证 / 何时选 / 搭配);新增"我要做什么,用哪个"决策树;合并为单文件 README;重写推荐工作流去除 Skill 依赖。
- **2026-07-14 · v2.0**:重新按任务分类;增加稳定 ID、AI 使用规则、标签词表和贡献规范;加入 Jitter;移除容易过时的数量与绝对化表述。
- **2026-07-10 · v1.0**:创建初始资源清单。
