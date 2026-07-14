---
title: 设计、动效与 AI 前端资源目录
version: "2.0"
updated_at: "2026-07-14"
language: zh-CN
entry_count: 35
catalog_type: design-motion-ai-resources
---

# 设计、动效与 AI 前端资源目录

这是一份面向设计师、开发者和 AI Agent 的策展型资源目录，覆盖设计灵感、UI 组件、动效制作、前端动画、设计规范与 Agent Skills。

> 本目录提供“发现与选型”，不等同于对价格、许可证、安全性或长期可用性的背书。使用前请查看资源的官方说明；安装第三方 Skill 前，请审查其 `SKILL.md`、脚本、依赖和权限。

## 快速导航

| 任务 | 优先查看 |
|---|---|
| 找网页视觉方向或案例 | [设计灵感与案例](#一设计灵感与案例) |
| 找可直接用于网页的组件 | [UI 组件与视觉资源](#二ui-组件与视觉资源) |
| 制作品牌动效、GIF、Lottie 或视频 | [动效设计与视觉制作工具](#三动效设计与视觉制作工具) |
| 在代码中实现动画或渲染视频 | [前端动画与视频技术](#四前端动画与视频技术) |
| 提取设计规范、研究设计系统或做原型 | [设计规范、参考与工作空间](#五设计规范参考与工作空间) |
| 给 AI Agent 增加设计或动效能力 | [AI 设计与动效 Skills](#六ai-设计与动效-skills) |
| 继续寻找更多 Skills | [Skills 生态与发现目录](#七skills-生态与发现目录) |

## 给 AI Agent 的使用规则

1. 先根据用户目标选择分类，再从分类中挑选资源；不要把灵感站、可视化工具、代码库和 Agent Skill 混为一谈。
2. 每次推荐优先给出 1–3 个资源，并说明选择原因、输入形式、输出形式和是否需要写代码。
3. “AI 使用方式”表示适合怎样纳入 AI 工作流，不代表该资源一定提供官方 API、MCP 或 Skill。
4. 实施前重新核对官方文档、许可证、价格、框架版本和导出能力；这些信息可能变化。
5. 引用条目时优先使用稳定 ID，例如 `MOT-001`，方便后续讨论与自动化处理。
6. 同一资源只归入一个主分类；跨领域能力通过标签表达。

### 标签词表

`inspiration` · `gallery` · `prompt` · `component` · `react` · `animation` · `motion-design` · `lottie` · `video` · `shader` · `design-system` · `design-extraction` · `agent-skill` · `directory`

---

## 一、设计灵感与案例

用于寻找视觉方向、页面结构、动效案例和布局参考。这里的资源主要帮助“看”和“选方向”，不一定能直接产出代码。

| ID | 资源 | 类型 | 适合做什么 | AI 使用方式 | 标签 |
|---|---|---|---|---|---|
| INS-001 | [MotionSites](https://motionsites.ai) | Prompt / 页面灵感库 | 查找 Hero、动态背景、渐变和整页方向 | 根据产品概念检索或改写结构化设计 Prompt | `inspiration` `prompt` `motion-design` |
| INS-002 | [Made with GSAP](https://madewithgsap.com) | 动效案例画廊 | 研究滚动、拖拽、鼠标跟随和循环动画 | 先选动效模式，再交给 AI 用 GSAP 复现交互逻辑 | `inspiration` `gallery` `animation` |
| INS-003 | [Bento Grids](https://bentogrids.com) | 布局灵感库 | 查找 Bento 网格、卡片组合和信息层级 | 让 AI 提取布局规律，而不是照搬单个页面 | `inspiration` `gallery` `design-system` |
| INS-004 | [Godly / Recent](https://recent.design) | 网站灵感画廊 | 浏览高质量营销网站和数字产品案例 | 用作风格检索与案例对比，避免直接复刻 | `inspiration` `gallery` |
| INS-005 | [Awwwards](https://www.awwwards.com) | 设计奖项与案例平台 | 研究行业级网页设计、交互和创意方向 | 让 AI 总结多个案例的共同设计原则 | `inspiration` `gallery` `motion-design` |

---

## 二、UI 组件与视觉资源

用于直接选择、组合或实现网页组件。部分资源提供复制代码、安装包或设计工具导出，具体方式以官方文档为准。

| ID | 资源 | 类型 | 适合做什么 | AI 使用方式 | 标签 |
|---|---|---|---|---|---|
| CMP-001 | [Shader Gradient](https://shadergradient.co) | 3D 渐变生成器 / 组件 | 创建可动画的着色器渐变背景 | 生成视觉参数或导出组件后交给 AI 集成 | `component` `shader` `animation` |
| CMP-002 | [21st.dev](https://21st.dev) | AI 组件注册表 | 搜索和复用现代 Web UI 组件 | 让 AI 按页面需求检索组件并组合实现 | `component` `react` |
| CMP-003 | [React Bits](https://www.reactbits.dev) | React 动画组件库 | 使用可定制的文本、背景和交互组件 | 让 AI 选择组件、安装依赖并适配现有设计系统 | `component` `react` `animation` |
| CMP-004 | [Magic UI](https://magicui.design) | 动画 UI 组件库 | 构建营销页、展示区和高表现力交互 | 让 AI 复用组件并统一颜色、字体与动效节奏 | `component` `react` `animation` |
| CMP-005 | [Aceternity UI](https://ui.aceternity.com) | Tailwind / React 组件库 | 创建动态背景、卡片、导航和营销页面 | 让 AI 根据技术栈挑选组件并处理依赖 | `component` `react` `animation` |
| CMP-006 | [Uiverse](https://uiverse.io) | 社区 UI 元素库 | 查找按钮、加载器、开关和微交互 | 让 AI 选取单个元素并转换为项目所需样式 | `component` `animation` |
| CMP-007 | [OriginKit](https://www.originkit.dev) | 动效组件库 | 查找文本、图库和高装饰性互动组件 | 让 AI 通过组件或 MCP 工作流进行检索与集成 | `component` `react` `motion-design` |

---

## 三、动效设计与视觉制作工具

用于在可视化界面中制作品牌动效、社交内容、Shader、GIF、Lottie 或视频。它们不是前端组件库。

| ID | 资源 | 类型 | 适合做什么 | AI 使用方式 | 标签 |
|---|---|---|---|---|---|
| MOT-001 | [Jitter](https://jitter.video) | 在线动效设计工具 | 从静态设计制作品牌动画、社交视频和界面动效 | 导入 Figma 或使用 AI 生成可编辑动效，再导出视频、GIF 或 Lottie | `motion-design` `video` `lottie` |
| MOT-002 | [SuperOPC](https://superopc.app) | 设计灵感与动效工具集合 | 制作 ASCII、Dither、Logo 动效等视觉效果 | 用 AI 先确定视觉方向，再在工具中生成素材 | `motion-design` `shader` `inspiration` |
| MOT-003 | [Paper](https://paper.design) | 画布式设计工具 | 设计、编辑和分享网页视觉或可编辑图层 | 将网页组件或 AI 生成内容带入画布继续调整 | `motion-design` `design-system` |
| MOT-004 | [Shader（Flux Pic）](https://shaders.fluxpic.com) | Shader 效果生成器 | 为图片、Logo 和背景制作液态、半色调等效果 | 让 AI 推荐效果方向，再在工具中调参与导出 | `shader` `motion-design` |
| MOT-005 | [LottieFiles](https://lottiefiles.com) | Lottie 资源与编辑平台 | 查找、预览、编辑和交付 Lottie 动画 | 让 AI 根据场景筛选动画，并在集成前检查授权与性能 | `lottie` `animation` |

---

## 四、前端动画与视频技术

用于在代码中实现交互动画，或通过 Web 技术渲染视频。

| ID | 资源 | 类型 | 适合做什么 | AI 使用方式 | 标签 |
|---|---|---|---|---|---|
| DEV-001 | [Motion](https://motion.dev) | Web / React 动画库 | 实现组件过渡、手势、布局和时间线动画 | 让 AI 根据框架与交互复杂度生成动画代码 | `animation` `react` |
| DEV-002 | [HyperFrames](https://github.com/heygen-com/hyperframes) | HTML 视频渲染框架 | 用 HTML、CSS 和 JavaScript 构建可重复渲染的视频 | 让 Agent 生成确定性场景并通过渲染管线输出视频 | `video` `animation` |

---

## 五、设计规范、参考与工作空间

用于研究真实产品的设计系统、提取设计规则，或者在 AI 驱动的工作空间中完成原型。

| ID | 资源 | 类型 | 适合做什么 | AI 使用方式 | 标签 |
|---|---|---|---|---|---|
| SYS-001 | [Refero Styles](https://styles.refero.design/?sort=popular) | 设计系统参考库 | 查看真实产品网站的色彩、字体、间距和组件规范 | 让 AI 检索接近目标产品的设计系统并提取规则 | `design-system` `design-extraction` |
| SYS-002 | [Open Design](https://open-design.ai) | 开源 AI 设计工作空间 | 制作原型、落地页、仪表盘、Slides 和 HTML 视频 | 让 coding agent 在统一工作空间内生成并迭代设计 | `design-system` `motion-design` |

---

## 六、AI 设计与动效 Skills

下面这些资源用于扩展 AI Agent 的能力。安装路径和兼容性取决于具体工具；不要默认所有 Skill 都能跨平台无修改运行。

| ID | 资源 | 类型 | 适合做什么 | AI 使用方式 | 标签 |
|---|---|---|---|---|---|
| SKL-001 | [Taste Skill](https://github.com/senlindesign/taste-skill) | 设计分析 Skill | 提取网站的设计令牌和设计取舍 | 让 Agent 把参考站转成可解释的设计 DNA | `agent-skill` `design-extraction` |
| SKL-002 | [Impeccable](https://github.com/pbakaus/impeccable) | 前端设计 Skill 包 | 改善 AI 生成界面的视觉判断与设计语言 | 在生成或审查前端页面时提供设计约束 | `agent-skill` `design-system` |
| SKL-003 | [shadcn/ui Skill](https://ui.shadcn.com/docs/skills) | 组件知识 Skill | 使用 shadcn/ui 的组件、模式和最佳实践 | 让 Agent 按官方模式选择、安装和组合组件 | `agent-skill` `component` `react` |
| SKL-004 | [AI Website Clone](https://github.com/nelakay/ai-website-cloner-claudeskill) | 网站复刻 Skill | 从现有网页提取结构并生成前端实现 | 用于获得经授权的页面实现或内部原型，避免侵权复制 | `agent-skill` `design-extraction` |
| SKL-005 | [Guizang Social Card](https://github.com/op7418/guizang-social-card-skill) | 社交视觉 Skill | 生成社交卡片、封面和动态内容 | 让 Agent 按平台尺寸与内容结构生成视觉资产 | `agent-skill` `motion-design` |
| SKL-006 | [Pixel2Motion](https://github.com/nolangz/pixel2motion) | Logo 动效 Skill | 将位图 Logo 转成 SVG 并生成动效预览 | 让 Agent 完成矢量化、动画和预览输出 | `agent-skill` `animation` |
| SKL-007 | [Text-to-Lottie](https://github.com/diffusionstudio/lottie) | Lottie 生成 Skill / 工具 | 从自然语言生成和预览 Lottie 动画 | 让 Agent 生成 JSON，并在交付前验证渲染结果 | `agent-skill` `lottie` |
| SKL-008 | [GSAP Skill（官方）](https://github.com/greensock/gsap-skills) | GSAP 编码 Skill | 使用 GSAP、Timeline 和 ScrollTrigger 实现网页动效 | 为 Agent 提供官方动画模式与框架集成指导 | `agent-skill` `animation` |
| SKL-009 | [Web to Design MD](https://github.com/Paidax01/web-to-design-md) | 设计提取 Skill | 将网页整理成可复用的 DESIGN.md 与预览 | 让 Agent 把视觉参考转成结构化设计规范 | `agent-skill` `design-extraction` |
| SKL-010 | [Remotion Skill](https://github.com/wshuyi/remotion-video-skill) | 编程视频 Skill | 使用 React 和 Remotion 生成视频 | 让 Agent 编写场景、时间线和渲染流程 | `agent-skill` `video` `react` |
| SKL-011 | [Motion Design Director](https://github.com/liangming99/motion-design-director-skill) | 动效指导 Skill | 规划、批评和优化动效方案 | 让 Agent 先制定动效语言和节奏，再生成实现草图 | `agent-skill` `motion-design` |

### 常见 Skill 安装位置

以下只是常见约定，最终以各工具和仓库说明为准：

| 工具 | 常见目录 |
|---|---|
| Codex | `$CODEX_HOME/skills/` |
| Claude Code | `~/.claude/skills/` |
| Cursor | `~/.cursor/skills/` |
| 其他 Agent | 查看其 Skill / Plugin 文档 |

---

## 七、Skills 生态与发现目录

用于寻找更多 Skill、参考规范或组合式技能包。

| ID | 资源 | 类型 | 适合做什么 | AI 使用方式 | 标签 |
|---|---|---|---|---|---|
| ECO-001 | [Anthropic 官方 Skills](https://github.com/anthropics/skills) | 官方 Skill 仓库 | 参考 Agent Skill 的结构和官方示例 | 让 Agent 优先学习权威实现与安全边界 | `directory` `agent-skill` |
| ECO-002 | [Claude Design Skillstack](https://github.com/freshtechbro/claudedesignskills) | 设计技能集合 | 获取 3D、WebGL、动效和现代前端相关能力 | 按任务选取子 Skill，不要一次加载无关能力 | `directory` `agent-skill` `motion-design` |
| ECO-003 | [The Skills Directory](https://theskills.directory) | Skill 搜索目录 | 搜索不同生态中的 Agent Skills | 用作发现入口，安装前回到源码仓库审查 | `directory` `agent-skill` |

---

## 推荐工作流

### 1. 从产品概念到网页

1. 用产品文档和素材与 AI 对齐目标。
2. 从 `INS-*` 选择多个参考方向。
3. 从 `CMP-*` 选择组件，不直接复制单一参考站。
4. 用 `SKL-001`、`SKL-002` 或 `SKL-009` 提取并约束设计语言。
5. 用 `DEV-*` 实现交互，最后进行反馈校准。

### 2. 从静态视觉到动效

1. 用 `MOT-001` Jitter 或其他 `MOT-*` 工具制作可视化动效。
2. 需要网页交互时使用 `DEV-001` Motion，复杂时间线可结合 GSAP 相关资源。
3. 需要跨端矢量动画时输出 Lottie，并用 `MOT-005` 检查。
4. 需要视频流水线时选择 `DEV-002` 或 `SKL-010`。

### 3. 从参考网站到设计规范

1. 从多个 `INS-*` 案例提取共同特征。
2. 用 `SYS-001` 查找接近的真实设计系统。
3. 使用 `SKL-001` 或 `SKL-009` 生成结构化规范。
4. 让 AI 按规范自主选择组件，并通过反馈迭代，而不是逐页硬抄。

---

## 贡献规范

新增资源时：

1. 选择唯一主分类和下一个稳定 ID。
2. 使用官方主页或官方源码仓库链接。
3. 描述“适合解决什么问题”，避免广告式形容词和易过时的数量。
4. 明确它是灵感、工具、代码库还是 Skill。
5. 给出 2–3 个受控标签。
6. 不确定许可证、价格或兼容性时不要猜测，直接提示读者查看官方说明。

---

## 更新记录

- **2026-07-14 · v2.0**：重新按任务分类；增加稳定 ID、AI 使用规则、标签词表和贡献规范；加入 Jitter；移除容易过时的数量与绝对化表述。
- **2026-07-10 · v1.0**：创建初始资源清单。
