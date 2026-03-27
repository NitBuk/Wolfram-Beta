"""Interactive menu scaffolding for trigonometry and logarithms."""

from wolfram_beta.menu import not_implemented, render_menu

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
    return render_menu(
        "Trigonometry and Logarithms Menu",
        [
            (SIN, "Calculate the sine of x (x in radians)"),
            (COS, "Calculate the cosine of x (x in radians)"),
            (TAN, "Calculate the tangent of x (x in radians)"),
            (ARC_SIN, "Calculate the arc-sine of x"),
            (ARC_COS, "Calculate the arc cosine of x"),
            (ARC_TAN, "Calculate the arc-tangent of x"),
            (LN, "Calculate the natural logarithm of x"),
            (LOG2, "Calculate the base-2 logarithm of x"),
            (EXP, "Calculate e raised to the power x"),
        ],
    )


def trigo_and_log_menu():
    while True:
        tl_option = print_trigo_and_log_menu()
        if tl_option == SIN:
            not_implemented("Sine")
        elif tl_option == COS:
            not_implemented("Cosine")
        elif tl_option == TAN:
            not_implemented("Tangent")
        elif tl_option == ARC_SIN:
            not_implemented("Arc-sine")
        elif tl_option == ARC_COS:
            not_implemented("Arc-cosine")
        elif tl_option == ARC_TAN:
            not_implemented("Arc-tangent")
        elif tl_option == LN:
            not_implemented("Natural logarithm")
        elif tl_option == LOG2:
            not_implemented("Base-2 logarithm")
        elif tl_option == EXP:
            not_implemented("Exponential")
        elif tl_option == EXIT:
            return
        else:
            print("Invalid option. Please try again.")
