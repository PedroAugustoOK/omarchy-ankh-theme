#!/usr/bin/env python3
"""Offline validation for the Omarchy Ankh theme assets."""

from __future__ import annotations

import json
import re
import struct
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODE = "light"
REQUIRED_FILES = {
    "shell.toml", "gtk.css", "walker.css", "mako.ini", "swayosd.css",
    "waybar.css", "btop.theme", "chromium.theme", "superfile.toml",
    "zed.json", "cava_theme", "fzf.fish", "steam.css", "vencord.theme.css",
    "bat.conf", "lazygit.yml", "fastfetch.jsonc", "yazi-theme.toml",
    "delta.gitconfig", "INTEGRATIONS.md", "CONTRIBUTING.md", "CHANGELOG.md",
    "LICENSE", "ATTRIBUTIONS.md", "unlock.png",
}
REQUIRED_SHELL_SECTIONS = {
    "bar", "controls", "spacing", "font", "popups", "tooltip",
    "notifications", "launcher", "menu", "polkit", "lock", "image-picker",
}
COLOR_SOURCES = {
    "shell.toml", "gtk.css", "walker.css", "mako.ini", "swayosd.css",
    "waybar.css", "btop.theme", "chromium.theme", "superfile.toml", "zed.json",
    "cava_theme", "steam.css", "vencord.theme.css", "lazygit.yml",
    "fastfetch.jsonc", "yazi-theme.toml", "delta.gitconfig",
}


def luminance(color: str) -> float:
    channels = [int(color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4 for channel in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(first: str, second: str) -> float:
    one, two = luminance(first), luminance(second)
    return (max(one, two) + 0.05) / (min(one, two) + 0.05)


def png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as image:
        assert image.read(8) == b"\x89PNG\r\n\x1a\n", f"{path.name} is not a PNG"
        image.read(4)
        assert image.read(4) == b"IHDR", f"{path.name} has no IHDR"
        return struct.unpack(">II", image.read(8))


def main() -> None:
    palette = tomllib.loads((ROOT / "colors.toml").read_text())
    assert palette.get("mode") == MODE, f"colors.toml must define mode = {MODE!r}"
    colors = {key: value for key, value in palette.items() if key != "mode"}
    assert len(colors) >= 20, "palette is missing semantic colors"
    assert all(re.fullmatch(r"#[0-9A-Fa-f]{6}", value) for value in colors.values()), "invalid palette hex color"
    assert contrast(palette["foreground"], palette["background"]) >= 7, "body text contrast must be at least 7:1"
    assert contrast(palette["accent"], palette["background"]) >= 4.5, "accent contrast must be at least 4.5:1"
    assert contrast(palette["muted"], palette["background"]) >= 4.5, "muted text contrast must be at least 4.5:1"

    missing = sorted(name for name in REQUIRED_FILES if not (ROOT / name).is_file())
    assert not missing, f"missing theme files: {', '.join(missing)}"

    shell = tomllib.loads((ROOT / "shell.toml").read_text())
    assert REQUIRED_SHELL_SECTIONS <= set(shell), "shell.toml is missing a required surface section"
    tomllib.loads((ROOT / "superfile.toml").read_text())
    tomllib.loads((ROOT / "yazi-theme.toml").read_text())
    json.loads((ROOT / "zed.json").read_text())
    json.loads((ROOT / "fastfetch.jsonc").read_text())
    assert "[delta]" in (ROOT / "delta.gitconfig").read_text(), "delta.gitconfig is missing the delta section"

    palette_values = {value.lower() for value in colors.values()}
    for filename in COLOR_SOURCES:
        used = {value.lower() for value in re.findall(r"#[0-9A-Fa-f]{6}", (ROOT / filename).read_text())}
        unknown = sorted(used - palette_values)
        assert not unknown, f"{filename} uses colors outside colors.toml: {', '.join(unknown)}"

    for preview_name in ("preview.png", "preview-unlock.png"):
        width, height = png_size(ROOT / preview_name)
        assert width >= 1000 and height >= 500, f"{preview_name} is too small"
        assert abs((width / height) - (16 / 9)) < 0.03, f"{preview_name} must be 16:9"

    wallpapers = sorted((ROOT / "backgrounds").glob("*.png"))
    assert len(wallpapers) == 3, "exactly three wallpapers are required"
    for wallpaper in wallpapers:
        assert png_size(wallpaper) == (3840, 2160), f"{wallpaper.name} must be 3840x2160"

    print(f"Validated {len(colors)} colors, {len(REQUIRED_FILES)} required files, real previews, and {len(wallpapers)} wallpapers.")


if __name__ == "__main__":
    main()
