"""CLI entrypoint for Wolfram Beta."""

from __future__ import annotations

import sys

from calculus_api import calculus_menu
from linear_api import linear_menu
from number_api import number_theory_menu
from statistics_api import statistics_and_probability_menu
from trigo_api import trigo_and_log_menu

from .commands import execute_command
from .menu import render_menu


MENU_LINEAR = 1
MENU_CALCULUS = 2
MENU_NUMBER_THEORY = 3
MENU_STATISTICS = 4
MENU_TRIG = 5
MENU_EXIT = 0


def _main_menu() -> int:
    return render_menu(
        "Main Menu",
        [
            (MENU_LINEAR, "Linear Algebra"),
            (MENU_CALCULUS, "Calculus"),
            (MENU_NUMBER_THEORY, "Number Theory"),
            (MENU_STATISTICS, "Statistics and Probability"),
            (MENU_TRIG, "Trigonometry and Logarithms"),
        ],
    )


def main(argv: list[str] | None = None) -> int:
    """Run Wolfram Beta in interactive or command mode."""
    if argv is None:
        argv = sys.argv[1:]
    if argv:
        return execute_command(argv)

    print("Welcome to Wolfram Beta!")
    while True:
        choice = _main_menu()

        if choice == MENU_LINEAR:
            linear_menu()
        elif choice == MENU_CALCULUS:
            calculus_menu()
        elif choice == MENU_NUMBER_THEORY:
            number_theory_menu()
        elif choice == MENU_STATISTICS:
            statistics_and_probability_menu()
        elif choice == MENU_TRIG:
            trigo_and_log_menu()
        elif choice == MENU_EXIT:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

    return 0
