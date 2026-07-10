# 设计 / 动效 / 前端 资源清单

整理时间：2026-07-10
主题：动效、前端设计组件、AI 编码技能（Skills）。所有 Skill 均遵循 SKILL.md 开放标准，可装在 Claude Code / Cursor / Codex / WorkBuddy 等支持 Skill 机制的 agent 上。

---

## 一、灵感网站（6 个）

| # | 名称 | 网址 | 一句话说明 |
|---|------|------|-----------|
| 1 | Shader Gradient | https://shadergradient.co | 用着色器生成可动的 3D 渐变，可导出 React / Framer / Figma 组件（开源：github.com/ruucm/shadergradient） |
| 2 | 21st.dev | https://21st.dev | AI 原生组件注册表，Magic UI、Aceternity 等组件库都托管于此，复制即用 |
| 3 | MotionSites | https://motionsites.ai | 面向 AI 建站工具的结构化 Prompt 库：Hero 区、动态背景、渐变、整页模板 |
| 4 | React Bits | https://www.reactbits.dev | 100+ 开源动画 / 交互 React 组件，完全可定制（开源：github.com/DavidHDev/react-bits） |
| 5 | Made with GSAP | https://madewithgsap.com | 50 个 GSAP 精品动效 + Showcase 画廊（滚动 / 拖拽 / 鼠标跟随 / 无限循环） |
| 6 | Bento Grids | https://bentogrids.com | Bento 风格布局的策展灵感库，每周更新免费模板 |

---

## 二、AI 设计 / 动效 Skills（10 个）

| # | 名称 | 来源（GitHub） | 一句话说明 |
|---|------|----------------|-----------|
| 1 | Taste Skill | github.com/senlindesign/taste-skill | 反向提取任意网站的「设计 DNA」——设计令牌 + 背后的取舍逻辑，专治 AI 前端塑料味 |
| 2 | Impeccable | github.com/pbakaus/impeccable | 让 AI 编码助手更有「设计感」的前端设计语言技能包（前 Google DevRel 出品） |
| 3 | shadcn/ui Skill | 官方 ui.shadcn.com/docs/skills （另 github.com/mattbx/shadcn-skills） | 给 AI 注入 shadcn/ui 组件、模式与最佳实践的深度知识 |
| 4 | AI Website Clone | github.com/nelakay/ai-website-cloner-claudeskill （另 github.com/huangmingfu/clone-website） | 一条指令把任意网站像素级克隆成干净的 Next.js 代码 |
| 5 | Guizang Social Card | github.com/op7418/guizang-social-card-skill | 生成小红书图文 / 公众号封面 / Live Photo 动态社交卡片 |
| 6 | Pixel2Motion | github.com/nolangz/pixel2motion | 把位图 logo 转成干净 SVG，并生成动效 HTML / GIF / 视频预览 |
| 7 | Text-to-Lottie | github.com/diffusionstudio/lottie | 用自然语言生成生产级 Lottie 动画 JSON，内置 Skottie 实时预览 |
| 8 | GSAP Skill（官方） | github.com/greensock/gsap-skills | 官方 GSAP AI 技能，教 agent 正确使用 core / timeline / ScrollTrigger / React·Vue·Svelte |
| 9 | Web to Design MD | github.com/Paidax01/web-to-design-md | 把任意在线网站提取成可复用的 design.md 设计规范 + HTML 预览 |
| 10 | Remotion Skill | github.com/wshuyi/remotion-video-skill | 用自然语言驱动 Remotion 框架生成编程式视频（React 写视频） |

> 安装方式（WorkBuddy 为例）：把仓库里的 `SKILL.md`（及 `scripts/`）放到 `~/.workbuddy/skills/<技能名>/`，重启或新开会话即生效。
> Claude Code → `~/.claude/skills/`；Cursor → `~/.cursor/skills/`.

---

## 三、同类推荐（10 个，按你的口味挑的）

| # | 名称 | 网址 / 来源 | 类别 | 一句话说明 |
|---|------|------------|------|-----------|
| 1 | Magic UI | https://magicui.design | 组件库 | 150+ 免费动画组件，shadcn/ui 的官方好搭档（和 React Bits、21st 同类） |
| 2 | Aceternity UI | https://ui.aceternity.com | 组件库 | 200+ 免费 Tailwind + Framer Motion 动效组件，复制即用 |
| 3 | Motion（原 Framer Motion） | https://motion.dev | 动画库 | React 动画核心库，上面很多组件的动效底层都靠它 |
| 4 | Uiverse | https://uiverse.io | 组件库 | 社区贡献 4000+ 动画 UI 元素，CSS / Tailwind 一键复制 |
| 5 | Godly | https://godly.website（现跳转 recent.design） | 灵感画廊 | 1000+ 精选高品质网站设计灵感，动效参考利器 |
| 6 | Awwwards | https://www.awwwards.com | 灵感画廊 | 网页设计奖项与每日灵感，看顶级行业案例 |
| 7 | LottieFiles | https://lottiefiles.com | 动效资源 | Lottie 动画资源市场 + 在线编辑器，和 Text-to-Lottie 配套使用 |
| 8 | Anthropic 官方 Skills | https://github.com/anthropics/skills | 技能仓库 | Anthropic 官方 Agent Skills 仓库，权威参考 |
| 9 | Claude Design Skillstack | https://github.com/freshtechbro/claudedesignskills | 技能包 | 3D / WebGL / 动效 / 现代前端的设计技能栈，一站式 |
| 10 | The Skills Directory | https://theskills.directory | 技能目录 | 可搜索的 AI Skills 目录，找 skill 最方便的入口 |

---

## 四、补充资源（4 项，用户追加）

| # | 名称 | 网址 | 一句话说明 |
|---|------|------|-----------|
| 1 | SuperOPC | https://superopc.app | AI 时代设计灵感与资源库：网站灵感画廊 + 独家动效工具（ASCII/Dither、Motion 动态模板、Tracker 目标追踪、Apple 风格 Logo 动效）+ 品牌指南 / AI 教程 / Mockup |
| 2 | Paper | https://paper.design | 为 AI 时代打造的画布式设计工具（设计 / 分享 / 发布），可直接粘贴网页组件为可编辑图层，支持 macOS / Windows |
| 3 | Shader（Flux Pic） | https://shaders.fluxpic.com | 可视化 Shader 效果生成器（墨滴 / 光晕 / 背景等），支持上传 PNG / JPG / SVG（含 logo）预览液态金属、半色调、滤镜等效果 |
| 4 | Open Design | https://open-design.ai | 开源 vibe design workspace，Claude Design 的开源替代，用自己的 coding agent 做原型 / 落地页 / 仪表盘 / Slides / HTML 视频（另：opendesign.cc 是同类网页设计资源库，可下载完整设计系统） |

> 补充：SuperOPC 的 Logo 动效工具基于开源 **Paper Shader** 构建；若你说的「shader」特指 Paper Shader 项目本身，可与本表第 3 项的 Flux Pic 配合使用。

---

## 小贴士

- **组件库三件套**：React Bits / 21st / Magic UI / Aceternity 互为补充，建议都收藏，按场景挑。
- **动效链路**：GSAP（脚本动效）+ Motion（React 动效）+ Lottie（矢量动画）+ Remotion（编程视频）覆盖了从网页到视频的全链路。
- **设计提取**：Taste Skill + Web to Design MD + AI Website Clone 组合起来，可形成「拆解任意网站设计 → 复刻」的完整工作流。
- 以上 Skill 全部开源、免费；安装前建议像本次一样做一次安全审查（读 SKILL.md 与 scripts/）。
