# number_theory.py

##############################################################################
#                                   Imports                                  #
##############################################################################
import math
from sympy import isprime, primefactors
from math import gcd


def check_prime(n: int) -> bool | None:
    """Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    try:
        return isprime(n)
    except TypeError:
        print("Input must be an integer.")
        return None


def prime_factorization(n: int) -> list | None:
    """Return the prime factorization of a number.

    Args:
        n (int): The number to factorize.

    Returns:
        list: The prime factors of the number.
    """
    try:
        return primefactors(n)
    except TypeError:
        print("Input must be an integer.")
        return None


def power(base: float, exponent: float) -> float | None:
    """Return the power of a base number.

    Args:
        base (float): The base number.
        exponent (float): The exponent.

    Returns:
        float: The result of the power operation.
    """
    try:
        return math.pow(base, exponent)
    except TypeError:
        print("Both base and exponent must be numbers.")
        return None


def sqrt(x: float) -> float | None:
    """Return the square root of a number.

    Args:
        x (float): The number to find the square root of.

    Returns:
        float: The square root of the number.
    """
    try:
        return math.sqrt(x)
    except ValueError:
        print("Input must be a non-negative number.")
        return None


def find_gcd(x: int, y: int) -> int | None:
    """Find the greatest common divisor of two numbers.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The greatest common divisor of the two numbers.
    """
    try:
        return gcd(x, y)
    except TypeError:
        print("Both x and y must be integers.")
        return None


def find_lcm(x: int, y: int) -> int | None:
    """Find the least common multiple of two numbers.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The least common multiple of the two numbers.
    """
    try:
        return abs(x * y) // find_gcd(x, y)
    except TypeError:
        print("Both x and y must be integers.")
        return None


def fibonacci(n: int) -> int | None:
    """Return the nth number in the Fibonacci sequence.

    Args:
        n (int): The position in the Fibonacci sequence to return.

    Returns:
        int: The nth number in the Fibonacci sequence.
    """
    try:
        if n <= 0:
            print("Input must be a positive integer.")
            return None
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return b
    except TypeError:
        print("Input must be an integer.")
        return None


def factorial(n: int) -> int | None:
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    n (int): The non-negative integer.

    Returns:
    int: The factorial of the input.

    Raises:
    ValueError: If the input is a negative integer.

    """
    try:
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")
        return math.factorial(n)
    except ValueError as e:
        print(f"Error: {e}")
        return None
