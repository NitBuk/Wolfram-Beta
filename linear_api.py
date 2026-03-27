"""Interactive menu scaffolding for linear algebra helpers."""

import numpy as np

from linear_algebra import solve_linear, solve_quadratic
from wolfram_beta.menu import not_implemented, prompt_float, prompt_int, render_menu

##############################################################################
#                                 CONSTANTS                                  #
##############################################################################

LINEAR_EQUATION = 1
QUADRATIC_EQUATION = 2
ADD_MATRICES = 3
SUBTRACT_MATRICES = 4
MULTIPLY_MATRIX_BY_SCALAR = 5
MULTIPLY_MATRICES = 6
MATRIX_RANK = 7
MATRIX_SYMMETRIC = 8
MATRIX_INVERSE = 9
MATRIX_TRANSPOSE = 10
MATRIX_TRACE = 11
MATRIX_DETERMINANT = 12
EIGENVALUES_AND_EIGENVECTORS = 13
EXIT = 0


def print_linear_menu() -> int:
    return render_menu(
        "Linear Algebra Menu",
        [
            (LINEAR_EQUATION, "Solve a linear equation"),
            (QUADRATIC_EQUATION, "Solve a quadratic equation"),
            (ADD_MATRICES, "Add two matrices"),
            (SUBTRACT_MATRICES, "Subtract two matrices"),
            (MULTIPLY_MATRIX_BY_SCALAR, "Multiply a matrix by a scalar"),
            (MULTIPLY_MATRICES, "Multiply two matrices"),
            (MATRIX_RANK, "Calculate the rank of a matrix"),
            (MATRIX_SYMMETRIC, "Check if a matrix is symmetric"),
            (MATRIX_INVERSE, "Calculate the inverse of a matrix"),
            (MATRIX_TRANSPOSE, "Calculate the transpose of a matrix"),
            (MATRIX_TRACE, "Calculate the trace of a matrix"),
            (MATRIX_DETERMINANT, "Calculate the determinant of a matrix"),
            (EIGENVALUES_AND_EIGENVECTORS, "Calculate the eigenvalues and eigenvectors of a matrix"),
        ],
    )


def get_float_input(prompt: str) -> float:
    """
    Get a float input from the user.

    Parameters:
    prompt (str): Prompt message to be displayed to the user.

    Returns:
    float: User input converted to float.
    """
    return prompt_float(prompt)


def get_int_input(prompt: str) -> int:
    """
    Get an integer input from the user.

    Parameters:
    prompt (str): Prompt message to be displayed to the user.

    Returns:
    int: User input converted to integer.
    """
    return prompt_int(prompt)


def get_vector_input() -> np.ndarray | None:
    """
    Get a vector input from the user.

    Returns:
    numpy.ndarray: User input converted to a numpy array.
    """
    while True:
        try:
            values = list(map(float, input("Enter the vector elements separated by spaces: ").split()))
            if not values:
                raise ValueError
            return np.array(values)
        except ValueError:
            print("Invalid input. Please enter a sequence of numbers separated by spaces.")
            return None


def get_matrix_input() -> np.ndarray | None:
    """
    Get a matrix input from the user.

    Returns:
    numpy.ndarray: User input converted to a numpy array.
    """
    while True:
        try:
            rows = prompt_int("Enter the number of rows in the matrix: ")
            if rows <= 0:
                raise ValueError
            matrix_rows = []
            for i in range(rows):
                row_values = list(map(float, input(f"Enter the elements of row {i + 1} separated by spaces: ").split()))
                if not row_values:
                    raise ValueError
                matrix_rows.append(row_values)

            row_lengths = {len(row) for row in matrix_rows}
            if len(row_lengths) != 1:
                raise ValueError
            return np.array(matrix_rows)
        except ValueError:
            print("Invalid input. Please enter a sequence of numbers separated by spaces for each row.")
            return None


def get_input_and_solve_quadratic() -> bool:
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return False

    solution = solve_quadratic(a, b, c)

    if isinstance(solution, str):
        print(solution)
    elif isinstance(solution, tuple):
        print(f"The solutions are {solution[0]} and {solution[1]}")
    else:
        print(f"The solution is {solution}")
    return True


def get_input_and_solve_linear() -> bool:
    A = get_matrix_input()
    b = get_vector_input()
    if A is None or b is None:
        return False

    solution = solve_linear(A, b)
    if solution is not None:
        print(f"The solution is {solution}")
        return True
    else:
        return False


def linear_menu():
    while True:
        la_option = print_linear_menu()
        if la_option == LINEAR_EQUATION:
            get_input_and_solve_linear()
        elif la_option == QUADRATIC_EQUATION:
            get_input_and_solve_quadratic()
        elif la_option == ADD_MATRICES:
            not_implemented("Matrix addition")
        elif la_option == SUBTRACT_MATRICES:
            not_implemented("Matrix subtraction")
        elif la_option == MULTIPLY_MATRIX_BY_SCALAR:
            not_implemented("Scalar multiplication")
        elif la_option == MULTIPLY_MATRICES:
            not_implemented("Matrix multiplication")
        elif la_option == MATRIX_RANK:
            not_implemented("Matrix rank")
        elif la_option == MATRIX_SYMMETRIC:
            not_implemented("Symmetry checks")
        elif la_option == MATRIX_INVERSE:
            not_implemented("Matrix inversion")
        elif la_option == MATRIX_TRANSPOSE:
            not_implemented("Transpose")
        elif la_option == MATRIX_TRACE:
            not_implemented("Trace")
        elif la_option == MATRIX_DETERMINANT:
            not_implemented("Determinant")
        elif la_option == EIGENVALUES_AND_EIGENVECTORS:
            not_implemented("Eigenvalue decomposition")
        elif la_option == EXIT:
            return
        else:
            print("Invalid option. Please try again.")
