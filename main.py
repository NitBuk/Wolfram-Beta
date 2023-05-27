# main.py

"""
Wolfram Beta - A comprehensive calculator for Linear Algebra, Calculus, Number Theory, Statistics, Probability, Trigonometry, and Logarithms.
"""

##############################################################################
#                                   Imports                                  #
##############################################################################
from linear_api import *
from calculus_api import *
from number_api import *
from statistics_api import *
from trigo_api import *
# import pytest

##############################################################################
#                                 CONSTANTS                                  #
##############################################################################
LINEAR = 1
CALCULUS = 2
NUMBER_THEORY = 3
STATISTICS_AND_PROBABILITY = 4
TRIGONOMETRY_AND_LOGARITHMS = 5
EXIT = 0
# TEST = -1


def math_menu() -> int:
    print("\nMain Menu:")
    print("1: Linear Algebra")
    print("2: Calculus")
    print("3: Number Theory")
    print("4: Statistics and Probability")
    print("5: Trigonometry and logarithms")
    # print("-1: Run tests") # option to run tests
    print("0: Exit")
    main_option = int(input("Enter an option: "))
    return main_option


def wolfram_beta():
    print("Welcome to Wolfram Beta!")
    while True:
        main_option = math_menu()

        if main_option == LINEAR:
            linear_menu()

        elif main_option == CALCULUS:
            calculus_menu()

        elif main_option == NUMBER_THEORY:
            number_theory_menu()

        elif main_option == STATISTICS_AND_PROBABILITY:
            statistics_and_probability_menu()

        elif main_option == TRIGONOMETRY_AND_LOGARITHMS:
            trigo_and_log_menu()

        # elif main_option == TEST:
        #     pytest.main(['-x', 'test.py'])

        elif main_option == EXIT:
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    wolfram_beta()
