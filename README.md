# Omarchy Ankh

Tema claro e sóbrio para Omarchy, com azul ardósia, neutros frios e acentos
quentes dessaturados. Os wallpapers retratam um espaço de estudo e trabalho
com referências médicas, natureza e fantasia — a identidade visual do Ankh.

Omarchy's light theme with slate blue, cool neutrals, and muted warm accents.
Its wallpapers portray a study and work space shaped by medical references,
nature, and fantasy.

![Prévia do Omarchy Ankh](preview.png)

## Estrutura / Structure

- `colors.toml`: paleta semântica principal do Omarchy v4 / main Omarchy v4 palette.
- `icons.theme`: ícones Yaru Blue / Yaru Blue icons.
- `preview.png`: imagem do seletor de temas / theme selector preview.
- `preview-unlock.png`: prévia da tela de desbloqueio / unlock preview.
- `unlock.png`: símbolo Ankh transparente / transparent Ankh emblem.
- `backgrounds/`: wallpapers 16:9 e 21:9 / 16:9 and 21:9 wallpapers.

## Wallpapers

### 16:9

- `01-ankh-study.png`: escritório com vista para as montanhas.
- `02-ankh-meadow.png`: campo aberto visto do espaço de estudo.
- `03-ankh-window.png`: janela, mesa e paisagem ao entardecer.

### Ultrawide 21:9

- `01-ankh-study-ultrawide.png`
- `02-ankh-meadow-ultrawide.png`
- `03-ankh-window-ultrawide.png`

## Integrações / Integrations

O Omarchy gera automaticamente os temas do terminal, Neovim, Helix, VS Code,
btop, Chromium e do shell a partir de `colors.toml`. Este repositório também
inclui refinamentos para GTK, Walker, Waybar, Mako, SwayOSD, Superfile e Zed.

Omarchy generates terminal, Neovim, Helix, VS Code, btop, Chromium, and shell
themes from `colors.toml`. This repository also includes refinements for GTK,
Walker, Waybar, Mako, SwayOSD, Superfile, and Zed.

Arquivos que executam código — como `.lua`, configurações de terminal e
`vscode.json` — são deliberadamente evitados para manter o tema seguro quando
instalado a partir de um repositório Git.

## Instalação local / Local installation

```bash
mkdir -p ~/.config/omarchy/themes
ln -sfn "$PWD" ~/.config/omarchy/themes/ankh
omarchy theme set ankh
```

## Instalação pelo GitHub / GitHub installation

```bash
omarchy theme install https://github.com/PedroAugustoOK/omarchy-ankh-theme
omarchy theme set ankh
```

Alterne os wallpapers com:

```bash
omarchy theme bg next
```

## Paleta / Palette

- Fundo / background: off-white frio `#F4F6F8`
- Superfícies / surfaces: cinza-azulado `#E8EDF1`
- Destaque / accent: azul ardósia `#527A9E`
- Texto / text: azul-marinho `#243746`

## Desenvolvimento / Development

O GitHub Actions valida automaticamente a paleta, o `preview.png`, o
`preview-unlock.png` e as proporções dos wallpapers.

## Licença / License

MIT. Veja [LICENSE](LICENSE).
