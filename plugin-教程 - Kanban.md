---
created: 2026-07-28
plugin-id: obsidian-kanban
plugin-name: Kanban
plugin-author: mgmeyers
rank: "#9"
downloads: 2,470,342
tags: [plugin-tutorial, kanban, project-management]
---

# Kanban 使用教程

> **排名 #9 / 6,081** · 下载量 **2,470,342** · 作者：mgmeyers

---

## 📋 简介

Kanban 插件将**看板方法论**带入 Obsidian。每个看板文件对应一个看板，包含多个列表（列），每个列表包含多个卡片。数据以纯 Markdown 存储，支持日期、标签、复选框、归档、链接等功能。

---

## 🚀 快速上手

### 创建看板

命令面板（`Ctrl+P`）→ "Kanban: 新建看板" 或在文件列表中右键 → 新建 Kanban 看板。

### 基本操作

| 操作 | 方式 |
|------|------|
| 添加列 | 点击看板右侧的「+」按钮 |
| 添加卡片 | 点击列底部的「+」按钮或双击列空白区 |
| 拖拽移动 | 直接拖拽卡片到其他列 |
| 编辑卡片 | 点击卡片标题进入编辑模式 |
| 删除卡片 | 编辑模式下点击「删除」按钮 |
| 折叠列 | 点击列标题左侧的箭头 |

---

## 🎯 核心功能

### 1️⃣ 卡片元数据

编辑卡片时可以添加：

| 元数据 | 说明 | 用法 |
|--------|------|------|
| 📅 日期 | 截止日期 | 设置到期提醒 |
| 🏷️ 标签 | 颜色分类标签 | 按类别筛选卡片 |
| ☑️ 复选框 | 子任务清单 | 在卡片中添加检查列表 |
| 📝 备注 | 展开详情 | 添加更多描述信息 |
| 🔗 链接 | 笔记/外部链接 | `[[笔记名]]` 或 `https://...` |

### 2️⃣ 列的设置

点击列标题右侧的「···」菜单：
- **归档列中的卡片** — 已完成卡片归档到隐藏的归档列
- **清除已归档卡片** — 永久删除归档卡片
- **重命名列**
- **删除列**

### 3️⃣ 看板全局设置

在看板右上角的「···」菜单中：
- **紧凑模式** — 减小卡片间距
- **日期显示** — 开启/关闭卡片日期
- **卡片计数** — 显示各列卡片数量
- **堆叠卡片** — 限制卡片最大宽度
- **隐藏存档列** — 在底部隐藏已归档卡片

### 4️⃣ Markdown 存储格式

看板数据直接存储在 Markdown 文件中，可以用文本编辑器查看和修改：

```markdown
---
kanban-plugin: basic
---

## 📋 待办

- [ ] 写周报 📅 2026-08-01 🏷️ work
- [ ] 买礼物 🏷️ personal

## 🔄 进行中

- [ ] 项目 A 🔗 [[项目A]]
- [ ] 读《思考快与慢》 🏷️ reading

## ✅ 已完成

- [x] 完成日报 ✅

```

这也意味着你可以在 Markdown 视图下批量编辑卡片。

### 5️⃣ 链接与引用

- 在卡片中使用 `[[笔记名]]` 链接到其他笔记
- 在其他笔记中使用 `![[看板文件.md]]` 嵌入看板视图
- 移动/重命名链接笔记时，看板中的链接会自动更新

---

## 💡 最佳实践

### GTD 工作流看板

```
📋 待办 → 🔄 进行中 → 🔍 验证中 → ✅ 已完成
```

### 内容管理看板

```
📝 草稿 → ✏️ 编辑中 → 📋 审校 → 🚀 已发布
```

### 项目管理看板

```
🎯 待启动 → 🚧 开发中 → 🧪 测试中 → ✅ 已完成 → 📦 已交付
```

### 配合 Dataview

使用 Dataview 查询看板卡片元数据，生成全局任务仪表盘：

```dataview
TABLE tags, due
FROM "看板"
WHERE contains(file.name, "Kanban")
```

### 模板

创建看板模板文件，包含预设的列结构和示例卡片：

```markdown
---
kanban-plugin: basic
---

## 📋 待办

## 🔄 进行中

## ✅ 已完成

```

---


## ⚙️ 设置选项详解

在 Obsidian 设置 → 社区插件 → Kanban 下，以及看板文件内部均可配置。

### 全局设置（Obsidian 设置面板）

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Date format** | YYYY-MM-DD | 卡片日期的显示格式 | 保持默认 |
| **Date display style** | bsolute | 日期显示方式：bsolute（绝对日期）或 elative（相对日期，如"2天后"） | bsolute |
| **Time format** | h:mm a | 时间显示格式（12小时制） | 保持默认 |
| **Archive with date** | ✅ 开启 | 归档卡片时自动添加归档日期 | ✅ 开启 |
| **Archive date format** | YYYY-MM-DD | 归档日期的格式 | 保持默认 |
| **Maximum archived cards** | -1（无限制） | 最大归档卡片数量，超过后自动删除最旧卡片 | -1 |
| **Linked page metadata** | ❌ 关闭 | 在卡片中显示 [[链接笔记]] 的 Frontmatter 元数据（如 aliases、tags） | ⚠️ 按需开启 |
| **Prepare responsive columns** | ✅ 开启 | 根据屏幕宽度自动调整列数为单列/双列 | ✅ 开启 |
| **Horizontal scroll** | ❌ 关闭 | 启用水平滚动替代列换行 | 看板列数多时开启 |

### 看板级设置（在看板右上角 ··· 菜单中）

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Compact mode** | 紧凑模式，减小卡片间距和内边距 | 卡片数量多时 ✅ 开启 |
| **Show clock** | 在卡片日期旁显示具体时间 | 按个人偏好 |
| **Show relative date** | 显示相对日期（"今天""明天""2天后"）替代绝对日期 | ✅ 开启 |
| **Card count** | 在列标题旁显示该列卡片数量 | ✅ 开启 |
| **Stacked cards** | 限制卡片最大宽度，使列变窄 | 三列及以上看板 ✅ 开启 |
| **Hide archive column** | 在底部隐藏归档列，归档内容仅通过菜单访问 | ✅ 开启 |
| **Max card count** | 每列最大卡片数，超出时前端警告（不阻止添加） | 按需设置（如 20） |

### 看板 Frontmatter 设置

看板 Markdown 文件头部的 YAML 可配置以下字段：

`yaml
---
kanban-plugin: basic
kanban-archived-cards: 0
kanban-board-width: 1200
kanban-list-width: 300
kanban-hide-tags: false
kanban-hide-dates: false
---
`

| 字段 | 说明 |
|------|------|
| kanban-plugin | 看板类型：asic（基础）或 oard（完整） |
| kanban-archived-cards | 已归档卡片数量统计 |
| kanban-board-width | 整个看板最大宽度（px） |
| kanban-list-width | 每列宽度（px） |
| kanban-hide-tags | 是否隐藏卡片标签显示 |
| kanban-hide-dates | 是否隐藏卡片日期显示 |

## 🔗 资源

| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/mgmeyers/obsidian-kanban |
| 官方文档 | https://publish.obsidian.md/kanban/ |
| 问题反馈 | https://github.com/mgmeyers/obsidian-kanban/issues |

---

> 📝 本文档由 Claudian 检索官方文档后补充完整 · 最后更新 2026-07-28

