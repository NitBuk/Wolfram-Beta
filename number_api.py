"""Interactive menu scaffolding for number theory helpers."""

from wolfram_beta.menu import not_implemented, render_menu

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
    return render_menu(
        "Number Theory Menu",
        [
            (PRIME, "Check if a number is prime"),
            (PRIME_FACTORS, "Calculate the prime factorization of a number"),
            (POWER, "Calculate the power of a base number"),
            (SQRT, "Calculate the square root of a number"),
            (GCD, "Find the greatest common divisor of two numbers"),
            (LCM, "Find the least common multiple of two numbers"),
            (FIBONACCI, "Calculate the nth number in the Fibonacci sequence"),
            (FACTORIAL, "Calculate the factorial of a non-negative integer"),
        ],
    )


def number_theory_menu():
    while True:
        nt_option = print_number_theory_menu()
        if nt_option == PRIME:
            not_implemented("Primality checks")
        elif nt_option == PRIME_FACTORS:
            not_implemented("Prime factorization")
        elif nt_option == POWER:
            not_implemented("Power calculations")
        elif nt_option == SQRT:
            not_implemented("Square roots")
        elif nt_option == GCD:
            not_implemented("Greatest common divisor")
        elif nt_option == LCM:
            not_implemented("Least common multiple")
        elif nt_option == FIBONACCI:
            not_implemented("Fibonacci sequence")
        elif nt_option == FACTORIAL:
            not_implemented("Factorials")
        elif nt_option == EXIT:
            return
        else:
            print("Invalid option. Please try again.")
