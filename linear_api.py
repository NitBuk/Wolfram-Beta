# linear_api.py

##############################################################################
#                                   Imports                                  #
##############################################################################
from linear_algebra import *

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
    print("\nLinear Algebra Menu:")
    print("1: Solve a linear equation")
    print("2: Solve a quadratic equation")
    print("3: Add two matrices")
    print("4: Subtract two matrices")
    print("5: Multiply a matrix by a scalar")
    print("6: Multiply two matrices")
    print("7: Calculates the rank of a matrix")
    print("8: Check if a matrix is symmetric")
    print("9: Calculate the inverse of a matrix")
    print("10: Calculate the transpose of a matrix")
    print("11: Calculate the trace of a matrix")
    print("12: Calculate the determinant of a matrix")
    print("13: Calculate the eigenvalues and eigenvectors of a matrix")
    print("0: Exit")
    la_option = int(input("Enter an option: "))
    return la_option


def get_float_input(prompt: str) -> float:
    """
    Get a float input from the user.

    Parameters:
    prompt (str): Prompt message to be displayed to the user.

    Returns:
    float: User input converted to float.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_int_input(prompt: str) -> int:
    """
    Get an integer input from the user.

    Parameters:
    prompt (str): Prompt message to be displayed to the user.

    Returns:
    int: User input converted to integer.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_vector_input() -> np.ndarray | None:
    """
    Get a vector input from the user.

    Returns:
    numpy.ndarray: User input converted to a numpy array.
    """
    while True:
        try:
            return np.array(list(map(float, input("Enter the vector elements separated by spaces: ").split())))
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
            rows = int(input("Enter the number of rows in the matrix: "))
            if rows <= 0:
                raise ValueError
            return np.array(
                [list(map(float, input(f"Enter the elements of row {i + 1} separated by spaces: ").split())) for i in
                 range(rows)])
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
    try:
        A = get_matrix_input()
        b = get_vector_input()

    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return False

    solution = solve_linear(A, b)
    if solution is not None:
        print(f"The solution is {solution}")
        return True
    else:
        return False


def linear_menu():
    la_option = print_linear_menu()
    if la_option == LINEAR_EQUATION:
        get_input_and_solve_linear()
    elif la_option == QUADRATIC_EQUATION:
        get_input_and_solve_quadratic()
    elif la_option == ADD_MATRICES:
        pass
    elif la_option == SUBTRACT_MATRICES:
        pass
    elif la_option == MULTIPLY_MATRIX_BY_SCALAR:
        pass
    elif la_option == MULTIPLY_MATRICES:
        pass
    elif la_option == MATRIX_RANK:
        pass
    elif la_option == MATRIX_SYMMETRIC:
        pass
    elif la_option == MATRIX_INVERSE:
        pass
    elif la_option == MATRIX_TRANSPOSE:
        pass
    elif la_option == MATRIX_TRACE:
        pass
    elif la_option == MATRIX_DETERMINANT:
        pass
    elif la_option == EIGENVALUES_AND_EIGENVECTORS:
        pass
    elif la_option == EXIT:
        return
    else:
        print("Invalid option. Please try again.")
