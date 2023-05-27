# number_api.py

##############################################################################
#                                   Imports                                  #
##############################################################################
from number_theory import *

##############################################################################
#                                 CONSTANTS                                  #
##############################################################################
PRIME = 1
PRIME_FACTORS = 2
POWER = 3
SQRT = 4
GCD = 5
LCM = 6
FIBONACCI = 7
FACTORIAL = 8
EXIT = 0


def print_number_theory_menu() -> int:
    print("\nNumber Theory Menu:")
    print("1: Check if a number is prime")
    print("2: Calculate the prime factorization of a number")
    print("3: Calculate the power of a base number")
    print("4: Calculate the square root of a number")
    print("5: Find the greatest common divisor of two numbers")
    print("6: Find the least common multiple of two numbers")
    print("7: Calculates the nth number in the Fibonacci sequence")
    print("8: Calculate the factorial of a non-negative integer")
    print("0: Exit")
    nt_option = int(input("Enter an option: "))
    return nt_option


def number_theory_menu():
    nt_option = print_number_theory_menu()
    if nt_option == PRIME:
        pass
    elif nt_option == PRIME_FACTORS:
        pass
    elif nt_option == POWER:
        pass
    elif nt_option == SQRT:
        pass
    elif nt_option == GCD:
        pass
    elif nt_option == LCM:
        pass
    elif nt_option == FIBONACCI:
        pass
    elif nt_option == FACTORIAL:
        pass
    elif nt_option == EXIT:
        return
    else:
        print("Invalid option. Please try again.")
