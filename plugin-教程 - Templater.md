---
created: 2026-07-28
plugin-id: templater-obsidian
plugin-name: Templater
plugin-author: silentvoid13
rank: #2
downloads: 5,021,540
tags: [plugin-tutorial, template, automation]
---

# Templater 使用教程

> **排名 #2 / 6,081** · 下载量 **5,021,540** · 作者：[silentvoid13](https://github.com/silentvoid13)

---

## 📋 简介

Templater 是 Obsidian 最强大的模板引擎。相比核心插件「模板」，Templater 支持动态内容、JavaScript 脚本、文件创建触发器、系统信息变量等高级功能。

## 🚀 快速上手

### 1. 设置模板文件夹
- 进入设置 → Templater → **Template folder location**
- 指定你的模板文件夹（例如 	emplates/）

### 2. 创建一个简单模板
在模板文件夹新建一个文件，插入：

`markdown
---
created: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>

## 今日目标

- [ ]
`

### 3. 插入模板
- 使用命令 Templater: Insert template (Ctrl+P)
- 或设置快捷键

## 🎯 核心功能

| 功能 | 说明 |
|------|------|
| **动态变量** | 	p.date.now()、	p.file.title、	p.system.clipboard 等 |
| **JavaScript 脚本** | 在模板中嵌入 JS 实现任何逻辑 |
| **文件创建触发器** | 在特定文件夹创建文件时自动应用模板 |
| **系统命令** | 调用系统命令并捕获输出 |

## 📖 常用变量示例

| 变量 | 输出 |
|------|------|
| 	p.date.now("YYYY-MM-DD") | 2026-07-28 |
| 	p.date.weekday("YYYY-MM-DD", 0) | 下周一的日期 |
| 	p.file.title | 当前文件名 |
| 	p.file.creation_date() | 文件创建时间 |
| 	p.system.clipboard() | 剪贴板内容 |
| 	p.web.daily_quote() | 每日一言 |
| 	p.obsidian.time.now() | 当前时间 |

## 🔗 资源
- GitHub: https://github.com/silentvoid13/Templater
- 文档: https://silentvoid13.github.io/Templater/
