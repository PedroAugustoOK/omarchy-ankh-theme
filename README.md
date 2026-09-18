<p align="center">
  <img src="unlock.png" width="190" alt="Ankh emblem">
</p>

<h1 align="center">Omarchy Ankh</h1>

<p align="center">
  A calm, high-contrast light theme for <strong>Omarchy v4</strong>.<br>
  Cool paper, slate blue, and three supplied high-resolution wallpapers.
</p>

<p align="center">
  <a href="https://github.com/PedroAugustoOK/omarchy-ankh-theme/releases/tag/v1.0.0"><img src="https://img.shields.io/github/v/release/PedroAugustoOK/omarchy-ankh-theme?display_name=tag&style=flat-square" alt="Latest release"></a>
  <a href="https://github.com/PedroAugustoOK/omarchy-ankh-theme/actions/workflows/validate.yml"><img src="https://github.com/PedroAugustoOK/omarchy-ankh-theme/actions/workflows/validate.yml/badge.svg" alt="Validation status"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/PedroAugustoOK/omarchy-ankh-theme?style=flat-square" alt="MIT license"></a>
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#gallery">Gallery</a> ·
  <a href="#whats-included">Included</a> ·
  <a href="INTEGRATIONS.md">Integrations</a> ·
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

![Omarchy Ankh desktop — real Quickshell menu capture](preview.png)

## A considered light theme

Ankh is for a desktop that feels focused rather than sterile: cool off-white
surfaces, legible slate-blue focus states, and small warm accents for context.
It is built around the supplied study wallpapers, not around generated artwork.

- **Readable by default** — 7:1 minimum contrast for primary text, 4.5:1 for accent and muted text.
- **A complete shell** — bar, launcher, menus, notifications, polkit, image picker, and lock screen share one surface language.
- **Safe to install** — works with Omarchy's Git-installed-theme model without shipping executable configuration.

## Install

~~~bash
omarchy theme install https://github.com/PedroAugustoOK/omarchy-ankh-theme
omarchy theme set ankh
~~~

Cycle the three included wallpapers with <code>omarchy theme bg next</code>.

> Want the nocturnal counterpart? See [Omarchy Ankh Dark](https://github.com/PedroAugustoOK/omarchy-ankh-dark-theme).

## Gallery

<table>
  <tr>
    <td width="50%">
      <img src="preview.png" alt="Ankh light desktop with the Omarchy menu">
      <sub><strong>Desktop</strong> — real Quickshell menu capture.</sub>
    </td>
    <td width="50%">
      <img src="preview-unlock.png" alt="Ankh light lock screen with visible password field">
      <sub><strong>Lock screen</strong> — actual Omarchy lock preview.</sub>
    </td>
  </tr>
</table>

All previews are real captures from this theme on Omarchy v4. They are never AI
mockups. The desktop image shows the included Ankh workspace; the lock screen
shows the password field in its standard position.

## What's included

| Surface | Coverage |
| --- | --- |
| **Omarchy** | colors.toml, Quickshell shell.toml, Yaru Blue icons, three 3840×2160 wallpapers |
| **Desktop** | GTK, Walker, Waybar, Mako, SwayOSD, Superfile, Zed, Chromium |
| **Terminal & media** | btop, Cava, fzf, Steam, Vencord |
| **Optional companions** | bat, Lazygit, Fastfetch, Yazi, git-delta — see [INTEGRATIONS.md](INTEGRATIONS.md) |

Omarchy automatically derives terminal, Neovim, Helix, VS Code, and Obsidian
from colors.toml. Optional companion files are documented separately so they
never overwrite a person's existing configuration.

## Wallpapers

Exactly three PNG wallpapers are included, each at **3840×2160**:

| File | Scene |
| --- | --- |
| 01-ankh-study.png | Desk by a window, warm light, and greenery |
| 02-ankh-meadow.png | Study opening toward a meadow and distant village |
| 03-ankh-window.png | Bright desk, notebook, and laptop by the window |

Their origin and processing notes live in [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

## Project quality

~~~bash
python3 scripts/validate-theme.py
~~~

The same validation runs in GitHub Actions. It checks palette semantics,
contrast, TOML/JSON parsing, color references, required assets, real preview
dimensions, and the three exact wallpaper dimensions.

- [Design principles](docs/DESIGN.md)
- [Integration guide](INTEGRATIONS.md)
- [Contribution guide](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

## License

[MIT](LICENSE).
