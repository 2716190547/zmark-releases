<div align="center">

<img src="assets/macos-icon.png" alt="ZMark Logo" width="112" height="112" />

# ZMark Releases

**[ZMark](https://github.com/2716190547/zmark) 官方桌面安装包与签名自动更新分发仓库 —— 基于 Rust 与 GPUI 打造的原生极速本地 Markdown 编辑器、阅读工作台与 Mermaid 图表工作室。**

[![Release](https://img.shields.io/github/v/release/2716190547/zmark-releases?label=%E6%9C%80%E6%96%B0%E7%89%88%E6%9C%AC&color=E06C44&style=flat-square)](https://github.com/2716190547/zmark-releases/releases)
[![Source Repo](https://img.shields.io/badge/%E6%BA%90%E7%A0%81%E4%BB%93%E5%BA%93-2716190547%2Fzmark-2563EB?style=flat-square)](https://github.com/2716190547/zmark)
[![Platform](https://img.shields.io/badge/%E6%94%AF%E6%8C%81%E5%B9%B3%E5%8F%B0-macOS%20%7C%20Windows%20%7C%20Linux-4B5563?style=flat-square)](#下载与安装)

[简体中文](README.zh-CN.md) · [English](README.md) · [源码与反馈](https://github.com/2716190547/zmark) · [Gitee 国内镜像](https://gitee.com/zeng_sc/zmark-releases/releases)

</div>

---

## 下载与安装

**当前最新版本：`v0.2.10`** · [版本更新说明](https://github.com/2716190547/zmark/blob/master/docs/releases/v0.2.10.md) · [对应源码 `309d05e`](https://github.com/2716190547/zmark/tree/309d05eb6b934c0d94430d40ca42f71525a798c3)

可从 [GitHub Releases](https://github.com/2716190547/zmark-releases/releases/tag/v0.2.10) 下载对应系统安装包；国内网络也可通过 [Gitee 发行镜像](https://gitee.com/zeng_sc/zmark-releases/releases) 获取 macOS ZIP、Windows 安装包与签名更新清单（DMG 与 Linux 安装包请前往 GitHub 下载）。

| 平台 | 架构 | 安装包格式 | 安装说明 |
| --- | --- | --- | --- |
| **macOS** | Apple Silicon (`arm64`) | `.zip` / `.dmg` | 解压或打开镜像，将 `ZMark.app` 拖入「应用程序」目录即可。 |
| **Windows** | `x86_64` | Setup `.exe` | 双击运行安装向导完成安装。 |
| **Linux** | `x86_64` | `.deb` / `.tar.gz` | 通过 `apt` / `dpkg` 安装 `.deb`，或解压压缩包后运行 `usr/bin/zmark_app`。 |

> [!NOTE]
> macOS 应用包当前为 Ad-Hoc 本地签名（未经过 Apple 公证），Windows 安装程序暂无商业发布者代码签名。预览窗格出于隐私与性能考虑不请求远程网络图片 URL，请使用相对当前文档路径或绝对路径引用本地图片。导出 HTML 会内嵌排版样式表，图片路径保持引用不变，Mermaid 块保留为代码形式。

---

## 核心特性与快捷操作

- **三种视图与同步滚动**：按 `Cmd+1 / 2 / 3`（Windows/Linux 为 `Ctrl+1 / 2 / 3`）瞬间切换**源码 / 分屏 / 预览**；分屏支持按块精准对齐和平滑同步滚动，搭配跨平台悬停滚动条。
- **侧栏工作区与大纲**：按 `Cmd+Shift+B`（`Ctrl+Shift+B`）展开/收起侧栏，按 `Cmd+Shift+O`（`Ctrl+Shift+O`）快速互切**文件夹与大纲**；支持拖入文件夹与多选批量管理、5 秒撤销移除（`Cmd+Option+Z` / `Ctrl+Alt+Z`）与双击重命名。
- **Markdown 与图表渲染**：支持 GFM 表格、任务清单、多语言代码高亮一键复制、`rusty-mermaid` 原生矢量流程图、本地位图与 SVG 预览，以及点击进入 HiDPI 灯箱放大检视。
- **主题配色与键位自定义**：按 `Cmd+,`（`Ctrl+,`）打开设置，支持 7 套明暗调色板、19 项完整颜色自定义、10 种界面语言及快捷键录制重设。
- **导出 HTML**：按 `Cmd+Shift+E`（`Ctrl+Shift+E`）一键导出排版美观的 HTML 文档。

完整的源码构建、架构说明与开发指南，请访问主仓库 **[ZMark GitHub 源码仓库](https://github.com/2716190547/zmark)**。
