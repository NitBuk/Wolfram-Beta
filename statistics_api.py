# statistics_api.py
##############################################################################
#                                   Imports                                  #
##############################################################################
from statistics_and_probability import *

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
    print("\nStatistics and Probability Menu:")
    print("1: Calculate the mean of a list of numbers")
    print("2: Calculate the median of a list of numbers")
    print("3: Calculate the standard deviation of a list of numbers")
    print("4: Calculate the variance of a list of numbers")
    print("5: Calculate the mode of a list of numbers")
    print("6: Calculate the probability of an event")
    print("7: Calculate the number of combinations of n items taken r at a time")
    print("8: Calculate the number of permutations of n items taken r at a time")
    print("0: Exit")
    sp_option = int(input("Enter an option: "))
    return sp_option


def statistics_and_probability_menu():
    sp_option = print_statistics_and_probability_menu()
    if sp_option == MEAN:
        pass
    elif sp_option == MEDIAN:
        pass
    elif sp_option == DEVIATION:
        pass
    elif sp_option == VARIANCE:
        pass
    elif sp_option == MODE:
        pass
    elif sp_option == PROBABILITY:
        pass
    elif sp_option == COMBINATIONS:
        pass
    elif sp_option == PERMUTATIONS:
        pass
    elif sp_option == EXIT:
        return
    else:
        print("Invalid option. Please try again.")
