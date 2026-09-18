# Ankh design principles

## Intent

Ankh light is a focused reading and study environment. It uses a cool paper
background rather than pure white, slate-blue interaction states, and muted
warm colors only where information needs hierarchy.

## Surface hierarchy

| Layer | Role |
| --- | --- |
| Background | Quiet off-white canvas that lets wallpaper photography breathe |
| Surface | Blue-grey panels for menus, tooltips, and application chrome |
| Focus | Slate-blue borders and selected states, never bright neon |
| Text | Deep blue-black for comfortable long reading |
| Signals | Restrained sage, rose, ochre, cyan, and violet semantic colors |

## Light and dark are companions

Ankh and Ankh Dark use the same geometry, icons, semantic color roles, and
lockscreen treatment. Light is open and editorial; Dark is nocturnal and
contained. They should feel like the same system at different hours.

## Real imagery only

The theme has exactly three supplied wallpapers. Previews must be captured from
a running Omarchy session and must show actual UI states. Do not replace them
with generated scenes or UI mockups.

## Accessibility contract

Primary text must retain at least 7:1 contrast against its background. Accent
and muted text must retain at least 4.5:1. This is enforced by the validation
script before publication.
