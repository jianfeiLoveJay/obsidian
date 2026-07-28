---
created: 2026-07-28
plugin-id: obsidian-tasks-plugin
plugin-name: Tasks
plugin-author: obsidian-tasks-group
rank: "#4"
downloads: 3,892,497
tags: [plugin-tutorial, tasks, gtd]
---

# Tasks 使用教程

> **排名 #4 / 6,081** · 下载量 **3,892,497** · 作者：obsidian-tasks-group

---

## 📋 简介

Tasks 是 Obsidian 最专业的**任务管理插件**。支持截止日期、重复任务、优先级、依赖关系、任务过滤、分组、排序等。与 Dataview 深度兼容，可全库汇总任务。

> 🎯 **核心定位**：拥有完整语法的任务引擎，比核心插件"待办"强大得多。

---

## 🚀 快速上手

### 创建任务

```markdown
- [ ] 写周报 📅 2026-08-01 ⏫
- [x] 买咖啡 ✅ 2026-07-28
- [ ] 读书计划 🔁 每周一 ➕ 2026-07-01 📅 2026-08-07 ⏳ 2026-08-01
```

---

## 🎯 核心语法（完整参考）

### 任务修饰符

| 符号 | 名称 | 说明 | 示例 |
|------|------|------|------|
| `📅 2026-08-01` | Due | 截止日期 | 到期提醒 |
| `⏳ 2026-07-28` | Scheduled | 计划开始日期 | 在此之前不可见 |
| `🔼` | Priority 中 | 中等优先级 | 默认级别 |
| `⏫` | Priority 高 | 最高优先级 | 最紧急 |
| `🔽` | Priority 低 | 低优先级 | 可延后 |
| `⏬` | Priority 最低 | 最低优先级 | 不紧急 |
| `🔁 每周一` | Repeat | 重复规则 | 自动生成下一个 |
| `✅ 2026-07-28` | Done | 完成日期 | 勾选后自动添加 |
| `➕ 2026-07-01` | Created | 创建日期 | 手动或自动添加 |
| `🏷️ work` | Tag | 自定义标签 | 用于过滤 |

### 重复任务语法

| 规则 | 说明 | 示例 |
|------|------|------|
| `🔁 每天` | 每日重复 | 完成后自动创建新任务 |
| `🔁 每周一` | 每周一 | 支持 `every Monday` |
| `🔁 每周末` | 周末 | `on Friday` 指定具体日 |
| `🔁 每月 1 号` | 每月1日 | 支持 `every month on the 1st` |
| `🔁 每年` | 每年 | `every year on Jan 1` |
| `🔁 every 7 days` | 每7天 | 支持英文规则 |
| `🔁 when done` | 完成后开始计时 | 从完成日开始计算 |
| `🔁 every week on Sunday` | 每周日 | 指定具体星期 |

### 优先级排序

| 符号 | 名称 | 排序权重 |
|------|------|---------|
| `⏫` | Highest | 1 |
| `🔺` | High | 2 |
| `🔼` | Medium | 3 |
| `🔽` | Low | 4 |
| `⏬` | Lowest | 5 |

---

## 📖 Tasks 查询块

使用 ```tasks 代码块来过滤和展示任务：

### 基本过滤

```tasks
not done
due before 2026-08-07
sort by priority
group by folder
```

### 全部过滤选项

| 过滤条件 | 说明 | 示例 |
|----------|------|------|
| `not done` | 未完成 | `done` 显示已完成 |
| `due (before/after/on) date` | 按截止日期 | `due after 2026-07-01` |
| `starts (before/after/on) date` | 按开始日期 | `starts before today` |
| `scheduled (before/after/on) date` | 按计划日期 | `scheduled on 2026-08-01` |
| `created (before/after/on) date` | 按创建日期 | `created after yesterday` |
| `done (before/after/on) date` | 按完成日期 | `done on 2026-07-28` |
| `priority is (above/below)` | 按优先级 | `priority is above medium` |
| `description includes` | 描述包含 | `description includes "周报"` |
| `heading includes` | 所属标题包含 | `heading includes "工作"` |
| `tags include` | 标签包含 | `tags include #work` |
| `has due date` | 有截止日期 | 过滤设置了日期的任务 |

### 排序与分组

```tasks
not done
sort by priority
sort by due
group by folder
group by heading
```

| 指令 | 说明 |
|------|------|
| `sort by status` / `priority` / `due` / `created` | 排序方式 |
| `sort by done` / `description` / `path` / `heading` | 更多排序 |
| `group by folder` / `file` / `heading` | 按文件夹/文件/标题分组 |
| `group by priority` / `due` / `tags` | 按属性分组 |

---

## 💡 最佳实践

### 每日任务仪表盘

```tasks
not done
due on today
sort by priority
```

### 周报任务汇总

```tasks
not done
due after 2026-07-21
due before 2026-07-28
group by folder
```

### 与 Dataview 配合

Tasks 的元数据在 Dataview 中自动索引，可用 DQL 查询：

```dataview
TASK
WHERE !completed AND contains(tags, "#work")
SORT due ASC
```

### 建议快捷键

| 快捷键 | 操作 |
|--------|------|
| `Ctrl+Shift+T` | 插入任务模板 |
| 使用 Templater 创建任务模板 | 自动添加创建日期 |

---


## ⚙️ 设置选项详解

在 Obsidian 设置 → 社区插件 → Tasks → 可配置丰富的选项：

### 任务过滤（Global Task Filter）

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Global task filter** | 空（不启用） | 设置后只有包含此标签的待办项才被识别为"任务"。如设为 #task，则只识别 - [ ] 任务 #task | #task（避免与其他插件冲突） |
| **Global query** | 空 | 当 	asks 代码块为空时的默认查询 | 
ot done |
| **Remove empty tasks** | ❌ 关闭 | 删除空白任务条目（仅有 - [ ] 的行） | ❌ 关闭 |

### 完成日期设置（Completion Date）

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Set completion date on done** | ✅ 开启 | 勾选任务时自动在行尾添加 ✅ 完成日期 | ✅ 开启 |
| **Completion date format** | YYYY-MM-DD | 完成日期的格式 | YYYY-MM-DD |
| **Recurrence on next line** | ❌ 关闭 | 重复任务的 🔁 符号放在任务文本的下一行（使一行更整洁） | ❌ 关闭（保持一行完整） |
| **Confirm before delete** | ✅ 开启 | 删除任务前弹出确认对话框 | ✅ 开启 |

### 任务状态（Task Status）

Tasks 支持完全自定义任务状态类型。在设置 → Custom task status 中可添加/编辑：

| 状态名称 | 符号 | 类型 | 下一个状态 | 说明 |
|---------|------|------|-----------|------|
| **Todo** | 空格 | TODO | In Progress | 未开始，默认初始状态 |
| **In Progress** | / | IN_PROGRESS | Done | 进行中 |
| **Done** | x | DONE | — | 已完成（终态） |
| **Cancelled** | - | CANCELLED | — | 已取消（终态） |

> 你还可以自定义更多状态，如 Delay（⏰）、Waiting（👀）等。每个状态可指定符号、类型和点击后跳转的下一个状态。

### 日期设置（Dates）

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Default due time** | 截止日期的默认时间，如 17:00 | 保持空（仅日期） |
| **Default scheduled time** | 计划日期的默认时间 | 保持空 |
| **Use emoji in task description** | 在任务描述中使用 Emoji 符号表示状态 | ✅ 开启 |

### 功能开关（Features）

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Recurrence** | ✅ 开启 | 启用 🔁 重复任务功能 | ✅ 开启 |
| **Priority** | ✅ 开启 | 启用优先级符号（⏫ 🔺 🔼 🔽 ⏬） | ✅ 开启 |
| **Scheduled dates** | ✅ 开启 | 启用 ⏳ 计划日期功能 | ✅ 开启 |
| **Start dates** | ✅ 开启 | 启用开始日期功能（使用 🛫 符号） | ✅ 开启 |
| **Creation dates** | ✅ 开启 | 启用 ➕ 创建日期功能 | ✅ 开启 |
| **Depends on** | ❌ 关闭 | 启用任务依赖（⛔ 依赖其他任务完成后才显示） | ⚠️ 高级功能按需开启 |
| **ID** | ❌ 关闭 | 为任务分配唯一 ID，用于依赖引用 | 配合 Depends on 开启 |

### 搜索与显示（Search & Display）

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Short mode** | 在 	asks 查询块中只显示任务文本，不显示元数据列 | 按需（配合 Dataview 时常用） |
| **Hide task count** | 隐藏查询结果底部的任务计数「N tasks」 | ❌ 关闭 |
| **Support dataview** | 允许 Dataview 查询 Tasks 的元数据 | ✅ 开启（自动） |

## 🔗 资源

| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/obsidian-tasks-group/obsidian-tasks |
| 官方文档 | https://publish.obsidian.md/tasks/ |
| 问题反馈 | https://github.com/obsidian-tasks-group/obsidian-tasks/issues |

---

> 📝 本文档由 Claudian 检索官方文档后补充完整 · 最后更新 2026-07-28

