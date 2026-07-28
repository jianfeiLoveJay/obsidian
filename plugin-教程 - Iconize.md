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

## 📋 简介

Iconize（原 Icon Folder）让你在 Obsidian 中**任何地方添加图标**。可以为文件、文件夹、笔记标题、标签页设置自定义图标，内置大量图标包，让你的 Vault 更直观、更个性化。

## 🚀 快速上手

### 安装
在 Obsidian 设置 → 社区插件 → 浏览中搜索「Iconize」即可安装。

### 给文件/文件夹添加图标
在文件资源管理器中右键单击文件或文件夹 → 「选择图标」→ 从图标库中选择。

### 给笔记标题添加图标
在笔记编辑界面右键单击标题区域 →「选择标题图标」。

## 🎯 核心功能

### 1. 图标包
内置多种免费图标包：
- **Font Awesome**（免费版）
- **Lucide**（原 Feather Icons）
- **Material Icons**
- **Tabler Icons**
- **自定义 SVG**：导入自己的 .svg 文件

### 2. 文件/文件夹图标
- 为单个文件或文件夹设置独立图标
- 图标会显示在文件资源管理器中
- 支持按文件扩展名自动匹配图标（如 .pdf 自动显示 PDF 图标）

### 3. 标题图标
在笔记编辑界面顶部标题前显示图标，让笔记更易识别。

### 4. 标签页图标
在打开的标签页上显示图标，配合图标区分不同的工作区。

### 5. 自定义规则
设置自动化规则，根据条件自动分配图标：

| 规则类型 | 示例 |
|---------|------|
| 按路径 | 文件夹/项目/* → 使用 project 图标 |
| 按标签 | #daily → 使用 calendar 图标 |
| 按文件名 | *日记* → 使用 book 图标 |
| 按扩展名 | *.pdf → 使用 pdf 图标 |

### 6. Frontmatter 集成
在笔记 YAML 前置元数据中指定图标：

`yaml
---
icon: 📝
icon-color: "#FF5733"
---
`

图标会显示在文件资源管理器和标题区域，颜色也可自定义。

### 7. 更改图标颜色
右键图标 →「选择颜色」→ 支持十六进制颜色码。

## 💡 最佳实践

1. **文件夹分类用颜色**：为不同类别的文件夹设置不同颜色的图标（如 🟢 学习、🔵 工作、🟡 生活）
2. **快捷键**：设置常用图标的快捷键快速插入
3. **导出/导入配置**：在设置中导出图标配置，换设备时一键恢复
4. **图标搜索**：在图标选择器中直接搜索关键词快速定位
5. **轻量化提示**：图标数量过多可能影响启动速度，建议只对常用项目设置

## 🔗 资源

| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/FlorianWoelki/obsidian-iconize |
| 官方文档 | https://florianwoelki.github.io/obsidian-iconize/ |
| 问题反馈 | https://github.com/FlorianWoelki/obsidian-iconize/issues |

---

> 📝 本文档由 Claudian 自动生成 · 最后更新 2026-07-28
