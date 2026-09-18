# Omarchy Ankh

Tema claro, sóbrio e calmo para Omarchy v4. O Ankh combina off-white frio,
azul ardósia e acentos quentes dessaturados; os três wallpapers fornecidos
trazem estudo, natureza e referências médicas sem recorrer a imagens geradas.

![Desktop Ankh — captura real do Omarchy](preview.png)

![Lockscreen Ankh — captura real do Omarchy](preview-unlock.png)

## Instalação

```bash
omarchy theme install https://github.com/PedroAugustoOK/omarchy-ankh-theme
omarchy theme set ankh
```

Para usar este checkout durante o desenvolvimento:

```bash
mkdir -p ~/.config/omarchy/themes
ln -sfn "$PWD" ~/.config/omarchy/themes/ankh
omarchy theme set ankh
```

Alterne entre os três wallpapers com `omarchy theme bg next`.

## O que está incluído

- Paleta `colors.toml` com contraste mínimo de 7:1 para texto principal.
- `shell.toml` completo para barra, controles, menus, launcher, notificações,
  polkit, lockscreen e seletor de imagens do Quickshell.
- Ícones `Yaru-blue`, escolhidos para manter a identidade azul discreta em GTK.
- Integrações com GTK, Walker, Waybar, Mako, SwayOSD, Superfile, Zed, btop,
  Chromium, Cava, fzf, Steam e Vencord.
- Complementos opcionais para bat, Lazygit, Fastfetch, Yazi e git-delta em
  [INTEGRATIONS.md](INTEGRATIONS.md).

O Omarchy gera automaticamente terminal, Neovim, Helix, VS Code e Obsidian a
partir de `colors.toml`. Os arquivos opcionais não são copiados sobre suas
preferências existentes.

## Wallpapers

Há exatamente três imagens PNG em 3840×2160 (16:9):

- `01-ankh-study.png` — mesa junto à janela, luz quente e vegetação.
- `02-ankh-meadow.png` — estudo aberto para campo e vila distante.
- `03-ankh-window.png` — mesa clara, caderno e laptop junto à janela.

## Desenvolvimento

Valide localmente com:

```bash
python3 scripts/validate-theme.py
```

O teste verifica paleta, contraste, formatos TOML/JSON, referências de cores,
assets obrigatórios, previews reais e as três imagens em alta resolução.
Leia [CONTRIBUTING.md](CONTRIBUTING.md) antes de alterar assets e consulte
[CHANGELOG.md](CHANGELOG.md) para as versões.

Notas de origem dos assets: [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

Para a variante noturna, veja
[Omarchy Ankh Dark](https://github.com/PedroAugustoOK/omarchy-ankh-dark-theme).

## Licença

[MIT](LICENSE).
