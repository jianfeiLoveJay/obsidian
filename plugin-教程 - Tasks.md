---
created: 2026-07-28
plugin-id: obsidian-tasks-plugin
plugin-name: Tasks
plugin-author: obsidian-tasks-group
rank: #4
downloads: 3,892,497
tags: [plugin-tutorial, tasks, gtd]
---

# Tasks 使用教程

> **排名 #4 / 6,081** · 下载量 **3,892,497** · 作者：obsidian-tasks-group

---

## 📋 简介

Tasks 是 Obsidian 最专业的**任务管理插件**。支持截止日期、重复任务、优先级、依赖关系、任务过滤和分组。

## 🚀 快速上手

### 创建任务

在笔记中直接输入（支持 Dataview 语法）：

`markdown
- [ ] 写周报 📅 2026-08-01 ⏫
- [x] 买咖啡 ✅ 2026-07-28
- [ ] 读书计划 🔁 每周一 ➕ 2026-07-01 📅 2026-08-07 ⏳ 2026-08-01
`

### 任务查询

``markdown
`	asks
not done
due before 2026-08-07
sort by priority
group by folder
`
``

## 🎯 核心语法

| 符号 | 含义 | 示例 |
|------|------|------|
| 📅 | 截止日期 | 📅 2026-08-01 |
| ⏳ | 计划开始 | ⏳ 2026-07-28 |
| 🔼 ⏫ 🔼 🔽 ⏬ | 优先级 | ⏫ 高优先 |
| 🔁 | 重复规则 | 🔁 每周一 |
| ✅ | 完成日期 | 自动添加 |
| ➕ | 创建日期 | ➕ 2026-07-28 |
| 🏷️ | 标签 | 🏷️ work |

### 重复任务示例

`markdown
- [ ] 周报 🔁 每周末 on Friday 📅 2026-08-01
- [ ] 健身 🔁 每天 when done
- [ ] 还款 🔁 每月 1 号
`

## 💡 最佳实践

1. **结合 Dataview**：Tasks 支持 Dataview 查询，自动汇总全库任务
2. **创建任务看板**：使用 Tasks 查询搭配 Kanban 插件
3. **快捷键**：建议设置 Ctrl+Shift+T 快速插入任务

## 🔗 资源
- GitHub: https://github.com/obsidian-tasks-group/obsidian-tasks
- 文档: https://publish.obsidian.md/tasks/
