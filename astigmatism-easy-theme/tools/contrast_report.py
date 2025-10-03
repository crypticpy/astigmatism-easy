#!/usr/bin/env python3
"""Contrast verification tool for AstigmatismEasy themes."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[1]
THEME_DIR = ROOT / "themes"


def parse_color(value: str) -> Tuple[float, float, float]:
    if not value.startswith("#"):
        raise ValueError(f"Unsupported color format: {value}")
    hex_part = value[1:7]
    r = int(hex_part[0:2], 16) / 255.0
    g = int(hex_part[2:4], 16) / 255.0
    b = int(hex_part[4:6], 16) / 255.0
    return (r, g, b)


def srgb_to_linear(channel: float) -> float:
    return channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb: Tuple[float, float, float]) -> float:
    r, g, b = (srgb_to_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def lstar(rgb: Tuple[float, float, float]) -> float:
    y = relative_luminance(rgb)
    if y <= 0.008856:
        return 903.3 * y
    return 116 * (y ** (1 / 3)) - 16


def contrast_ratio(foreground: str, background: str) -> Tuple[float, float]:
    fg_rgb = parse_color(foreground)
    bg_rgb = parse_color(background)
    l_fg = relative_luminance(fg_rgb)
    l_bg = relative_luminance(bg_rgb)
    ratio = (max(l_fg, l_bg) + 0.05) / (min(l_fg, l_bg) + 0.05)
    delta = abs(lstar(fg_rgb) - lstar(bg_rgb))
    return ratio, delta


def find_token_color(theme: dict, scopes: Sequence[str]) -> Optional[str]:
    for entry in theme.get("tokenColors", []):
        entry_scopes = entry.get("scope")
        if isinstance(entry_scopes, str):
            entry_scopes = [entry_scopes]
        if not isinstance(entry_scopes, list):
            continue
        settings = entry.get("settings", {})
        color = settings.get("foreground")
        if not color:
            continue
        if any(scope in entry_scopes for scope in scopes):
            return color
    return None


Check = Tuple[str, Tuple[str, ...], Tuple[str, ...]]

COLOR_CHECKS: List[Check] = [
    ("Editor Text", ("colors", "editor.foreground"), ("colors", "editor.background")),
    ("Inactive Tabs", ("colors", "tab.inactiveForeground"), ("colors", "tab.inactiveBackground")),
    ("Active Tabs", ("colors", "tab.activeForeground"), ("colors", "tab.activeBackground")),
    ("Status Bar", ("colors", "statusBar.foreground"), ("colors", "statusBar.background")),
    ("Terminal", ("colors", "terminal.foreground"), ("colors", "terminal.background")),
    ("Breadcrumb", ("colors", "breadcrumb.foreground"), ("colors", "breadcrumb.background")),
    ("Editor Hint", ("colors", "editorInlayHint.foreground"), ("colors", "editor.background")),
]

TOKEN_CHECKS: List[Tuple[str, Sequence[str]]] = [
    ("Keyword", ("keyword", "keyword.control")),
    ("String", ("string", "string.quoted")),
    ("Number", ("constant.numeric",)),
    ("Comment", ("comment", "punctuation.definition.comment"))
]


def resolve_color(theme: dict, path: Tuple[str, ...]) -> Optional[str]:
    node = theme
    for key in path:
        if not isinstance(node, dict):
            return None
        node = node.get(key)
    return node if isinstance(node, str) else None


def evaluate_theme(theme_path: Path, threshold: float) -> None:
    with theme_path.open("r", encoding="utf-8") as handle:
        theme = json.load(handle)

    print(f"\nTheme: {theme.get('name', theme_path.name)}")
    print("=" * (len(theme.get('name', theme_path.name)) + 7))

    for label, fg_path, bg_path in COLOR_CHECKS:
        fg = resolve_color(theme, fg_path)
        bg = resolve_color(theme, bg_path)
        if not fg or not bg:
            continue
        ratio, delta = contrast_ratio(fg, bg)
        status = "PASS" if ratio >= threshold else "WARN"
        print(f"- {label:<15} ratio={ratio:4.2f} ΔL*={delta:4.1f} [{status}] ({fg} vs {bg})")

    editor_bg = resolve_color(theme, ("colors", "editor.background"))
    if editor_bg:
        for label, scopes in TOKEN_CHECKS:
            token_color = find_token_color(theme, scopes)
            if not token_color:
                continue
            ratio, delta = contrast_ratio(token_color, editor_bg)
            status = "PASS" if ratio >= threshold else "WARN"
            print(f"- {label:<15} ratio={ratio:4.2f} ΔL*={delta:4.1f} [{status}] ({token_color} vs {editor_bg})")


def iter_theme_files(targets: Iterable[str]) -> List[Path]:
    paths: List[Path] = []
    for target in targets:
        path = Path(target)
        if path.is_dir():
            paths.extend(sorted(path.glob("*.json")))
        else:
            paths.append(path)
    if not paths:
        paths = sorted(THEME_DIR.glob("*.json"))
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description="Contrast report for theme files")
    parser.add_argument("paths", nargs="*", help="Theme files or directories")
    parser.add_argument("--threshold", type=float, default=5.0, help="Minimum acceptable contrast ratio")
    args = parser.parse_args()

    for theme_path in iter_theme_files(args.paths):
        evaluate_theme(theme_path, args.threshold)


if __name__ == "__main__":
    main()
