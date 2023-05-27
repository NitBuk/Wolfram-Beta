# trigo_and_log.py

##############################################################################
#                                   Imports                                  #
##############################################################################
import math
from typing import Union


# Trigonometric Functions
def sin(x: Union[int, float]) -> float | None:
    """
    Returns the sine of x (x in radians).
    """
    try:
        return math.sin(x)
    except TypeError:
        print("Input must be an integer or a float.")
        return None


def cos(x: Union[int, float]) -> float | None:
    """
    Returns the cosine of x (x in radians).
    """
    try:
        return math.cos(x)
    except TypeError:
        print("Input must be an integer or a float.")
        return None


def tan(x: Union[int, float]) -> float | None:
    """
    Returns the tangent of x (x in radians).
    """
    try:
        return math.tan(x)
    except TypeError:
        print("Input must be an integer or a float.")
        return None


def arcsin(x: Union[int, float]) -> float | None:
    """
    Returns the arc-sine of x.
    """
    try:
        return math.asin(x)
    except TypeError:
        print("Input must be an integer or a float.")
        return None


def arccos(x: Union[int, float]) -> float | None:
    """
    Returns the arc cosine of x.
    """
    try:
        return math.acos(x)
    except TypeError:
        print("Input must be an integer or a float.")
        return None


def arctan(x: Union[int, float]) -> float | None:
    """
    Returns the arc-tangent of x.
    """
    try:
        return math.atan(x)
    except TypeError:
        print("Input must be an integer or a float.")
        return None


# Logarithmic and Exponential Functions
def ln(x: Union[int, float]) -> float | None:
    """
    Returns the natural logarithm of x.
    """
    try:
        return math.log(x)
    except TypeError:
        print("Input must be an integer or a float.")
        return None


def log2(x: Union[int, float]) -> float | None:
    """
    Returns the base-2 logarithm of x.
    """
    try:
        return math.log2(x)
    except TypeError:
        print("Input must be an integer or a float.")
        return None


def exp(x: Union[int, float]) -> float | None:
    """
    Returns e raised to the power x.
    """
    try:
        return math.exp(x)
    except TypeError:
        print("Input must be an integer or a float.")
        return None
