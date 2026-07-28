---
created: 2026-07-28
plugin-id: obsidian-excalidraw-plugin
plugin-name: Excalidraw
plugin-author: zsviczian
rank: "#1"
downloads: 6,864,510
tags: [plugin-tutorial, drawing, visual]
---

# Excalidraw 使用教程

> **排名 #1 / 6,081** · 下载量 **6,864,510** · 作者：zsviczian

---

## 📋 简介

Excalidraw 是 Obsidian 中最强大的**可视化笔记插件**。它将 Excalidraw 白板工具深度集成到 Obsidian 中，让你可以在笔记中直接绘制手绘风格的图表、流程图、思维导图等。支持 LaTeX 公式、脚本引擎、图片嵌入、Markdown 嵌入、OCR、自定义字体等高级功能。

---

## 🚀 快速上手

### 创建白板

命令面板（`Ctrl+P`）→ "Excalidraw: 新建绘图" 或在文件列表中右键创建 `.excalidraw.md` 文件。

### 基本工具

| 工具 | 快捷键 | 用途 |
|------|--------|------|
| 选区 | `V` | 选择和移动元素 |
| 矩形 | `R` | 绘制矩形 |
| 菱形 | `D` | 绘制菱形 |
| 椭圆 | `O` | 绘制椭圆/圆形 |
| 箭头 | `A` | 绘制箭头 |
| 线条 | `L` | 绘制线条 |
| 文本 | `T` | 添加文字 |
| 图片 | — | 插入图片 |
| 激光笔 | — | 演示时标记重点 |

---

## 🎯 核心功能

### 1️⃣ 超链接与拖放

在绘图文本中支持以下链接格式：
- 🌐 外部链接：`https://zsolt.blog` 或 `[Obsidian](https://obsidian.md)`
- 🔗 内部链接：`[[My file in vault|别名]]`
- 📄 嵌入：`![[myfile#^blockref]]` — 将绘图转换为嵌入文本

**拖放支持：**
- 从文件管理器拖入 → 创建文件链接
- 从网页拖入 → 创建链接（含缩略图）
- 按住 `Shift` 拖入 → 嵌入 Markdown 文件内容
- YouTube 链接 → 自动转为带缩略图的链接

### 2️⃣ LaTeX 公式

使用命令 `Insert LaTeX formula` 插入公式，`Ctrl/Cmd + 点击` 编辑：

```
$$\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$$
```

### 3️⃣ 嵌入笔记到绘图

拖入 `[[笔记名]]` 到画布即可，双击嵌入笔记可打开编辑。可以通过自定义 CSS 控制渲染样式。

### 4️⃣ 绘图嵌入到笔记

```markdown
![[绘图文件.excalidraw|100]]          # 宽度 100px
![[绘图文件.excalidraw|300x400]]      # 宽 300px，高 400px
![[绘图文件.excalidraw|200|left]]     # 左对齐
![[绘图文件.excalidraw|200|right-wrap]]  # 右环绕
```

### 5️⃣ 自定义 Frontmatter

在 `.excalidraw.md` 文件头部可设置：

```yaml
---
excalidraw-link-prefix: "📍"
excalidraw-url-prefix: "🌐"
excalidraw-default-mode: view
excalidraw-export-transparent: true
excalidraw-export-dark: false
excalidraw-export-pngscale: 2
---
```

### 6️⃣ Script Engine（脚本引擎）

Excalidraw 内置强大的脚本系统：
- 安装脚本：通过命令面板或 Script Store 安装
- 自定义自动化：用 JavaScript 编写 ExcalidrawAutomate 脚本
- 支持组织脚本到文件夹，在工具栏中分组显示

**常用脚本示例：**
- 自动绘制思维导图
- 批量调整元素样式
- 导出幻灯片
- 在 Obsidian Tools Panel 中组织脚本

### 7️⃣ 图片与 OCR

- 支持拖拽/粘贴/URL 插入图片
- **OCR 识别**：使用 Taskbone OCR 识别图片中的文字（需 API Key）
- **SVG 导入**：将 SVG 文件转换为 Excalidraw 绘图（保留可编辑性）

### 8️⃣ 自定义字体与颜色

- 在设置中添加第四种自定义字体（支持 woff/woff2/ttf）
- 通过模板自定义调色板
- 支持自定义笔刷和高亮笔

---

## 💡 最佳实践

1. **模板功能**：创建常用图表模板（流程图、时间线）
2. **配合 Dataview**：将 Dataview 查询结果嵌入白板
3. **块引用**：引用绘图中的特定元素 `[[file#^elementID]]` 或区域 `[[file#area=Section]]`
4. **分组与图层**：选中多元素按 `Ctrl+G` 分组
5. **自动导出**：设置开启自动导出 PNG/SVG，用于 Obsidian Publish
6. **演示模式**：设置 `excalidraw-default-mode: view` 打开即进入演示模式

---


---

## 🔗 资源

| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/zsviczian/obsidian-excalidraw-plugin |
| 官方文档 | https://zsviczian.github.io/obsidian-excalidraw-plugin/ |
| Excalidraw 脚本库 | https://github.com/zsviczian/excalidraw-scripts |
| 社区 Wiki | https://community.sketch-your-mind.com/Wiki |
| 免费课程 | https://community.sketch-your-mind.com/ee |


## ⚙️ 设置选项详解

Obsidian 设置 → 社区插件 → Excalidraw 下有大量可配置选项，按功能分组如下：

### Basic（基础设置）

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Drawing folder** | 空（Vault 根目录） | 新绘图文件的默认存储路径 | `drawings/` 或 `20.diary/attachments` |
| **Auto-save interval** | 30 秒 | 自动保存间隔 | 30 秒（默认即可） |

### Saving（保存设置）

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Compress JSON** | 在 Markdown 中压缩 Excalidraw JSON 数据 | ✅ 开启（减少文件大小） |
| **Decompress JSON in Markdown view** | 在 Markdown 源码中显示可读 JSON | 仅编辑模板时临时开启 |

### Filename（文件命名）

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Date format** | 自动文件名中的日期格式，默认 `YYYYMMDD` | `YYYYMMDDHHmm`（到分钟） |
| **Prefix / Suffix** | 文件名前后缀 | 如 `ex_` 前缀 |

### Display（显示设置）

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Left-handed mode** | 翻转工具栏到右侧 | 左撇子开启 |
| **Zoom to fit** | 打开时自动适配画布内容 | ✅ 开启 |
| **Mouse wheel zoom** | 滚轮缩放 | ✅ 开启 |
| **Theme** | 跟随 Obsidian 主题 / 强制亮色 / 强制暗色 | `跟随系统` |

### Links & Transclusions（链接设置）

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Auto-update links** | 文件移动时自动更新绘图中的链接 | ✅ 开启 |
| **Default link prefix** | 内部链接的预览前缀，如 `📍` | `📍`（便于区分） |
| **URL prefix** | 外部链接的预览前缀，如 `🌐` | `🌐` |

### Markdown Embed（Markdown 嵌入）

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Default font** | 渲染嵌入 Markdown 时的字体 | `Virgil`（手绘风格） |
| **Custom CSS** | 嵌入 Markdown 的自定义样式 | 可引用 `.css` 文件 |

### Embed & Export（嵌入与导出）

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Default width** | 嵌入笔记时的默认宽度，如 `400` | `400` |
| **Export type** | 嵌入时插入 `SVG` / `PNG` / `原文件` | `SVG`（矢量可缩放） |
| **Background** | 导出时是否包含白色背景 | 按需要（透明适合深色主题） |

### Auto-export（自动导出）

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Auto-export to SVG/PNG** | 每次保存时自动导出图片副本 | 需要发布或分享时开启 |
| **Keep in sync** | Markdown 嵌入与导出的 SVG/PNG 保持同步 | ⚠️ 开启可能影响性能 |

### Experimental（实验性功能）

| 设置项 | 说明 |
|--------|------|
| **Fourth font** | 添加第 4 种自定义字体（woff/woff2/ttf） |
| **Custom icon** | 在文件管理器中为 Excalidraw 文件设置自定义图标 |
| **OCR settings** | 配置 Taskbone OCR 的 API Key |

---

---

> 📝 本文档由 Claudian 检索官方文档后补充完整 · 最后更新 2026-07-28

