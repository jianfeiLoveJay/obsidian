---
created: 2026-07-28
plugin-id: obsidian-git
plugin-name: Git
plugin-author: Vinzent
rank: "#7"
downloads: 2,919,858
tags: [plugin-tutorial, git, backup, version-control]
---

# Git 使用教程

> **排名 #7 / 6,081** · 下载量 **2,919,858** · 作者：Vinzent

---

## 📋 简介

Git 插件将 Git 版本控制无缝集成到 Obsidian，支持**自动备份**、**历史版本**、**时间线**、**差异对比**、**源码管理视图**等完整功能。

> ⚡ **适合场景**：多设备同步、版本回退、写作历史追踪、团队协作。

---

## 🚀 快速上手

### 初始化仓库

1. 安装插件后，打开设置 → Git
2. 推荐开启 **Auto Backup after file change**
3. 首次需要初始化：命令面板 → "Obsidian Git: Initialize a new repo"
4. 配置用户名和邮箱（如未全局配置）：
   ```
   git config --global user.email "you@example.com"
   git config --global user.name "Your Name"
   ```

> ⚠️ 你的 Git 报错正是缺少此配置，执行上面两条命令即可解决。

### 设置远程仓库（多设备同步）

```bash
git remote add origin https://github.com/你的用户名/你的仓库.git
```

之后可用插件命令 Push/Pull 同步。

---

## 🎯 核心功能

### 1️⃣ 源码管理视图（Source Control View）

命令面板 → "Open source control view"，在侧边栏打开类似 VS Code 的 Git 面板：
- 📋 查看所有变更文件（新增/修改/删除）
- ✅ Stage/Unstage 单个文件
- ✍️ 填写提交信息并 Commit
- 📤 一键 Push 到远程

![Source Control View](https://raw.githubusercontent.com/Vinzent03/obsidian-git/master/images/source-view.png)

### 2️⃣ 历史视图（History View）

命令面板 → "Open history view"，查看完整提交历史：
- 📜 按时间线浏览所有 Commit
- 👤 显示作者、日期、提交信息
- 📁 查看每次提交变更的文件列表
- 可开启/关闭作者和日期显示

![History View](https://raw.githubusercontent.com/Vinzent03/obsidian-git/master/images/history-view.png)

### 3️⃣ Diff 视图（Diff View）

命令面板 → "Open diff view"，对比文件变更：
- 左右分栏显示文件差异
- 新增行绿色高亮，删除行红色标记
- 支持从 Source Control View 直接打开

![Diff View](https://raw.githubusercontent.com/Vinzent03/obsidian-git/master/images/diff-view.png)

### 4️⃣ 编辑器标记（Signs）

在编辑器中直接显示行级别变更：
- 🟢 绿色竖线 → 新增行
- 🟡 黄色竖线 → 修改行
- 🔴 红色竖线 → 删除行
- 可在标记上点击直接 Stage/Reset

![Signs](https://raw.githubusercontent.com/Vinzent03/obsidian-git/master/images/signs.png)

### 5️⃣ 可用命令大全

**变更管理：**
- `List changed files` — 列表所有变更
- `Stage current file` / `Unstage current file`
- `Discard all changes` — 丢弃所有变更
- `Open diff view` — 对比当前文件

**提交：**
- `Commit` — 提交已暂存文件
- `Commit all changes` — 提交所有变更（不推送）
- `Commit-and-sync` — 一键提交 + 拉取 + 推送

**远程：**
- `Push` / `Pull` — 推送/拉取
- `Edit remotes` — 编辑远程仓库
- `Clone an existing remote repo` — 克隆远程仓库
- `Open file on GitHub` — 在浏览器打开 GitHub 文件

**分支：**
- `Create new branch` / `Delete branch`
- 切换分支需通过 Git 命令自行操作

---


### .gitignore 建议

```
.obsidian/workspace.json
.obsidian/cache/
.obsidian/plugins/*/data.json  # 如果不想同步插件配置
.trash/
```

---


## ⚙️ 设置选项详解

Obsidian 设置 → 社区插件 → Git 下有完整的版本控制配置：

### 自动备份（Auto Backup）

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Auto backup after file change** | ❌ 关闭 | 文件变更后自动 Commit | ✅ 开启 |
| **Commit interval (minutes)** | 0（不自动） | 定时自动提交间隔（分钟） | `5`（频繁保存用 `3`） |
| **Auto pull interval (minutes)** | 0（不自动） | 定时自动拉取远程更新间隔 | `30` 或 `60` |
| **Auto push interval (minutes)** | 0（不自动） | 定时自动推送间隔 | 同 Auto pull |

### 提交设置（Commit）

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Commit message** | 提交信息模板，`{{date}}` 表示日期 | `auto: {{date}}` |
| **Commit date format** | 提交信息中日期格式 | `YYYY-MM-DD HH:mm` |
| **Push on commit** | Commit 时是否自动 Push | ✅ 开启（配合自动备份） |
| **Pull on commit** | Commit 前先 Pull 拉取远程 | ✅ 开启（避免冲突） |

### 界面设置（Appearance）

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Signs in the editor** | ❌ 关闭 | 编辑器显示新增/修改/删除行标记 | ✅ 开启 |
| **Date format for views** | `YYYY-MM-DD` | 历史视图和 Diff 视图中的日期格式 | `YYYY-MM-DD HH:mm` |
| **Author in history** | ❌ 关闭 | 历史视图中显示提交作者 | ✅ 开启（多人协作时） |
| **Show status bar** | ✅ 开启 | 状态栏显示当前分支和未推送数 | ✅ 开启 |

### 源控制视图（Source Control）

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Show source control button** | 侧边栏显示源控制按钮 | ✅ 开启 |
| **Auto refresh source control** | 自动刷新变更列表 | ✅ 开启 |

### 高级设置（Advanced）

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Git submodules** | 支持子模块（桌面端） | ⚠️ 按需开启 |
| **Disable push** | 禁用推送功能（纯本地版本控制） | 不需要远程时开启 |
| **Update branches** | 自动更新分支列表 | ✅ 开启 |
| **Base path** | Git 仓库路径（默认为 Vault 根） | 保持默认 |

### 忽略文件建议

```gitignore
.obsidian/workspace.json
.obsidian/cache/
.trash/
*.excalidraw.md.bak
```

> 💡 插件设置中的 **Ignore files** 选项也可配置忽略规则，支持通配符。

---

## 📱 移动端支持（实验性）

移动端使用 **isomorphic-git**（JS 版 Git），存在以下限制：
- ❌ 不支持 SSH 认证
- ❌ 不支持子模块
- ⚠️ 仓库大小受限，大仓库可能崩溃
- ⚠️ 不支持 Rebase 合并策略

> 移动端替代方案：[GitSync](https://github.com/ViscousPot/GitSync)

---

## 🔗 资源

| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/vinzent03/obsidian-git |
| 完整文档 | https://publish.obsidian.md/git-doc |
| 认证指南 | https://publish.obsidian.md/git-doc/Authentication |
| Git 教程 | https://git-scm.com/book/zh/v2 |

---

> 📝 本文档由 Claudian 检索官方文档后补充完整 · 最后更新 2026-07-28

