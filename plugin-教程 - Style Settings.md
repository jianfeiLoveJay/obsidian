---
created: 2026-07-28
plugin-id: obsidian-style-settings
plugin-name: Style Settings
plugin-author: obsidian-community
rank: "#8"
downloads: 2,529,630
tags: [plugin-tutorial, css, theme]
---

# Style Settings 使用教程

> **排名 #8 / 6,081** · 下载量 **2,529,630** · 作者：mgmeyers

---

## 📋 简介

Style Settings 是 Obsidian 的**CSS 可视化配置面板**。它允许主题和代码片段作者定义可调参数（颜色、字体、间距等），用户无需编辑 CSS 即可在统一的设置界面中调整 Obsidian 的外观。

## 🚀 快速上手

### 安装
在 Obsidian 设置 → 社区插件 → 浏览中搜索「Style Settings」即可安装。

### 使用
安装后重启，在设置面板中会出现「Style Settings」选项页。如果当前主题或代码片段定义了 CSS 变量，这里就会显示对应的设置开关、滑块、颜色选择器和下拉菜单。

## 🎯 CSS 配置语法

主题或代码片段作者在 CSS 文件中使用 /* @settings */ 注释块来定义可配置项：

`css
/* @settings

name: 我的主题配置
id: my-theme
settings:
    -
        id: accent-color
        title: 主题色
        type: variable-color
        format: hsl-split
        default: '#007AFF'
    -
        id: ui-font
        title: 界面字体
        type: variable-text
        default: -apple-system, sans-serif
    -
        id: sidebar-width
        title: 侧边栏宽度
        type: variable-number-slider
        default: 300
        min: 200
        max: 500
        step: 10
        format: px
*/
`

## 📋 支持的设置类型

| 类型 | 说明 | 控件 |
|------|------|------|
| heading | 标题，用于分组 | 折叠式标题 |
| info-text | 展示信息文本 | 纯文本（支持 Markdown） |
| class-toggle | 切换 CSS 类 | 开关 |
| class-select | 从多个类中选择 | 下拉菜单 |
| ariable-text | 文本类型 CSS 变量 | 输入框 |
| ariable-number | 数值类型 CSS 变量 | 输入框 |
| ariable-number-slider | 数值滑块 | 滑块 |
| ariable-select | 预定义选项选择 | 下拉菜单 |
| ariable-color | 颜色选择 | 颜色选择器 |

## 💡 使用技巧

### 查看主题支持

安装新主题后，在 Style Settings 面板中查看是否有可调选项。热门主题（如 Minimal、Blue Topaz、AnuPpuccin）均深度支持。

### 组合多个代码片段

可以将多个 CSS 代码片段分别定义 @settings，所有配置会合并展示。

### 自定义导出

配置好后，在 Style Settings 面板底部点击「Copy Settings」可以将所有配置导出，方便备份或分享。

## 🔗 资源

| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/mgmeyers/obsidian-style-settings |
| 问题反馈 | https://github.com/mgmeyers/obsidian-style-settings/issues |
| 默认主题 CSS 变量 | https://github.com/mgmeyers/obsidian-style-settings/blob/main/obsidian-default-theme.css |

---

> 📝 本文档由 Claudian 自动生成 · 最后更新 2026-07-28
