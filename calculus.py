# calculus.py

##############################################################################
#                                   Imports                                  #
##############################################################################
from sympy import symbols, limit, diff, sin, integrate, oo, Function, dsolve, Eq, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np

##############################################################################
#                                 CONSTANTS                                  #
##############################################################################
x = symbols('x')


def plot_function_from_string(function_string: str, x_range: tuple) -> bool | None:
    """
    Plots a function given as a string.

    Parameters:
    function_string (str): A string representation of the function to plot.
    x_range (tuple): A tuple specifying the range of x-values for the plot.

    Returns:
    bool: True if the function was plotted successfully, False otherwise.
    """
    try:
        f = sympify(function_string)
        f_lambdified = lambdify(x, f, "numpy")
        x_values = np.linspace(*x_range, 400)
        y_values = f_lambdified(x_values)
        plt.plot(x_values, y_values)
        plt.show()
        return True
    except Exception as e:
        print(f"Error in plotting the function: {e}")
        return False


def calculate_limit(function: str, point: float) -> float | None:
    """
    Calculates the limit of a function at a given point.

    Parameters:
    function (str): The function to calculate the limit of.
    point (float): The point to calculate the limit at.

    Returns:
    float: The calculated limit value or None if an error occurs.
    """
    try:
        return limit(sympify(function), x, point)
    except Exception as e:
        print(f"Error in calculating the limit: {e}")
        return None


def calculate_derivative(function: str) -> str | None:
    """
    Calculates the derivative of a function.

    Parameters:
    function (str): The function to calculate the derivative of.

    Returns:
    str: The derivative of the function as a string or None if an error occurs.
    """
    try:
        return str(diff(sympify(function), x))
    except Exception as e:
        print(f"Error in calculating the derivative: {e}")
        return None


def calculate_integral(function: str) -> str | None:
    """
    Calculates the indefinite integral of a function.

    Parameters:
    function (str): The function to calculate the integral of.

    Returns:
    str: The indefinite integral of the function as a string or None if an error occurs.
    """
    try:
        return str(integrate(sympify(function), x))
    except Exception as e:
        print(f"Error in calculating the integral: {e}")
        return None


def calculate_definite_integral(function: str, a: float, b: float) -> str | None:
    """
    Calculates the definite integral of a function from a to b.

    Parameters:
    function (str): The function to calculate the integral of.
    a, b (float): The limits of integration.

    Returns:
    str: The definite integral of the function as a string or None if an error occurs.
    """
    try:
        return str(integrate(sympify(function), (x, a, b)))
    except Exception as e:
        print(f"Error in calculating the definite integral: {e}")
        return None


def calculate_improper_integral(function: str, a: float) -> float | None:
    """
    Calculates the improper integral of a function from a to infinity.

    Parameters:
    function (str): The function to calculate the integral of.
    a (float): The lower limit of integration.

    Returns:
    float: The calculated improper integral value or None if an error occurs.
    """
    try:
        expr = sympify(function)
        result = integrate(expr, (x, a, oo)).evalf()  # Evaluate the integral numerically
        return float(result)
    except Exception as e:
        print(f"Error in calculating the improper integral: {e}")
        return None


def calculate_double_derivative(function: str) -> str | None:
    """
    Calculates the second derivative of a function.

    Parameters:
    function (str): The function to calculate the second derivative of.

    Returns:
    str: The second derivative of the function as a string or None if an error occurs.
    """
    try:
        return str(diff(sympify(function), x, x))
    except Exception as e:
        print(f"Error in calculating the double derivative: {e}")
        return None
