---
created: 2026-07-28
plugin-id: obsidian-icon-folder
plugin-name: Iconize
plugin-author: florianwoelki
rank: "#10"
downloads: 2,139,580
tags: [plugin-tutorial, icons, customization]
---

# Iconize 使用教程

> **排名 #10 / 6,081** · 下载量 **2,139,580** · 作者：florianwoelki

---
> ⚠️ **维护终止通知**：该项目已停止维护，详见 [讨论页](https://github.com/FlorianWoelki/obsidian-iconize/discussions/646)。当前功能仍可正常使用，但未来可能不再更新。

## 📋 简介

Iconize（原名 Icon Folder）让你在 Obsidian 中**任何地方添加图标**。可以为文件、文件夹、笔记标题、标签页设置自定义图标，内置大量图标包，让你的 Vault 更直观、更个性化。

---

## 🚀 快速上手

### 安装
设置 → 社区插件 → 搜索 "Iconize" → 安装并启用。

### 给文件/文件夹添加图标
在文件资源管理器中**右键单击**文件或文件夹 → **选择图标** → 从图标库中选择。

### 给笔记标题添加图标
在笔记编辑界面**右键单击标题区域** → **选择标题图标**。

---

## 🎯 核心功能

### 1️⃣ 图标包

内置多种免费图标包：

| 图标包 | 数量 | 特点 |
|--------|------|------|
| **Font Awesome**（免费版） | 1500+ | 最流行的图标集 |
| **Lucide** | 1000+ | 简洁线条风格 |
| **Material Icons** | 2000+ | Google 设计风格 |
| **Tabler Icons** | 3000+ | 开源高质量图标 |
| **自定义 SVG** | 无限制 | 导入自己的 `.svg` 文件 |

### 2️⃣ 文件/文件夹图标

- 为单个文件或文件夹设置独立图标
- 图标显示在文件资源管理器中
- 支持按文件扩展名自动匹配图标（如 `.pdf` → 📄）

### 3️⃣ 标题图标

在笔记编辑器顶部标题前显示图标，让笔记更易识别。

### 4️⃣ 标签页图标

在打开的标签页上显示图标，配合颜色区分不同工作区。

### 5️⃣ 自定义规则（自动分配图标）

设置自动化规则，根据条件自动分配图标：

| 规则类型 | 示例 | 说明 |
|---------|------|------|
| 按路径 | `文件夹/项目/*` → 🚀 | 匹配文件夹路径 |
| 按标签 | `#daily` → 📅 | 匹配笔记标签 |
| 按文件名 | `*日记*` → 📖 | 文件名通配匹配 |
| 按扩展名 | `*.pdf` → 📄 | 文件类型自动识别 |

### 6️⃣ Frontmatter 集成

在笔记 YAML 中指定图标和颜色：

```yaml
---
icon: 📝
icon-color: "#FF5733"
---
```

图标会自动显示在文件资源管理器和标题区。

### 7️⃣ 图标颜色自定义

右键图标 → **选择颜色**，支持十六进制颜色码，可为不同类别设置颜色（如 🟢 学习、🔵 工作、🟡 生活）。

---


## ⚙️ 设置选项详解

Obsidian 设置 → 社区插件 → Iconize 下可配置：

### 图标显示（Icon Display）

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Icon placement** | `before file name` | 图标位置：文件名前/后/替换 | `before file name` |
| **Show icon in title** | ✅ 开启 | 在笔记编辑器标题前显示图标 | ✅ 开启 |
| **Show icon in tabs** | ❌ 关闭 | 在标签页上显示图标 | ✅ 开启（方便区分标签） |
| **Icon size** | `16` | 图标大小（像素） | `16`（默认） |

### 图标包管理（Icon Packs）

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Font Awesome** | 1500+ 免费图标 | ✅ 开启 |
| **Lucide Icons** | 简洁线条风格 | ✅ 开启 |
| **Material Icons** | Google 设计风格 | ✅ 开启 |
| **Tabler Icons** | 3000+ 开源图标 | ⚠️ 按需（较多影响性能） |
| **Custom SVG folder** | 自定义 SVG 图标存放路径 | `attachments/icons/` |

### 自定义规则（Custom Rules）

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Rules** | 添加自动匹配规则：路径/标签/文件名/扩展名 | 见下表示例 |
| **Rule priority** | 多条规则冲突时优先级顺序 | 上方的规则优先 |

**推荐规则配置：**

```yaml
- 规则: 按文件夹
  匹配: 30.areas/*
  图标: 📂

- 规则: 按标签
  匹配: #daily
  图标: 📅

- 规则: 按扩展名
  匹配: *.pdf
  图标: 📄
  颜色: "#FF0000"

- 规则: 按文件名
  匹配: "*日记*"
  图标: 📖
```

### Frontmatter 集成

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Enable frontmatter** | 允许 Frontmatter 中的 `icon` 字段 | ✅ 开启 |
| **Enable icon color in frontmatter** | 允许 `icon-color` 字段定义颜色 | ✅ 开启 |
| **Override rules with frontmatter** | Frontmatter 优先级高于自动规则 | ✅ 开启 |

### 导出/导入（Backup）

| 设置项 | 说明 |
|--------|------|
| **Export configuration** | 将所有图标配置导出为 JSON |
| **Import configuration** | 从 JSON 导入图标配置 |

---

## 💡 最佳实践

1. **文件夹色彩系统**：为不同类别文件夹设置不同颜色（绿=学习，蓝=工作，黄=生活）
2. **快捷键**：为常用图标设置快捷键快速插入
3. **导出/导入配置**：在设置中导出图标配置，换设备时一键恢复
4. **图标搜索**：在图标选择器中直接搜索关键词快速定位
5. **轻量化提示**：图标过多可能影响启动速度，建议只对常用项目设置

---

## 🔗 资源

| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/FlorianWoelki/obsidian-iconize |
| 官方文档 | https://florianwoelki.github.io/obsidian-iconize/ |
| 问题反馈 | https://github.com/FlorianWoelki/obsidian-iconize/issues |

---

> 📝 本文档由 Claudian 检索官方文档后补充完整 · 最后更新 2026-07-28

