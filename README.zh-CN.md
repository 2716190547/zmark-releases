# ZMark

<img src="assets/icon.iconset/icon_256x256.png" alt="ZMark 图标" width="128">

[English](README.md)

ZMark 是一款面向本地文件的桌面 Markdown 编辑器与阅读器，也支持常见代码与文本文件的源码编辑。可以编辑源码、阅读排版预览，或在分屏中同时使用两者；通过侧栏整理文件夹，文档保存在你选择的位置。

## 下载与安装

**当前版本：0.2.9** · [版本更新说明](https://github.com/2716190547/zmark-releases/releases/tag/v0.2.9)

从 [GitHub Releases](https://github.com/2716190547/zmark-releases/releases/tag/v0.2.9) 下载。[Gitee 发行镜像](https://gitee.com/zeng_sc/zmark-releases/releases) 可能稍后同步。

| 平台 | 安装包 | 安装方式 |
| --- | --- | --- |
| macOS（Apple Silicon） | ZIP / DMG | 将 `ZMark.app` 移到“应用程序”。 |
| Windows x86_64 | Setup EXE | 运行安装程序。 |
| Linux x86_64 | DEB / tar.gz | 安装 DEB，或解压 tar.gz 后运行 `usr/bin/zmark_app`。 |

macOS 应用使用 Ad-Hoc 签名，未做 Apple 公证；Windows 安装包未做发布者代码签名。不同平台的实际行为可能存在差异。

## 快速上手

1. 在 macOS 上按 **Cmd+O**，在 Windows 或 Linux 上按 **Ctrl+O** 打开 Markdown 或支持的文本文件；也可以直接编辑欢迎草稿。
2. 在工具栏选择**源码**、**分屏**或**预览**。分屏时两个窗格支持同步滚动。
3. 按 **Cmd+B** 或 **Ctrl+B** 打开侧栏。将文件或文件夹拖入窗口即可添加到侧栏，可按名称筛选文件，并通过 Markdown 文档大纲跳转到标题。
4. 按 **Cmd+S** 或 **Ctrl+S** 保存。首次保存草稿时选择位置；双击文档标题可以重命名。
5. 按 **Cmd+,** 或 **Ctrl+,** 打开设置，调整外观、编辑、保存与语言。

## 使用文档

### 文件和文件夹

侧栏分组显示工作区文件夹、工作区之外打开的文件和草稿。通过工具栏添加文件夹，或从桌面拖入文件和文件夹。支持 Markdown、纯文本、Rust、Python、JavaScript/TypeScript、C/C++、Java、Go、HTML/CSS、JSON、YAML、TOML、Shell 等常见文件；非 Markdown 文件使用源码模式，并按语言高亮。

单击文件夹行展开或收起，双击名称重命名。按住 **Shift** 连选，按住 macOS **Cmd** / Windows 和 Linux **Ctrl** 增减单个选择；多选后使用右上角批量按钮，按 **Esc** 退出。**移除**仅隐藏侧栏项目，不删除磁盘文件，撤销入口保留 5 秒；**删除**将项目移到系统废纸篓，可从右键菜单或批量工具栏操作。

侧栏搜索框筛选的是**名称**。搜索当前文档正文时，点击右上角搜索图标或按 **Cmd+F** / **Ctrl+F**；点击结果可跳转，使用 **Enter / Shift+Enter** 或 **F3 / Shift+F3** 切换下一个、上一个匹配项，查找输入框内也支持上下方向键。大纲显示 Markdown 文档的标题。

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
| 文档内查找 | Cmd+F | Ctrl+F |
| 下一个 / 上一个匹配项 | F3 / Shift+F3 | F3 / Shift+F3 |
| 撤销侧栏移除（5 秒内） | Cmd+Option+Z | Ctrl+Alt+Z |
| 退出多选 / 关闭查找 | Esc | Esc |
| 源码 / 分屏 / 预览 | Cmd+1 / 2 / 3 | Ctrl+1 / 2 / 3 |
| 展开或收起侧栏 | Cmd+B | Ctrl+B |
| 设置 | Cmd+, | Ctrl+, |
| 导出 HTML | Cmd+Shift+E | Ctrl+Shift+E |

## 技术栈

ZMark 使用 **Rust** 和 **GPUI** 构建桌面应用，使用 **pulldown-cmark** 解析 Markdown、**syntect** 实现代码高亮，并用 **rusty-mermaid** 渲染图表。本地图片由 Rust 的 `image` 库解码，macOS 大尺寸不透明 PNG/JPEG 预览使用原生 ImageIO 缩略解码。预览图表按实际显示尺寸栅格化，不再使用的纹理及时释放。测量与剩余限制见[版本更新说明](https://github.com/2716190547/zmark-releases/releases/tag/v0.2.9)；占用会随文档、媒体和窗口尺寸变化。
