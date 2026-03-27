"""Interactive menu scaffolding for statistics and probability helpers."""

from wolfram_beta.menu import not_implemented, render_menu

##############################################################################
#                                 CONSTANTS                                  #
##############################################################################
MEAN = 1
MEDIAN = 2
DEVIATION = 3
VARIANCE = 4
MODE = 5
PROBABILITY = 6
COMBINATIONS = 7
PERMUTATIONS = 8
EXIT = 0


def print_statistics_and_probability_menu() -> int:
    return render_menu(
        "Statistics and Probability Menu",
        [
            (MEAN, "Calculate the mean of a list of numbers"),
            (MEDIAN, "Calculate the median of a list of numbers"),
            (DEVIATION, "Calculate the standard deviation of a list of numbers"),
            (VARIANCE, "Calculate the variance of a list of numbers"),
            (MODE, "Calculate the mode of a list of numbers"),
            (PROBABILITY, "Calculate the probability of an event"),
            (COMBINATIONS, "Calculate the number of combinations of n items taken r at a time"),
            (PERMUTATIONS, "Calculate the number of permutations of n items taken r at a time"),
        ],
    )


def statistics_and_probability_menu():
    while True:
        sp_option = print_statistics_and_probability_menu()
        if sp_option == MEAN:
            not_implemented("Means")
        elif sp_option == MEDIAN:
            not_implemented("Medians")
        elif sp_option == DEVIATION:
            not_implemented("Standard deviation")
        elif sp_option == VARIANCE:
            not_implemented("Variance")
        elif sp_option == MODE:
            not_implemented("Mode")
        elif sp_option == PROBABILITY:
            not_implemented("Probability")
        elif sp_option == COMBINATIONS:
            not_implemented("Combinations")
        elif sp_option == PERMUTATIONS:
            not_implemented("Permutations")
        elif sp_option == EXIT:
            return
        else:
            print("Invalid option. Please try again.")
