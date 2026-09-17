# Omarchy Ankh

Tema claro e sóbrio para Omarchy, com neutros frios, azul ardósia e acentos
dessaturados inspirados nos wallpapers do tema.

## Estrutura

- `colors.toml`: paleta principal do Omarchy v4.
- `icons.theme`: ícones Yaru Blue.
- `backgrounds/`: wallpapers temporários do tema (`ankh-bus.jpg` e
  `ankh-mountain.jpg`).

## Instalação local

Copie ou vincule este diretório para o diretório de temas do usuário:

```bash
mkdir -p ~/.config/omarchy/themes
ln -sfn "$PWD" ~/.config/omarchy/themes/ankh
omarchy theme set ankh
```

O link simbólico deve apontar para este diretório do projeto. Assim, alterações
na paleta podem ser reaplicadas sem duplicar os arquivos.

## Paleta

- Fundo: off-white frio `#F4F6F8`
- Superfícies: cinza-azulado `#E8EDF1`
- Destaque: azul ardósia `#527A9E`
- Texto: azul-marinho `#243746`
