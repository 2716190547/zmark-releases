# ZMark

<img src="assets/icon.iconset/icon_256x256.png" alt="ZMark 图标" width="128">

[English](README.md)

ZMark 是一款面向本地文件的桌面 Markdown 编辑器与阅读器。可以编辑源码、阅读排版预览，或在分屏中同时使用两者；通过侧栏整理文件夹，文档保存在你选择的位置。

## 下载与安装

从 [GitHub Releases](https://github.com/2716190547/zmark-releases/releases) 或 [Gitee 发行镜像](https://gitee.com/zeng_sc/zmark-releases/releases) 下载当前发布版本。目前提供 macOS ZIP 和 Windows 安装程序：解压 ZIP 后将 `ZMark.app` 移到“应用程序”，或运行 Windows 安装程序。不同平台的实际行为可能存在差异。

项目已配置 Linux 构建流程，但当前公开发行版尚未提供 Linux 安装包。

## 快速上手

1. 在 macOS 上按 **Cmd+O**，在 Windows 或 Linux 上按 **Ctrl+O** 打开 Markdown 文件；也可以直接编辑欢迎草稿。
2. 在工具栏选择**源码**、**分屏**或**预览**。分屏时两个窗格支持同步滚动。
3. 按 **Cmd+B** 或 **Ctrl+B** 打开侧栏。添加文件夹后可以浏览 Markdown 文件、按文件或文件夹名称搜索，并通过文档大纲跳转到标题。
4. 按 **Cmd+S** 或 **Ctrl+S** 保存。首次保存草稿时选择位置；双击文档标题可以重命名。
5. 按 **Cmd+,** 或 **Ctrl+,** 打开设置，调整外观、编辑、保存与语言。

## 使用文档

### 文件和文件夹

侧栏分组显示工作区文件夹、工作区之外打开的文件和草稿。可以添加多个工作区文件夹，也可以在其中新建 Markdown 文件。从侧栏移除工作区文件夹不会删除磁盘上的文件。搜索框筛选的是**名称**，不搜索文档正文；大纲显示当前文档中的标题。

已有文件可以在编辑后或窗口失焦时自动保存，两项行为都可以在设置中调整。新草稿需要先选择保存位置才会成为文件；关闭时会提示处理未保存的修改。

### Markdown 与图表

预览支持标题、段落、强调、链接、列表、任务列表标记、表格、引用、代码块、本地图片和 Mermaid 图表。围栏代码块可显示语法高亮和复制按钮。在源码中修改任务标记后，预览会随之更新。

图片使用本地路径：可以相对于已保存的 Markdown 文件，也可以使用绝对路径。预览不加载网络图片 URL。点击图片或使用图表的放大按钮，可以查看大图。

可以在分屏中试试：

````markdown
# 项目笔记

- [ ] 检查初稿
- [x] 创建文档

| 项目 | 状态 |
| --- | --- |
| 预览 | 已就绪 |

```mermaid
flowchart LR
    Write --> Preview --> Share
```
````

Mermaid 语法支持范围取决于渲染器；如果图表无法显示，可以先检查语法并简化示例。

### 导出 HTML

点击工具栏的**导出 HTML**，或按 **Cmd+Shift+E** / **Ctrl+Shift+E**，然后选择保存位置。导出的 HTML 内含样式，但图片仍以路径引用、不会嵌入文件；Mermaid 块会作为代码导出，不会自动变成图表。分享文件时请确保引用的图片仍然可访问。

### 外观与编辑

设置中可以调整浅色、深色及跟随系统外观，选择调色板和语言，开启减少动态效果，以及调整行号、缩进、行高和自动保存。**关于**页面显示版本与更新状态。

## 快捷键

| 操作 | macOS | Windows / Linux |
| --- | --- | --- |
| 打开文件 | Cmd+O | Ctrl+O |
| 保存 | Cmd+S | Ctrl+S |
| 源码 / 分屏 / 预览 | Cmd+1 / 2 / 3 | Ctrl+1 / 2 / 3 |
| 展开或收起侧栏 | Cmd+B | Ctrl+B |
| 设置 | Cmd+, | Ctrl+, |
| 导出 HTML | Cmd+Shift+E | Ctrl+Shift+E |

## 技术栈

ZMark 使用 **Rust** 和 **GPUI** 构建桌面应用，使用 **pulldown-cmark** 解析 Markdown、**syntect** 实现代码高亮，并用 **rusty-mermaid** 渲染图表。本地图片由 Rust 的 `image` 库解码。
