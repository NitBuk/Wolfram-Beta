# linear_algebra.py

##############################################################################
#                                   Imports                                  #
##############################################################################
import numpy as np
from numpy import ndarray
from typing import Union, Tuple


def solve_linear(A: np.ndarray, b: np.ndarray) -> np.ndarray | None:
    """
    Solves a system of linear equations.

    Parameters:
    A (numpy.ndarray): Coefficient matrix.
    b (numpy.ndarray): Constant vector.

    Returns:
    numpy.ndarray: Solution vector.
    """
    try:
        return np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        print("Error: Matrix A is singular.")
        return None
    except ValueError:
        print("Error: Invalid input for linear equation.")
        return None


def solve_quadratic(a: float, b: float, c: float) -> Union[str, Tuple[float, float], float]:
    """
    Solves a quadratic equation ax^2 + bx + c = 0.

    Parameters:
    a, b, c (float): Coefficients of the quadratic equation.

    Returns:
    Union[str, Tuple[float, float]]: Real solutions of the quadratic equation.
    """
    disc = b ** 2 - 4 * a * c
    if disc < 0:
        return "No real solutions"
    elif disc == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + np.sqrt(disc)) / (2 * a)
        root2 = (-b - np.sqrt(disc)) / (2 * a)
        return root1, root2


def add_matrices(m1: np.ndarray, m2: np.ndarray) -> np.ndarray | None:
    """
    Adds two matrices.

    Parameters:
    m1, m2 (numpy.ndarray): Matrices to be added.

    Returns:
    numpy.ndarray: Result of the addition.
    """
    try:
        return np.add(m1, m2)
    except ValueError:
        print("Error: Matrices must have the same dimensions.")
        return None


def subtract_matrices(m1: np.ndarray, m2: np.ndarray) -> np.ndarray | None:
    """
    Subtracts two matrices.

    Parameters:
    m1, m2 (numpy.ndarray): Matrices to be subtracted.

    Returns:
    numpy.ndarray: Result of the subtraction.
    """
    try:
        return np.subtract(m1, m2)
    except ValueError:
        print("Error: Matrices must have the same dimensions.")
        return None


def scalar_multiply(scalar: float, matrix: np.ndarray) -> np.ndarray | None:
    """
    Multiplies a matrix by a scalar.

    Parameters:
    scalar (float): Scalar to multiply the matrix by.
    matrix (numpy.ndarray): Matrix to be multiplied.

    Returns:
    numpy.ndarray: Result of the multiplication.
    """
    try:
        return np.multiply(scalar, matrix)
    except ValueError:
        print("Error: Invalid input for scalar multiplication.")
        return None


def multiply_matrices(m1: np.ndarray, m2: np.ndarray) -> np.ndarray | None:
    """
    Multiplies two matrices.

    Parameters:
    m1, m2 (numpy.ndarray): Matrices to be multiplied.

    Returns:
    numpy.ndarray: Result of the multiplication.
    """
    try:
        return np.matmul(m1, m2)
    except ValueError:
        print("Error: Matrices are not compatible for multiplication.")
        return None


def determinant(matrix: np.ndarray) -> float | None:
    """
    Calculates the determinant of a matrix.

    Parameters:
    matrix (numpy.ndarray): Matrix whose determinant is to be calculated.

    Returns:
    float: Determinant of the matrix.
    """
    try:
        return np.linalg.det(matrix)
    except np.linalg.LinAlgError:
        print("Error: Matrix must be square.")
        return None
    except ValueError:
        print("Error: Invalid input for determinant calculation.")
        return None


def is_symmetric(matrix: np.ndarray) -> bool | None:
    """
    Checks if a matrix is symmetric.

    Parameters:
    matrix (numpy.ndarray): Matrix to be checked.

    Returns:
    bool: True if the matrix is symmetric, False otherwise.
    """
    try:
        return np.array_equal(matrix, matrix.T)
    except ValueError:
        print("Error: Invalid input for symmetry check.")
        return None


def inverse(matrix: np.ndarray) -> np.ndarray | None:
    """
    Calculates the inverse of a matrix.

    Parameters:
    matrix (numpy.ndarray): Matrix to be inverted.

    Returns:
    numpy.ndarray: Inverse of the matrix.
    """
    try:
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        print("Error: Matrix must be square and invertible.")
        return None
    except ValueError:
        print("Error: Invalid input for inverse calculation.")
        return None


def eigen(matrix: np.ndarray) -> Union[Tuple[np.ndarray, np.ndarray], None]:
    """
    Calculates the eigenvalues and eigenvectors of a matrix.

    Parameters:
    matrix (numpy.ndarray): Matrix to calculate eigenvalues and eigenvectors of.

    Returns:
    Union[Tuple[np.ndarray, np.ndarray], None]: A tuple containing a numpy.ndarray of eigenvalues and a 2D
    numpy.ndarray of the corresponding eigenvectors.
    """
    try:
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        return eigenvalues, eigenvectors
    except np.linalg.LinAlgError:
        print("Error: Matrix must be square.")
        return None
    except ValueError:
        print("Error: Invalid input for eigenvalue and eigenvector calculation.")
        return None


def transpose(matrix: np.ndarray) -> np.ndarray | None:
    """
    Calculates the transpose of a matrix.

    Parameters:
    matrix (numpy.ndarray): Matrix to be transposed.

    Returns:
    numpy.ndarray: Transpose of the matrix.
    """
    try:
        return np.transpose(matrix)
    except ValueError:
        print("Error: Invalid input for transpose calculation.")
        return None


def trace(matrix: np.ndarray) -> ndarray | None:
    """
    Calculates the trace of a matrix.

    Parameters:
    matrix (numpy.ndarray): Matrix to calculate the trace of.

    Returns:
    float: Trace of the matrix.
    """
    try:
        return np.trace(matrix)
    except ValueError:
        print("Error: Invalid input for trace calculation.")
        return None


def rank(matrix: np.ndarray) -> int | None:
    """
    Calculates the rank of a matrix.

    Parameters:
    matrix (numpy.ndarray): Matrix to calculate the rank of.

    Returns:
    int: Rank of the matrix.
    """
    try:
        return np.linalg.matrix_rank(matrix)
    except ValueError:
        print("Error: Invalid input for rank calculation.")
        return None
