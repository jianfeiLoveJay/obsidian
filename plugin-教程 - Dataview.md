---
created: 2026-07-28
plugin-id: dataview
plugin-name: Dataview
plugin-author: blacksmithgu
rank: #3
downloads: 4,645,611
tags: [plugin-tutorial, query, database]
---

# Dataview 使用教程

> **排名 #3 / 6,081** · 下载量 **4,645,611** · 作者：blacksmithgu

---

## 📋 简介

Dataview 将 Obsidian 变成**个人数据库**。通过查询语言在笔记中检索、过滤、排序和展示结构化数据（YAML frontmatter、标签、任务等）。

## 🚀 快速上手

### 基础语法

在代码块中使用 dataview 查询语言：

``markdown
`dataview
TABLE created, tags
FROM "notes"
SORT created DESC
`
``

### 四大查询类型

| 类型 | 关键字 | 用途 |
|------|--------|------|
| **列表** | LIST | 列出符合条件的文件 |
| **表格** | TABLE | 展示字段数据表格 |
| **任务** | TASK | 汇总全库任务 |
| **日历** | CALENDAR | 按日期展示 |

## 🎯 常用查询示例

### 最近修改的笔记
``markdown
`dataview
TABLE file.mtime AS "修改时间"
SORT file.mtime DESC
LIMIT 10
`
``

### 按标签筛选
``markdown
`dataview
LIST
FROM #book/reading
`
``

### 任务看板
``markdown
`dataview
TASK
WHERE !completed AND contains(tags, "#project")
`
``

### 统计信息
``markdown
`dataview
TABLE length(file.outlinks) AS "出链数", length(file.inlinks) AS "入链数"
SORT length(file.outlinks) DESC
`
``

## 💡 进阶用法

- **DataviewJS**：使用 `` `dataviewjs `` 调用 JavaScript API
- **Metadata 字段**：通过 YAML frontmatter 定义结构化数据
- **内联字段**：在正文中用 [key:: value] 注入元数据

## 🔗 资源
- GitHub: https://github.com/blacksmithgu/obsidian-dataview
- 文档: https://blacksmithgu.github.io/obsidian-dataview/
