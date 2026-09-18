# Integrações Ankh

O Omarchy aplica automaticamente o tema de terminal, Neovim, Helix, VS Code,
Chromium e Obsidian a partir de `colors.toml`. Os arquivos abaixo são
complementos opcionais; eles não são copiados automaticamente para não apagar
preferências existentes.

| Ferramenta | Arquivo | Como usar |
| --- | --- | --- |
| bat | `bat.conf` | Mescle em `~/.config/bat/config`. Usa `ansi`, portanto acompanha a paleta do terminal. |
| Lazygit | `lazygit.yml` | Mescle somente `gui.theme` em `~/.config/lazygit/config.yml`. |
| Fastfetch | `fastfetch.jsonc` | Teste com `fastfetch --config /caminho/fastfetch.jsonc`; depois copie ou mescle em `~/.config/fastfetch/config.jsonc`. |
| Yazi | `yazi-theme.toml` | Mescle em `~/.config/yazi/theme.toml`; o arquivo não muda atalhos ou layout. |
| git-delta | `delta.gitconfig` | Adicione um `include.path` ao seu `~/.gitconfig`, apontando para este arquivo. |

As integrações do próprio tema — Quickshell, GTK, Walker, Waybar, Mako,
SwayOSD, Superfile, Zed, btop, Cava, fzf, Steam e Vencord — são disponibilizadas
como assets de cor e preservam as decisões de segurança do instalador de temas
do Omarchy.
