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
- `backgrounds/`: três wallpapers 16:9 em alta resolução / three high-resolution 16:9 wallpapers.

## Wallpapers

O tema contém exatamente três wallpapers 16:9 em 3840×2160. Eles são
fotografias reais, apenas recortadas, ampliadas e tratadas com uma graduação
pastel azul-ardósia para combinar com o tema.

The theme contains exactly three 3840×2160 16:9 wallpapers. They are real
photographs, only cropped, upscaled, and given a restrained slate-blue pastel
grade to match the theme.

- `01-ankh-study.png`: mesa junto à janela, com luz quente e vegetação.
- `02-ankh-mountain.png`: montanha nevada em luz suave.
- `03-ankh-lake.png`: lago enevoado cercado por pinheiros.

## Integrações / Integrations

O Omarchy gera automaticamente os temas do terminal, Neovim, Helix, VS Code,
btop, Chromium e do shell a partir de `colors.toml`. Este repositório também
inclui refinamentos para GTK, Walker, Waybar, Mako, SwayOSD, Superfile e Zed.

`preview.png` e `preview-unlock.png` são capturas reais do desktop e do
lockscreen do Omarchy, não mockups gerados.

`preview.png` and `preview-unlock.png` are real captures of the Omarchy
desktop and lock screen, not generated UI mockups.

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
`preview-unlock.png` e garante que existam exatamente três wallpapers 16:9.

As fontes e os créditos das fotografias estão em
[ATTRIBUTIONS.md](ATTRIBUTIONS.md).

Uma variante escura instalável está disponível em
[omarchy-ankh-dark-theme](https://github.com/PedroAugustoOK/omarchy-ankh-dark-theme).

An installable dark companion is available at
[omarchy-ankh-dark-theme](https://github.com/PedroAugustoOK/omarchy-ankh-dark-theme).

## Licença / License

MIT. Veja [LICENSE](LICENSE).
