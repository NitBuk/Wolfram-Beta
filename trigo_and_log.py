"""Pure trigonometry and logarithm helpers used by the Wolfram Beta toolkit."""

import math
from typing import Union


def _call_math(func, value: Union[int, float], error_message: str) -> float | None:
    try:
        return func(value)
    except (TypeError, ValueError):
        print(error_message)
        return None


# Trigonometric Functions
def sin(x: Union[int, float]) -> float | None:
    """
    Returns the sine of x (x in radians).
    """
    return _call_math(math.sin, x, "Input must be an integer or a float.")


def cos(x: Union[int, float]) -> float | None:
    """
    Returns the cosine of x (x in radians).
    """
    return _call_math(math.cos, x, "Input must be an integer or a float.")


def tan(x: Union[int, float]) -> float | None:
    """
    Returns the tangent of x (x in radians).
    """
    return _call_math(math.tan, x, "Input must be an integer or a float.")


def arcsin(x: Union[int, float]) -> float | None:
    """
    Returns the arc-sine of x.
    """
    return _call_math(math.asin, x, "Input must be an integer or a float.")


def arccos(x: Union[int, float]) -> float | None:
    """
    Returns the arc cosine of x.
    """
    return _call_math(math.acos, x, "Input must be an integer or a float.")


def arctan(x: Union[int, float]) -> float | None:
    """
    Returns the arc-tangent of x.
    """
    return _call_math(math.atan, x, "Input must be an integer or a float.")


# Logarithmic and Exponential Functions
def ln(x: Union[int, float]) -> float | None:
    """
    Returns the natural logarithm of x.
    """
    return _call_math(math.log, x, "Input must be an integer or a float.")


def log2(x: Union[int, float]) -> float | None:
    """
    Returns the base-2 logarithm of x.
    """
    return _call_math(math.log2, x, "Input must be an integer or a float.")


def exp(x: Union[int, float]) -> float | None:
    """
    Returns e raised to the power x.
    """
    return _call_math(math.exp, x, "Input must be an integer or a float.")
