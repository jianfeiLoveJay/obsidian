---
created: 2026-07-28
plugin-id: obsidian-git
plugin-name: Git
plugin-author: Vinzent
rank: #7
downloads: 2,919,858
tags: [plugin-tutorial, git, backup, version-control]
---

# Git 使用教程

> **排名 #7 / 6,081** · 下载量 **2,919,858** · 作者：Vinzent

---

## 📋 简介

Git 插件将 Git 版本控制无缝集成到 Obsidian，支持**自动备份**、**历史版本**、**时间线**、**差异对比**。（你已安装此插件！）

## 🚀 快速上手

### 初始化仓库
1. 安装插件后，设置 → Git → **Auto Backup after file change**（推荐开启）
2. 修改任意笔记，插件会自动 commit
3. 状态栏显示当前分支和未推送数量

### 核心命令

| 命令 | 说明 |
|------|------|
| Obsidian Git: Commit all changes | 提交所有更改 |
| Obsidian Git: Push | 推送到远程 |
| Obsidian Git: Pull | 拉取远程更新 |
| Obsidian Git: View diff | 查看文件差异 |
| Obsidian Git: Open source view | 查看 Git 历史 |
| Obsidian Git: Create backup | 手动创建备份 |

## 🎯 推荐设置

`
自动备份: ✅ 开启
提交间隔: 5 分钟
拉取间隔: 30 分钟
忽略文件: .obsidian/workspace.json, .obsidian/cache/
`

### 远程同步（多设备）

`ash
# 在 vault 目录初始化（如尚未初始化）
git init
git remote add origin https://github.com/你的用户名/你的仓库.git
`

> 💡 多设备同步推荐方案：Git + 远程仓库（GitHub/Gitee）

## ⚠️ 注意事项
- .obsidian/workspace.json 建议加入 .gitignore
- 大型附件请使用 Git LFS
- 自动提交前确保已设置 user.name 和 user.email

## 🔗 资源
- GitHub: https://github.com/vinzent03/obsidian-git
- Git 教程: https://git-scm.com/book/zh/v2
