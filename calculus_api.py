"""Interactive menu scaffolding for calculus helpers."""

from wolfram_beta.menu import not_implemented, render_menu

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
    return render_menu(
        "Calculus Menu",
        [
            (PLOT, "Plot a function"),
            (LIMIT, "Calculate the limit of a function at a given point"),
            (DERIVATIVE, "Calculate the derivative of a function"),
            (INDEFINITE_INTEGRAL, "Calculate the indefinite integral of a function"),
            (DEFINITE_INTEGRAL, "Calculate the definite integral of a function from a to b"),
            (IMPROPER_INTEGRAL, "Calculate the improper integral of a function from a to infinity"),
            (SECOND_DERIVATIVE, "Calculate the second derivative of a function"),
        ],
    )


def calculus_menu():
    while True:
        calc_option = print_calculus_menu()
        if calc_option == PLOT:
            not_implemented("Plotting")
        elif calc_option == LIMIT:
            not_implemented("Limits")
        elif calc_option == DERIVATIVE:
            not_implemented("Derivatives")
        elif calc_option == INDEFINITE_INTEGRAL:
            not_implemented("Indefinite integrals")
        elif calc_option == DEFINITE_INTEGRAL:
            not_implemented("Definite integrals")
        elif calc_option == IMPROPER_INTEGRAL:
            not_implemented("Improper integrals")
        elif calc_option == SECOND_DERIVATIVE:
            not_implemented("Second derivatives")
        elif calc_option == EXIT:
            return
        else:
            print("Invalid option. Please try again.")
