"""Pure statistics and probability helpers used by the Wolfram Beta toolkit."""

from collections.abc import Sequence
from numbers import Real
from statistics import StatisticsError, mean, median, mode, stdev, variance
import math
from typing import List, Union


def _validate_numbers(numbers: Sequence[Union[int, float]] | None) -> list[Union[int, float]] | None:
    if not isinstance(numbers, Sequence) or not numbers:
        print("Error: Input must be a non-empty sequence of numbers.")
        return None
    values = list(numbers)
    if any(not isinstance(value, Real) or isinstance(value, bool) for value in values):
        print("Error: Input must contain only numbers.")
        return None
    return values


def calculate_mean(numbers: List[Union[int, float]]) -> float | None:
    """
    Calculate the mean of a list of numbers.

    Parameters:
    numbers (list): List of numbers.

    Returns:
    float: The mean of the numbers. Returns None if input is not a non-empty list.
    """
    validated_numbers = _validate_numbers(numbers)
    if validated_numbers is None:
        return None
    return mean(validated_numbers)


def calculate_median(numbers: List[Union[int, float]]) -> float | None:
    """
    Calculate the median of a list of numbers.

    Parameters:
    numbers (list): List of numbers.

    Returns:
    float: The median of the numbers. Returns None if input is not a non-empty list.
    """
    validated_numbers = _validate_numbers(numbers)
    if validated_numbers is None:
        return None
    return median(validated_numbers)


def calculate_stdev(numbers: List[Union[int, float]]) -> float | None:
    """
    Calculate the standard deviation of a list of numbers.

    Parameters:
    numbers (list): List of numbers.

    Returns:
    float: The standard deviation of the numbers. Returns None if input is not a non-empty list.
    """
    validated_numbers = _validate_numbers(numbers)
    if validated_numbers is None:
        return None
    return stdev(validated_numbers)


def calculate_standard_deviation(numbers: List[Union[int, float]]) -> float | None:
    """Alias for `calculate_stdev` with a clearer name."""
    return calculate_stdev(numbers)


def calculate_variance(numbers: List[Union[int, float]]) -> float | None:
    """
    Calculate the variance of a list of numbers.

    Parameters:
    numbers (list): List of numbers.

    Returns:
    float: The variance of the numbers. Returns None if input is not a non-empty list.
    """
    validated_numbers = _validate_numbers(numbers)
    if validated_numbers is None:
        return None
    return variance(validated_numbers)


def calculate_mode(numbers: List[Union[int, float]]) -> float | None:
    """
    Calculate the mode of a list of numbers.

    Parameters:
    numbers (list): List of numbers.

    Returns:
    float: The mode of the numbers. Returns None if input is not a non-empty list or if the list does not have a mode.
    """
    validated_numbers = _validate_numbers(numbers)
    if validated_numbers is None:
        return None
    try:
        return mode(validated_numbers)
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
    except (TypeError, ZeroDivisionError):
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
        return math.comb(n, r)
    except (TypeError, ValueError):
        print(
            "Error: n and r should be non-negative integers, and n should be greater than or equal to r."
        )
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
        return math.perm(n, r)
    except (TypeError, ValueError):
        print(
            "Error: n and r should be non-negative integers, and n should be greater than or equal to r."
        )
        return None
