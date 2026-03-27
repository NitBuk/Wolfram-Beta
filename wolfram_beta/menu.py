"""Shared terminal menu helpers."""

from __future__ import annotations

from typing import Sequence


def prompt_int(prompt: str, input_fn=input) -> int:
    """Prompt until the user enters a valid integer."""
    while True:
        try:
            return int(input_fn(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def prompt_float(prompt: str, input_fn=input) -> float:
    """Prompt until the user enters a valid number."""
    while True:
        try:
            return float(input_fn(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def render_menu(title: str, options: Sequence[tuple[int, str]]) -> int:
    """Render a numbered menu and return the selected option."""
    print(f"\n{title}:")
    for option, description in options:
        print(f"{option}: {description}")
    print("0: Exit")
    return prompt_int("Enter an option: ")


def not_implemented(feature: str) -> None:
    """Announce that a menu item is only scaffolding for now."""
    print(f"{feature} is not wired into the interactive flow yet.")
