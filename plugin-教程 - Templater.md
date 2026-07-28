---
created: 2026-07-28
plugin-id: templater-obsidian
plugin-name: Templater
plugin-author: silentvoid13
rank: "#2"
downloads: 5,021,540
tags: [plugin-tutorial, template, automation]
---

# Templater 使用教程

> **排名 #2 / 6,081** · 下载量 **5,021,540** · 作者：silentvoid13

---

## 📋 简介

Templater 是 Obsidian 最强大的模板引擎。相比核心插件"模板"，支持动态内容、JavaScript 脚本、文件创建触发器、系统命令、丰富的内置函数模块等高级功能。

> 🎯 **核心定位**：用模板自动化 Obsidian 中一切重复操作。

---

## 🚀 快速上手

### 1. 设置模板文件夹
- 设置 → Templater → **Template folder location**
- 指定你的模板文件夹（如 `templates/`）

### 2. 创建一个简单模板
在模板文件夹中新建文件：

```markdown
---
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - daily
---

# <% tp.file.title %>

## 今日目标

- [ ] 

## 📝 笔记

<% tp.web.daily_quote() %>
```

### 3. 插入模板
- 命令面板 → "Templater: Insert template" (`Ctrl+P`)
- 或设置快捷键如 `Alt+T`

---

## 🎯 内置函数模块（完整参考）

### tp.date — 日期模块

```javascript
// 获取当前日期
<% tp.date.now("YYYY-MM-DD") %>
// 指定格式
<% tp.date.now("Do MMMM YYYY") %>
// 相对日期：7天后
<% tp.date.now("YYYY-MM-DD", 7) %>
// 相对日期：7天前
<% tp.date.now("YYYY-MM-DD", -7) %>
// 使用 ISO 偏移：1个月前
<% tp.date.now("YYYY-MM-DD", "P-1M") %>
// 1年后
<% tp.date.now("YYYY-MM-DD", "P1Y") %>
// 使用笔记标题作为参考日期
<% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>

// 明天 / 昨天
<% tp.date.tomorrow("YYYY-MM-DD") %>
<% tp.date.yesterday("YYYY-MM-DD") %>

// 本周一（0=周一，7=下周一）
<% tp.date.weekday("YYYY-MM-DD", 0) %>
<% tp.date.weekday("YYYY-MM-DD", 7) %>

// Moment.js 完整功能
<% moment(tp.file.title, "YYYY-MM-DD").startOf("month").format("YYYY-MM-DD") %>
<% moment(tp.file.title, "YYYY-MM-DD").endOf("month").format("YYYY-MM-DD") %>
```

**格式参考：** `YYYY`=年, `MM`=月, `DD`=日, `dddd`=星期, `Do`=序数日, `HH:mm`=时间

### tp.file — 文件模块

```javascript
// 文件标题
<% tp.file.title %>
// 文件内容
<% tp.file.content %>
// 创建日期 / 修改日期
<% tp.file.creation_date("YYYY-MM-DD") %>
<% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm") %>
// 文件路径
<% tp.file.path() %>          // 绝对路径
<% tp.file.path(true) %>       // 相对 vault 路径
// 所在文件夹
<% tp.file.folder() %>         // 只返回最后一级
<% tp.file.folder(true) %>     // 完整路径
// 文件标签
<% tp.file.tags %>
// 用户选中文本
<% tp.file.selection() %>
// 光标位置（多光标支持）
<% tp.file.cursor() %>
<% tp.file.cursor(1) %>内容<% tp.file.cursor(1) %>  // 多光标
// 光标后追加内容
<% tp.file.cursor_append("更多内容") %>

// 创建新文件
<%* await tp.file.create_new("内容", "新文件名", true) %>
// 使用模板创建
<%* await tp.file.create_new(tp.file.find_tfile("MyTemplate"), "新文件名", true) %>
// 在指定文件夹创建
<%* await tp.file.create_new("内容", "新文件名", false, "30.areas") %>
// 包含其他模板
<%* await tp.file.include("[[模板名称]]") %>
// 包含段落
<%* await tp.file.include("[[MyFile#Section1]]") %>

// 移动/重命名文件
<%* await tp.file.move("新路径/" + tp.file.title) %>
<%* await tp.file.rename("新名字") %>
// 检查文件是否存在
<% await tp.file.exists("Path/File.md") %>
```

### tp.frontmatter — 元数据模块

```javascript
// 读取 Frontmatter 字段
<% tp.frontmatter.author %>
// 或
<% tp.frontmatter["author"] %>
```

### tp.system — 系统模块

```javascript
// 剪贴板内容
<% tp.system.clipboard() %>
// 弹出输入框
<% tp.system.prompt("输入标题", "默认值") %>
// 确认对话框
<% tp.system.suggester(["选项1", "选项2"], ["val1", "val2"]) %>
// 执行系统命令
<%* tp.system.exec("echo Hello", "", false) %>
```

### tp.web — 网络模块

```javascript
// 每日一言
<% tp.web.daily_quote() %>
// 随机图片 URL
<% tp.web.random_picture() %>
// 带参数的随机图片
<% tp.web.random_picture("800x600", "landscape", "water") %>
```

### tp.obsidian — Obsidian API 模块

```javascript
// 访问 Obsidian API
<% tp.obsidian.Platform.isMobile %>
// 获取当前笔记文件对象
<% tp.config.target_file %>
```

### tp.config — 配置模块

```javascript
// 当前操作配置
<% tp.config.active_file %>    // 目标文件
<% tp.config.run_mode %>        // 运行模式
<% tp.config.template_file %>   // 模板文件对象
```

### tp.hooks — 钩子模块

```javascript
// 设置钩子
<% tp.hooks.on("create", () => { /* 逻辑 */ }) %>
```

---

## 🎯 用户函数

### 用户脚本（User Scripts）

在 `Templater/scripts/` 文件夹中创建 `.js` 文件：

```javascript
// scripts/我的脚本.js
function getGreeting() {
  const hour = new Date().getHours();
  if (hour < 12) return "早上好";
  if (hour < 18) return "下午好";
  return "晚上好";
}
module.exports = getGreeting;
```

在模板中使用：
```markdown
<% tp.user.我的脚本() %>
```

### 系统命令（System Commands）

```markdown
日期（系统格式）：<% tp.system.exec("date") %>
```

---

## 🎯 命令类型

### 动态命令（Dynamic Commands）

`<% %>` 语法 — 插入模板时执行，输出结果：

```markdown
今天：<% tp.date.now("YYYY-MM-DD") %>
```

### 执行命令（Execution Commands）

`<%* %>` 语法 — 执行但不输出结果，用于控制逻辑：

```markdown
<%* if (tp.file.title.startsWith("TODO")) { %>
  这是待办事项
<%* } %>
```

### 空白控制（Whitespace Control）

在 `%>` 前加 `-` 去除前面的空白，`<%` 后加 `-` 去除后面的空白：

```markdown
今天：<% tp.date.now("YYYY-MM-DD") -%>
后面没有换行
```

---

## 🎯 文件创建触发器

在 Templater 设置中配置，创建文件时**自动应用模板**：

| 触发条件 | 说明 |
|----------|------|
| 按文件夹 | 在指定文件夹中新建文件时自动应用模板 |
| 按文件名模式 | 文件名匹配正则时应用模板 |
| 空文件 | 新建空白文件时应用模板 |

设置路径：设置 → Templater → **Trigger Templater on new file creation**

---

## 💡 最佳实践

1. **每日笔记模板**：创建日期字段、每日目标、引用前一天笔记
2. **项目模板**：自动生成 Frontmatter、任务列表、关联标签
3. **周报模板**：自动汇总本周笔记、任务完成情况
4. **会议笔记模板**：参与者、议程、行动项
5. **书籍笔记模板**：元数据、引用、评论

### 完整模板示例

```markdown
---
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
modified: <% tp.file.last_modified_date("YYYY-MM-DD HH:mm") %>
type: daily
week: <% tp.date.now("WW") %>
tags:
  - daily
  - log
---

# <% tp.date.now("YYYY-MM-DD dddd") %>

<< [[<% tp.date.now("YYYY-MM-DD", -1) %>]] | [[<% tp.date.now("YYYY-MM-DD", 1) %>]] >>

## 🎯 今日目标
- [ ] 

## 📝 日志


## 📊 复盘
- 完成：:
- 收获：:
- 改进：:
```

---


## ⚙️ 设置选项详解

在 Obsidian 设置 → 社区插件 → Templater → 可配置以下完整选项：

### 模板位置（Template Location）

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Template folder location** | 空 | 模板文件存放的文件夹路径（支持多文件夹，用逗号分隔） | 	emplates/ 或 _templates/ |
| **Template file extension** | .md | 模板文件扩展名。设为 .templater 可避免与其他插件冲突 | .md（便于编辑和预览） |
| **Enable user scripts** | ❌ 关闭 | 启用 	p.user 脚本功能 | 需要自定义脚本时 ✅ 开启 |

### 自动触发（Automatic Template Triggering）

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Trigger Templater on new file creation** | ❌ 关闭 | 创建新文件时自动触发模板匹配 | ✅ 开启（配合下方规则使用） |
| **Folder templates** | 空 | 按文件夹自动应用模板。格式：文件夹路径: 模板文件名，每行一个 | 按需配置，如 daily/: templates/日常模板.md |
| **File name triggers** | 空 | 按文件名正则匹配自动应用模板。格式：正则表达式: 模板文件名 | 按需配置 |
| **Empty file template** | 空 | 创建空文件时自动应用的默认模板 | 	emplates/默认模板.md |

### 用户脚本（User Scripts）

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **User scripts folder** | Templater/scripts/ | 	p.user.* 函数查找用户脚本的文件夹 | Templater/scripts/ |
| **User script function name** | 空 | 用户脚本中导出的函数名，默认为文件名 | 保持默认（以文件名调用） |

### 系统命令（System Commands）

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Enable system commands** | ❌ 关闭 | 是否允许 	p.system.exec() 执行系统命令 | ❌ 关闭（存在安全风险，除非明确需要） |
| **Timeout (ms)** | 5000 | 系统命令执行超时时间（毫秒） | 保持默认 |

### 编辑器行为（Editor Behavior）

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Automatic jump to cursor** | ✅ 开启 | 插入模板后自动将光标跳转到 	p.file.cursor() 位置 | ✅ 开启 |
| **Trigger on file creation prompt** | ✅ 开启 | 创建文件时弹窗提示是否应用模板 | ⚠️ 按需（频繁创建时建议关闭） |
| **Quiet mode** | ❌ 关闭 | 禁用所有通知提示，静默执行模板 | ❌ 关闭（调试时临时开启） |
| **Copy file content as plain text** | ❌ 关闭 | 复制模板内容时不解析 Templater 命令 | ❌ 关闭 |

### 文件创建（File Creation）

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Enable folder creation** | ✅ 开启 | 允许 	p.file.create_new() 创建新文件夹 | ✅ 开启 |
| **File with same name** | overwrite | 同名文件处理方式：overwrite（覆盖）、ename（重命名新增）、skip（跳过） | ename（避免数据丢失） |

### 性能（Performance）

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Dynamic command timeout** | 5000 ms | <% %> 动态命令的超时时间 | 保持默认 |
| **Execution command timeout** | 5000 ms | <%* %> 执行命令的超时时间 | 保持默认 |

## 🔗 资源

| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/SilentVoid13/Templater |
| 官方文档 | https://silentvoid13.github.io/Templater/ |
| 安装指南 | https://silentvoid13.github.io/Templater/installation.html |
| FAQ | https://silentvoid13.github.io/Templater/faq.html |

---

> 📝 本文档由 Claudian 检索官方文档后补充完整 · 最后更新 2026-07-28

