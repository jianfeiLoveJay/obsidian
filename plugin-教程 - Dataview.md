---
created: 2026-07-28
plugin-id: dataview
plugin-name: Dataview
plugin-author: blacksmithgu
rank: "#3"
downloads: 4,645,611
tags: [plugin-tutorial, query, database]
---

# Dataview 使用教程

> **排名 #3 / 6,081** · 下载量 **4,645,611** · 作者：blacksmithgu

---

## 📋 简介

Dataview 将 Obsidian 变成**个人数据库**。通过查询语言在笔记中检索、过滤、排序和展示结构化数据。它索引 YAML frontmatter、标签、内联字段、任务等元数据，让你可以用 SQL 风格的查询来操作知识库。

> 🎯 **核心理念**：Dataview 只读取和显示数据，不会修改你的笔记（任务勾选除外）。

---

## 📦 数据类型与元数据

### 添加元数据的三种方式

```yaml
---
# 1️⃣ YAML Frontmatter（推荐）
author: "Edgar Allan Poe"
published: 1845
tags: poems
rating: 9.5
---
```

```markdown
# 2️⃣ 内联字段（正文中）
从 [author:: Edgar Allan Poe] 的作品
(published:: 1845) 年出版

# 3️⃣ 隐式字段（自动索引）
- 文件属性：file.name, file.ctime, file.size, file.tags, file.inlinks, file.outlinks
- 任务：completed, due, created, priority
- 列表：完不成的任务会包含 [list:: item] 元数据
```

### 隐式字段一览

| 字段 | 类型 | 说明 |
|------|------|------|
| `file.name` | 字符串 | 文件名（不含扩展名） |
| `file.path` | 字符串 | 完整路径 |
| `file.folder` | 字符串 | 所在文件夹 |
| `file.tags` | 数组 | 所有标签 |
| `file.etags` | 数组 | 显式标签（不含继承） |
| `file.inlinks` | 数组 | 入链 |
| `file.outlinks` | 数组 | 出链 |
| `file.ctime` | 日期 | 创建时间 |
| `file.mtime` | 日期 | 修改时间 |
| `file.size` | 数字 | 文件大小（字节） |
| `file.starred` | 布尔 | 是否收藏 |
| `file.lists` | 数组 | 所有列表项 |
| `file.tasks` | 数组 | 所有任务 |

---

## 🚀 DQL（Dataview Query Language）

### 查询结构

```dataview
QUERY_TYPE
FROM source
WHERE condition
SORT field [ASC|DESC]
GROUP BY field
LIMIT number
FLATTEN field
```

### 基本类型

```dataview
LIST
FROM "笔记"
```

```dataview
TABLE author, published, rating
FROM #books
SORT rating DESC
```

```dataview
TASK
WHERE !completed AND contains(tags, "#urgent")
GROUP BY file.link
```

```dataview
CALENDAR file.ctime
```

### FROM 数据源

| 语法 | 说明 | 示例 |
|------|------|------|
| `FROM "folder"` | 指定文件夹 | `FROM "30.areas"` |
| `FROM #tag` | 指定标签 | `FROM #book/reading` |
| `FROM "folder" OR #tag` | 多条件 | `FROM #project OR "Work"` |
| `FROM -"exclude"` | 排除 | `FROM -"Template"` |

### WHERE 过滤

支持完整表达式和函数：

```dataview
TABLE file.mtime AS "修改时间"
WHERE file.mtime > date(today) - dur(7 days)
SORT file.mtime DESC
```

```dataview
LIST
WHERE contains(file.folder, "projects") AND rating >= 8
```

### SORT 排序

```dataview
TABLE rating
SORT rating DESC, file.name ASC
```

### GROUP BY 分组

```dataview
TABLE rows.file.link AS "笔记", rows.rating AS "评分"
GROUP BY type
```

### FLATTEN 展开

```dataview
TABLE file.link
FLATTEN file.tags AS tag
WHERE contains(tag, "#book")
```

### LIMIT 限制

```dataview
LIST
LIMIT 10
```

---

## 📖 函数参考

### 日期函数
| 函数 | 说明 |
|------|------|
| `date(string)` | 将字符串解析为日期 |
| `date(now)` | 当前日期时间 |
| `date(today)` | 今天日期 |
| `dur(string)` | 解析持续时间，如 `dur(3 days)` |
| `startswith(date1, date2)` | 日期比较 |

### 字符串函数
| 函数 | 说明 |
|------|------|
| `contains(string, value)` | 是否包含 |
| `length(string)` | 字符串长度 |
| `replace(string, from, to)` | 替换 |
| `regexmatch(pattern, string)` | 正则匹配 |
| `substring(string, start, end)` | 截取子串 |
| `lowercase(string)` / `uppercase(string)` | 大小写转换 |
| `split(string, delimiter)` | 分割字符串 |

### 数组/对象函数
| 函数 | 说明 |
|------|------|
| `length(array)` | 数组长度 |
| `nonnull(array)` | 去除非空 |
| `join(array, separator)` | 拼接 |
| `filter(array, predicate)` | 过滤 |
| `contains(array, value)` | 包含 |
| `extract(object, key)` | 提取字段 |

### 数值函数
| 函数 | 说明 |
|------|------|
| `round(number)` | 四舍五入 |
| `min(a, b)` / `max(a, b)` | 最小/最大值 |
| `sum(array)` / `avg(array)` | 求和/平均 |
| `default(field, value)` | 空值默认 |

---


## ⚙️ 设置选项详解

在 Obsidian 设置 → 社区插件 → Dataview → 可配置以下选项：

### 通用设置

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Enable Dataview** | ✅ 开启 | 总开关，关闭后所有查询不生效 | ✅ 开启 |
| **Enable JavaScript Queries** | ❌ 关闭 | 允许 `dataviewjs` 代码块执行 JS | ⚠️ 按需开启（有安全风险） |
| **Enable Inline Queries** | ✅ 开启 | 允许 `= field` 内联语法 | ✅ 开启 |
| **Enable Inline JavaScript** | ❌ 关闭 | 允许内联 JS 执行 | ❌ 关闭（除非需要） |
| **Warn on empty query** | ❌ 关闭 | 查询无结果时在预览中显示警告 | ✅ 开启（调试用） |

### 性能设置

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Maximum recursion depth** | 递归查询最大深度，默认 6 | 默认即可 |
| **Recursive query performance warning** | 递归查询超过一定层级时警告 | ✅ 开启 |
| **Auto refresh interval** | 自动刷新间隔（秒），默认 60 | 默认即可 |

### 表格设置

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Display result count** | 表格首行显示结果数量 `File (N)` | 按个人偏好 |
| **Primary column name** | 表格首列表头文字，默认 `File` | `文件` 或 `笔记` |
| **Group column name** | 分组表格首列表头文字，默认 `Group` | `分组` |

### 任务设置

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Set completion date on task completion** | ❌ 关闭 | 在 Dataview 中勾选任务时自动添加 ✅ 完成日期 | ✅ 开启 |
| **Completion date format** | `YYYY-MM-DD` | 完成日期的格式 | `YYYY-MM-DD` |
| **Emoji status** | ❌ 关闭 | 使用 ✅ ❌ 替代常规复选框样式 | 按个人偏好 |

### 内联字段前缀

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Inline field prefix** | 内联字段的默认前缀，默认空 | 保持默认 |
| **Inline field regex** | 自定义内联字段的正则匹配模式 | 高级用户调整 |

---

## 💡 DataviewJS

当 DQL 不够用时，可以使用 DataviewJS：

````markdown
```dataviewjs
// 获取当前页面所有标签
let pages = dv.pages("#book")
  .where(p => p.rating > 7)
  .sort(p => p.rating, 'desc')
  .limit(5)

dv.table(["书名", "评分", "作者"], 
  pages.map(p => [p.file.link, p.rating, p.author])
)
```
````

---

## 💡 内联查询

在正文中直接引用单个值：

```markdown
今天是 `= date(today)`。

这本 `= this.title` 评分为 `= this.rating`。

未完成任务：`= length(filter(file.tasks, (t) => !t.completed))`
```

---


## 🔗 资源

| 资源 | 链接 |
|------|------|
| 官方文档 | https://blacksmithgu.github.io/obsidian-dataview/ |
| GitHub 仓库 | https://github.com/blacksmithgu/obsidian-dataview |
| 社区示例 | https://blacksmithgu.github.io/obsidian-dataview/resources/examples/ |
| FAQ | https://blacksmithgu.github.io/obsidian-dataview/resources/faq/ |

---

> 📝 本文档由 Claudian 检索官方文档后补充完整 · 最后更新 2026-07-28

