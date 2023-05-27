# trigo_api.py

##############################################################################
#                                   Imports                                  #
##############################################################################
from trigo_and_log import *

##############################################################################
#                                 CONSTANTS                                  #
##############################################################################
SIN = 1
COS = 2
TAN = 3
ARC_SIN = 4
ARC_COS = 5
ARC_TAN = 6
LN = 7
LOG2 = 8
EXP = 9
EXIT = 0


def print_trigo_and_log_menu() -> int:
    print("\nTrigonometry and Logarithms Menu:")
    print("1: Calculate the sine of x (x in radians)")
    print("2: Calculate the cosine of x (x in radians)")
    print("3: Calculate the tangent of x (x in radians)")
    print("4: Calculate the arc-sine of x")
    print("5: Calculate the arc cosine of x")
    print("6: Calculate the arc-tangent of x")
    print("7: Calculate the natural logarithm of x")
    print("8: Calculate the base-2 logarithm of x")
    print("9: Calculate e raised to the power x")
    print("0: Exit")
    tl_option = int(input("Enter an option: "))
    return tl_option


def trigo_and_log_menu():
    tl_option = print_trigo_and_log_menu()
    if tl_option == SIN:
        pass
    elif tl_option == COS:
        pass
    elif tl_option == TAN:
        pass
    elif tl_option == ARC_SIN:
        pass
    elif tl_option == ARC_COS:
        pass
    elif tl_option == ARC_TAN:
        pass
    elif tl_option == LN:
        pass
    elif tl_option == LOG2:
        pass
    elif tl_option == EXP:
        pass
    elif tl_option == EXIT:
        return
    else:
        print("Invalid option. Please try again.")
