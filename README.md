<div align="center">

<img src="assets/macos-icon.png" alt="ZMark Logo" width="112" height="112" />

# ZMark Releases

**Official installers and signed auto-update feeds for [ZMark](https://github.com/2716190547/zmark) — a fast, native local-first Markdown editor, reader, and Mermaid diagram workspace built with Rust & GPUI.**

[![Release](https://img.shields.io/github/v/release/2716190547/zmark-releases?label=Latest%20Release&color=E06C44&style=flat-square)](https://github.com/2716190547/zmark-releases/releases)
[![Source Repo](https://img.shields.io/badge/Source-2716190547%2Fzmark-2563EB?style=flat-square)](https://github.com/2716190547/zmark)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Windows%20%7C%20Linux-4B5563?style=flat-square)](#download-and-install)

[English](README.md) · [简体中文](README.zh-CN.md) · [Source Repository](https://github.com/2716190547/zmark) · [Gitee Mirror](https://gitee.com/zeng_sc/zmark-releases/releases)

</div>

---

## Download and Install

**Current release: `v0.2.10`** · [Release Notes](https://github.com/2716190547/zmark/blob/master/docs/releases/v0.2.10.md) · [Tagged Source `309d05e`](https://github.com/2716190547/zmark/tree/309d05eb6b934c0d94430d40ca42f71525a798c3)

Download installers directly from [GitHub Releases](https://github.com/2716190547/zmark-releases/releases/tag/v0.2.10). Users in mainland China can also download the macOS ZIP, Windows installer, and signed update manifests via the [Gitee Mirror](https://gitee.com/zeng_sc/zmark-releases/releases) (DMG and Linux packages are hosted on GitHub).

| Platform | Architecture | Package | Install Instructions |
| --- | --- | --- | --- |
| **macOS** | Apple Silicon (`arm64`) | `.zip` / `.dmg` | Extract or mount and drag `ZMark.app` into `/Applications`. |
| **Windows** | `x86_64` | Setup `.exe` | Run the installer wizard. |
| **Linux** | `x86_64` | `.deb` / `.tar.gz` | Install via `apt` / `dpkg`, or extract and run `usr/bin/zmark_app`. |

> [!NOTE]
> The macOS bundle is Ad-Hoc signed (not Apple-notarized), and the Windows installer has no publisher code signature. Native local image previews do not fetch remote HTTP/HTTPS URLs; reference images locally relative to your Markdown file or via an absolute disk path. Exported HTML embeds typography CSS while keeping image paths as references and Mermaid blocks as fenced code.

---

## Key Capabilities & Shortcuts

- **Writing & Sync Scroll**: Switch seamlessly between **Source** (`Cmd+1` / `Ctrl+1`), **Split** (`Cmd+2` / `Ctrl+2`), and **Preview** (`Cmd+3` / `Ctrl+3`), with block-aligned smooth synchronized scrolling and hover scrollbars.
- **Workspace & Document Outline**: Open the sidebar with `Cmd+Shift+B` / `Ctrl+Shift+B` and toggle **Files ↔ Outline** with `Cmd+Shift+O` / `Ctrl+Shift+O`. Drop folders or Markdown files directly into the window, search by filename, undo sidebar removals (`Cmd+Option+Z` / `Ctrl+Alt+Z`), or double-click names to rename inline.
- **Markdown, Diagrams & Media**: Adaptive GFM tables, interactive task lists, multi-language code syntax highlighting with one-click copy, native local `rusty-mermaid` SVG diagrams, local image previews (PNG/JPEG/GIF/WebP/SVG), and interactive HiDPI Lightbox zoom.
- **Themes & Customizable Shortcuts**: Press `Cmd+,` / `Ctrl+,` for Settings — 7 light/dark palettes, a 19-token Custom Theme Editor, 10 UI languages, and customizable keyboard shortcuts (`Backspace` to unbind, live conflict detection).
- **Standalone HTML Export**: Export clean formatted HTML with `Cmd+Shift+E` / `Ctrl+Shift+E`.

For full developer documentation, architecture diagrams, and source builds, visit the main **[ZMark Source Repository](https://github.com/2716190547/zmark)**.
