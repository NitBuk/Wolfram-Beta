# calculus_api.py

##############################################################################
#                                   Imports                                  #
##############################################################################
from calculus import *

##############################################################################
#                                 CONSTANTS                                  #
##############################################################################
PLOT = 1
LIMIT = 2
DERIVATIVE = 3
INDEFINITE_INTEGRAL = 4
DEFINITE_INTEGRAL = 5
IMPROPER_INTEGRAL = 6
SECOND_DERIVATIVE = 7
EXIT = 0


def print_calculus_menu() -> int:
    print("\nCalculus Menu:")
    print("1: Plot a function")
    print("2: Calculate the limit of a function at a given point")
    print("3: Calculate the derivative of a function")
    print("4: Calculate the indefinite integral of a function")
    print("5: Calculate the definite integral of a function from a to b")
    print("6: Calculate the improper integral of a function from a to infinity")
    print("7: Calculate the second derivative of a function")
    print("0: Exit")
    calc_option = int(input("Enter an option: "))
    return calc_option


def calculus_menu():
    calc_option = print_calculus_menu()
    if calc_option == PLOT:
        pass
    elif calc_option == LIMIT:
        pass
    elif calc_option == DERIVATIVE:
        pass
    elif calc_option == INDEFINITE_INTEGRAL:
        pass
    elif calc_option == DEFINITE_INTEGRAL:
        pass
    elif calc_option == IMPROPER_INTEGRAL:
        pass
    elif calc_option == SECOND_DERIVATIVE:
        pass
    elif calc_option == EXIT:
        return
    else:
        print("Invalid option. Please try again.")
