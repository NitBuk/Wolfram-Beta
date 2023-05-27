# statistics_and_probability.py
##############################################################################
#                                   Imports                                  #
##############################################################################
from statistics import mean, median, stdev, variance, mode, StatisticsError
import math
from typing import List, Union


def calculate_mean(numbers: List[Union[int, float]]) -> float | None:
    """
    Calculate the mean of a list of numbers.

    Parameters:
    numbers (list): List of numbers.

    Returns:
    float: The mean of the numbers. Returns None if input is not a non-empty list.
    """
    if not isinstance(numbers, list) or not numbers:
        print("Error: Input must be a non-empty list.")
        return None
    return mean(numbers)


def calculate_median(numbers: List[Union[int, float]]) -> float | None:
    """
    Calculate the median of a list of numbers.

    Parameters:
    numbers (list): List of numbers.

    Returns:
    float: The median of the numbers. Returns None if input is not a non-empty list.
    """
    if not isinstance(numbers, list) or not numbers:
        print("Error: Input must be a non-empty list.")
        return None
    return median(numbers)


def calculate_stdev(numbers: List[Union[int, float]]) -> float | None:
    """
    Calculate the standard deviation of a list of numbers.

    Parameters:
    numbers (list): List of numbers.

    Returns:
    float: The standard deviation of the numbers. Returns None if input is not a non-empty list.
    """
    if not isinstance(numbers, list) or not numbers:
        print("Error: Input must be a non-empty list.")
        return None
    return stdev(numbers)


def calculate_variance(numbers: List[Union[int, float]]) -> float | None:
    """
    Calculate the variance of a list of numbers.

    Parameters:
    numbers (list): List of numbers.

    Returns:
    float: The variance of the numbers. Returns None if input is not a non-empty list.
    """
    if not isinstance(numbers, list) or not numbers:
        print("Error: Input must be a non-empty list.")
        return None
    return variance(numbers)


def calculate_mode(numbers: List[Union[int, float]]) -> float | None:
    """
    Calculate the mode of a list of numbers.

    Parameters:
    numbers (list): List of numbers.

    Returns:
    float: The mode of the numbers. Returns None if input is not a non-empty list or if the list does not have a mode.
    """
    if not isinstance(numbers, list) or not numbers:
        print("Error: Input must be a non-empty list.")
        return None
    try:
        return mode(numbers)
    except StatisticsError:
        print("Error: The list does not have a mode.")
        return None


def probability(event_outcomes: int, sample_space: int) -> float | None:
    """
    Calculate the probability of an event.

    The probability of an event is calculated as the ratio of the number of outcomes in which the
    event occurs to the total number of outcomes in the sample space.

    Parameters:
    event_outcomes (int): Number of outcomes in which the event occurs.
    sample_space (int): Total number of outcomes in the sample space.

    Returns:
    float: The probability of the event. Returns None if sample_space is zero.
    """
    try:
        return event_outcomes / sample_space
    except ZeroDivisionError:
        print("Error: The sample space cannot be zero.")
        return None


def combinations(n: int, r: int) -> float | None:
    """
    Calculate the number of combinations of n items taken r at a time.

    Parameters:
    n (int): Total number of items.
    r (int): Number of items to choose.

    Returns:
    int: The number of combinations or None if invalid parameters.
    """
    try:
        return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
    except ValueError:
        print("Error: n and r should be non-negative integers, and n should be greater than or equal to r.")
        return None


def permutations(n: int, r: int) -> float | None:
    """
    Calculate the number of permutations of n items taken r at a time.

    Parameters:
    n (int): Total number of items.
    r (int): Number of items to choose.

    Returns:
    int: The number of permutations or None if invalid parameters.
    """
    try:
        return math.factorial(n) / math.factorial(n - r)
    except ValueError:
        print("Error: n and r should be non-negative integers, and n should be greater than or equal to r.")
        return None
