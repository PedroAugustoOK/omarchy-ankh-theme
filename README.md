# Omarchy Ankh

Tema claro e sóbrio para Omarchy, com azul ardósia, neutros frios e acentos
quentes dessaturados. Os wallpapers retratam um espaço de estudo e trabalho
com referências médicas, natureza e fantasia — a identidade visual do Ankh.

![Prévia do Omarchy Ankh](preview.png)

## Estrutura

- `colors.toml`: paleta semântica principal do Omarchy v4.
- `icons.theme`: ícones Yaru Blue.
- `preview.png`: imagem usada no seletor de temas.
- `backgrounds/`: wallpapers principais do tema.

## Wallpapers

- `01-ankh-study.png`: escritório com vista para as montanhas.
- `02-ankh-meadow.png`: campo aberto visto do espaço de estudo.
- `03-ankh-window.png`: janela, mesa e paisagem ao entardecer.

## Instalação local

Copie ou vincule este diretório para o diretório de temas do usuário:

```bash
mkdir -p ~/.config/omarchy/themes
ln -sfn "$PWD" ~/.config/omarchy/themes/ankh
omarchy theme set ankh
```

O link simbólico deve apontar para este diretório do projeto. Assim, alterações
na paleta podem ser reaplicadas sem duplicar os arquivos.

## Instalação pelo GitHub

```bash
omarchy theme install https://github.com/PedroAugustoOK/omarchy-ankh-theme
omarchy theme set ankh
```

## Paleta

- Fundo: off-white frio `#F4F6F8`
- Superfícies: cinza-azulado `#E8EDF1`
- Destaque: azul ardósia `#527A9E`
- Texto: azul-marinho `#243746`

## Licença

MIT. Veja [LICENSE](LICENSE).
