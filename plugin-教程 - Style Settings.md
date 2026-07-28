---
created: 2026-07-28
plugin-id: obsidian-style-settings
plugin-name: Style Settings
plugin-author: mgmeyers
rank: "#8"
downloads: 2,529,630
tags: [plugin-tutorial, css, theme]
---

# Style Settings 使用教程

> **排名 #8 / 6,081** · 下载量 **2,529,630** · 作者：mgmeyers

---

## 📋 简介

Style Settings 是 Obsidian 的**CSS 可视化配置面板**。它允许主题和代码片段作者定义可调参数（颜色、字体、间距等），用户无需编辑 CSS 即可在统一的设置界面中调整 Obsidian 的外观。

---

## 🚀 快速上手

### 安装
设置 → 社区插件 → 搜索 "Style Settings" → 安装并启用。

### 使用
安装后重启，在设置面板中会出现 **Style Settings** 选项页。如果当前主题或 CSS 代码片段定义了配置参数，这里就会显示对应的设置开关、滑块、颜色选择器和下拉菜单。

---

## 🎯 CSS 配置语法（面向主题/片段作者）

在 CSS 文件中使用 `/* @settings */` 注释块定义可配置项：

```css
/* @settings

name: 我的主题配置
id: my-theme
settings:
    -
        id: accent-color
        title: 主题色
        type: variable-color
        format: hsl-split
        default: "#007AFF"

    -
        id: ui-font
        title: 界面字体
        type: variable-text
        default: -apple-system, sans-serif

    -
        id: sidebar-width
        title: 侧边栏宽度
        type: variable-number-slider
        default: 300
        min: 200
        max: 500
        step: 10
        format: px
*/
```

---

## 📋 所有设置类型详解

### 1️⃣ heading（标题）
用于组织分组，可折叠：
```css
settings:
    -
        id: section-heading
        title: 外观设置
        type: heading
        level: 2
        collapsed: true   /* 默认折叠 */
```

### 2️⃣ info-text（信息文本）
展示说明文字，支持 Markdown：
```css
    -
        id: info
        title: 使用说明
        description: "这是 *提示* 文本"
        type: info-text
        markdown: true
```

### 3️⃣ class-toggle（类切换开关）
在 `body` 上切换 CSS 类，支持快捷键：
```css
    -
        id: my-css-class
        title: 我的开关
        type: class-toggle
        addCommand: true   /* 添加到命令面板 */
```

### 4️⃣ class-select（类选择下拉）
从预定义类中选择：
```css
    -
        id: theme-variant
        title: 主题变体
        type: class-select
        allowEmpty: false
        default: my-class
        options:
            - label: 浅色
              value: theme-light-mode
            - label: 深色
              value: theme-dark-mode
```

### 5️⃣ variable-text（文本变量）
任意 CSS 文本值，可加引号：
```css
    -
        id: text-font
        title: UI 字体
        type: variable-text
        default: -apple-system, sans-serif
        quotes: true       /* 输出带引号 */
```
输出：`--text-font: "-apple-system, sans-serif";`

### 6️⃣ variable-number（数字变量）
数字值，可带单位：
```css
    -
        id: line-width
        title: 行宽
        type: variable-number
        default: 42
        format: rem
```
输出：`--line-width: 42rem;`

### 7️⃣ variable-number-slider（滑块数字）
带滑块的数字选择：
```css
    -
        id: spacing
        title: 间距
        type: variable-number-slider
        default: 16
        min: 0
        max: 48
        step: 2
        format: px
```

### 8️⃣ variable-select（下拉选择）
预定义选项的下拉菜单：
```css
    -
        id: font
        title: 正文字体
        type: variable-select
        default: Roboto
        options:
            - Roboto
            - "Helvetica Neue"
            - sans-serif
```

### 9️⃣ variable-color（颜色选择器）

```css
    -
        id: accent
        title: 强调色
        type: variable-color
        format: hex
        opacity: false
        alt-format:
            - id: accent-rgb
              format: rgb
        default: "#007AFF"
```

**支持的 format 格式：**

| 格式 | 输出示例 |
|------|---------|
| `hex` | `--accent: #007AFF;` |
| `rgb` | `--accent: rgb(0, 122, 255);` |
| `rgb-values` | `--accent: 0, 122, 255;` |
| `rgb-split` | `--accent-r: 0; --accent-g: 122; --accent-b: 255;` |
| `hsl` | `--accent: hsl(211, 100%, 50%);` |
| `hsl-split` | `--accent-h: 211; --accent-s: 100%; --accent-l: 50%;` |

### 🔟 variable-themed-color（双主题颜色）
同时生成亮色/暗色两个颜色选择器：
```css
    -
        id: bg
        title: 背景色
        type: variable-themed-color
        format: hex
        default-light: "#FFFFFF"
        default-dark: "#1E1E1E"
```
输出：
```css
body.theme-light.css-settings-manager { --bg: #FFFFFF; }
body.theme-dark.css-settings-manager  { --bg: #1E1E1E; }
```

### 1️⃣1️⃣ color-gradient（渐变色）
在两个颜色变量之间生成渐变色阶：
```css
    -
        id: color-base
        type: color-gradient
        from: color-base-00
        to: color-base-100
        step: 5
        pad: 2
        format: hex
```

---

## 💡 使用技巧

### 查看主题支持
安装新主题后，在 Style Settings 面板中查看是否有可调选项。热门主题均深度支持：
- **Minimal** — 最丰富的 Style Settings 支持
- **Blue Topaz** — 大量自定义选项
- **AnuPpuccin** — 完整配置界面
- **Primary / Things** — 部分支持

### 组合多个代码片段
多个 CSS 代码片段可各自定义 `@settings`，所有配置会合并展示在同一个面板。

### 配置导出
在 Style Settings 面板底部点击 **Copy Settings** 可将所有配置复制到剪贴板，方便备份或分享。

### 本地化支持
支持多语言标题和描述：
```css
    -
        id: setting
        title: My Setting
        title.zh: 我的设置
        title.de: Meine Einstellung
        description: Description
        description.zh: 描述文本
        description.de: Beschreibungstext
```

---


## ⚙️ 设置选项详解

Style Settings 插件本身在 Obsidian 设置面板中的可配置项很少，它的核心能力是提供一个 **可视化配置界面**，让主题和 CSS 片段作者定义的参数以开关、滑块、颜色选择器等形式展示。

### 插件自身设置

在 Obsidian 设置 → 社区插件 → Style Settings 下：

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Snippet folder** | .obsidian/snippets/ | 扫描 CSS 代码片段的目录路径 | 保持默认 |
| **Scan theme CSS** | ✅ 开启 | 自动扫描当前主题 CSS 中的 @settings 定义 | ✅ 开启 |
| **Scan plugin CSS** | ❌ 关闭 | 扫描已启用的社区插件 CSS 中的 @settings 定义 | ⚠️ 按需（开启可能影响启动性能） |
| **Enable advanced CSS classes** | ✅ 开启 | 在 ody 上启用 .css-settings-manager 类 | ✅ 开启 |

### 配置管理（面板底部按钮）

| 操作 | 说明 |
|------|------|
| **Copy Settings** | 将当前所有样式设置复制到剪贴板（JSON 格式），用于备份或分享主题配置 |
| **Paste Settings** | 从剪贴板粘贴 JSON 配置并应用 |
| **Reset to defaults** | 将所有样式设置恢复为默认值 |
| **Clear all settings** | 清除所有样式设置 |

> 💡 **注意**：Style Settings 面板中具体显示什么设置项，完全由你**当前安装的主题**和**启用的 CSS 代码片段**决定。安装一个新的主题后，打开 Style Settings 面板即可看到该主题暴露的全部可调参数。热门主题如 **Minimal**、**Blue Topaz**、**AnuPpuccin** 均有深度支持。

### 推荐的常用 CSS 设置项示例（以 Minimal 主题为例）

安装 Minimal 主题后，Style Settings 面板会出现以下常见选项：

| 设置分组 | 包含选项 |
|---------|---------|
| **Accent** | 主题色选择、强调色深浅模式 |
| **Background** | 编辑器背景色、侧边栏背景色、Hover 背景色 |
| **Borders** | 边框颜色、边框圆角大小、边框宽度 |
| **Typography** | 正文字体、标题字体、UI 字体、字号缩放、行高、最大行宽 |
| **Icons** | 图标风格（Lucide / 无图标）、图标颜色 |
| **Tabs** | 标签页高度、标签页圆角、标签页样式 |
| **Sidebars** | 侧边栏宽度、导航项间距、文件图标显示 |
| **Tables** | 表格样式、表格单元格间距 |
| **Callouts** | Callout 颜色、Callout 图标、折叠动画 |
| **Publish** | Publish 站点宽度、字体设置 |

## 🔗 资源

| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/mgmeyers/obsidian-style-settings |
| 默认主题 CSS 变量 | https://github.com/mgmeyers/obsidian-style-settings/blob/main/obsidian-default-theme.css |
| 问题反馈 | https://github.com/mgmeyers/obsidian-style-settings/issues |

---

> 📝 本文档由 Claudian 检索官方文档后补充完整 · 最后更新 2026-07-28

