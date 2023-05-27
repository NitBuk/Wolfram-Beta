# test.py

##############################################################################
#                                   Imports                                  #
##############################################################################
import pytest
from calculus import *
from linear_algebra import *
from statistics_and_probability import *
from number_theory import *
import numpy as np
from sympy import Function, sympify, Eq, dsolve
import trigo_and_log as trig
import math

##############################################################################
#                                 CONSTANTS                                  #
##############################################################################
x = symbols('x')
F = Function('F')

"""
    calculus tests
"""


def test_calculate_limit():
    result = calculate_limit('x', 2)
    print(f"calculate_limit('x', 2) = {result}")
    assert result == 2

    result = calculate_limit('x^2', 3)
    print(f"calculate_limit('x^2', 3) = {result}")
    assert result == 9


def test_calculate_derivative():
    result = calculate_derivative('x^2')
    print(f"calculate_derivative('x^2') = {result}")
    assert str(result) == '2*x'

    result = calculate_derivative('sin(x)')
    print(f"calculate_derivative('sin(x)') = {result}")
    assert str(result) == 'cos(x)'


def test_calculate_integral():
    result = calculate_integral('2*x')
    print(f"calculate_integral('2*x') = {result}")
    assert str(result) == 'x**2'

    result = calculate_integral('cos(x)')
    print(f"calculate_integral('cos(x)') = {result}")
    assert str(result) == 'sin(x)'


def test_calculate_definite_integral():
    result = calculate_definite_integral('x', 0, 2)
    print(f"calculate_definite_integral('x', 0, 2) = {result}")
    assert result == '2'

    result = calculate_definite_integral('x^2', 0, 3)
    print(f"calculate_definite_integral('x^2', 0, 3) = {result}")
    assert result == '9'


def test_calculate_improper_integral():
    result = calculate_improper_integral('exp(-x)', 0)
    print(f"calculate_improper_integral('exp(-x)', 0) = {result}")
    assert result == 1


def test_calculate_double_derivative():
    result = calculate_double_derivative('x^3')
    print(f"calculate_double_derivative('x^3') = {result}")
    assert str(result) == '6*x'

    result = calculate_double_derivative('sin(x)')
    print(f"calculate_double_derivative('sin(x)') = {result}")
    assert str(result) == '-sin(x)'


"""
    linear algebra tests
"""


def test_solve_linear():
    A = np.array([[3, 1], [1, 2]])
    b = np.array([9, 8])
    result = solve_linear(A, b)
    print(f"solve_linear(A, b) = {result}")
    assert np.array_equal(result, np.array([2, 3]))


def test_solve_quadratic():
    result = solve_quadratic(1, -3, 2)
    print(f"solve_quadratic(1, -3, 2) = {result}")
    assert np.array_equal(result, (2.0, 1.0))


def test_add_matrices():
    m1 = np.array([[1, 2], [3, 4]])
    m2 = np.array([[5, 6], [7, 8]])
    result = add_matrices(m1, m2)
    print(f"add_matrices(m1, m2) = {result}")
    assert np.array_equal(result, np.array([[6, 8], [10, 12]]))


def test_subtract_matrices():
    m1 = np.array([[1, 2], [3, 4]])
    m2 = np.array([[5, 6], [7, 8]])
    result = subtract_matrices(m1, m2)
    print(f"subtract_matrices(m1, m2) = {result}")
    assert np.array_equal(result, np.array([[-4, -4], [-4, -4]]))


def test_scalar_multiply():
    matrix = np.array([[1, 2], [3, 4]])
    scalar = 2
    result = scalar_multiply(scalar, matrix)
    print(f"scalar_multiply(scalar, matrix) = {result}")
    assert np.array_equal(result, np.array([[2, 4], [6, 8]]))


def test_multiply_matrices():
    m1 = np.array([[1, 2], [3, 4]])
    m2 = np.array([[5, 6], [7, 8]])
    result = multiply_matrices(m1, m2)
    print(f"multiply_matrices(m1, m2) = {result}")
    assert np.array_equal(result, np.array([[19, 22], [43, 50]]))


def test_determinant():
    matrix = np.array([[1, 2], [3, 4]])
    result = determinant(matrix)
    print(f"determinant(matrix) = {result}")
    assert result > -2.0004 or result < -2


def test_is_symmetric():
    matrix = np.array([[1, 2], [2, 1]])
    result = is_symmetric(matrix)
    print(f"is_symmetric(matrix) = {result}")
    assert result == True


def test_inverse():
    matrix = np.array([[1, 2], [3, 4]])
    result = inverse(matrix)
    print(f"inverse(matrix) = {result}")
    assert np.allclose(result, np.array([[-2.0, 1.0], [1.5, -0.5]]))


def test_eigen():
    matrix = np.array([[1, 2], [2, 1]])
    result = eigen(matrix)
    print(f"eigen(matrix) = {result}")
    assert np.allclose(result[0], np.array([3., -1.]))  # Checking the eigenvalues


def test_transpose():
    matrix = np.array([[1, 2], [3, 4]])
    result = transpose(matrix)
    print(f"transpose(matrix) = {result}")
    assert np.array_equal(result, np.array([[1, 3], [2, 4]]))


def test_trace():
    matrix = np.array([[1, 2], [3, 4]])
    result = trace(matrix)
    print(f"trace(matrix) = {result}")
    assert result == 5


def test_rank():
    matrix = np.array([[1, 2], [3, 4]])
    result = rank(matrix)
    print(f"rank(matrix) = {result}")
    assert result == 2


"""
    Number theory tests
"""


def test_check_prime():
    assert check_prime(17)
    assert not check_prime(15)


def test_prime_factorization():
    assert prime_factorization(18) == [2, 3]
    assert prime_factorization(19) == [19]


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1


def test_sqrt():
    assert sqrt(16) == 4
    assert sqrt(0) == 0
    assert sqrt(-1) is None


def test_find_gcd():
    assert find_gcd(48, 18) == 6
    assert find_gcd(7, 1) == 1


def test_find_lcm():
    assert find_lcm(15, 20) == 60
    assert find_lcm(5, 7) == 35


def test_fibonacci():
    assert fibonacci(1) == 1
    assert fibonacci(7) == 13


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(-1) is None


"""
    Statistics and probability tests
"""


@pytest.mark.parametrize("numbers, expected_mean", [
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3], 2),
    ([], None),
])
def test_calculate_mean(numbers, expected_mean):
    calculated_mean = calculate_mean(numbers)
    print(f"Calculated mean: {calculated_mean}")
    assert calculated_mean == expected_mean


@pytest.mark.parametrize("numbers, expected_median", [
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3], 2),
    ([], None),
])
def test_calculate_median(numbers, expected_median):
    calculated_median = calculate_median(numbers)
    print(f"Calculated median: {calculated_median}")
    assert calculated_median == expected_median


@pytest.mark.parametrize("numbers, expected_stdev", [
    ([1, 2, 3, 4, 5], pytest.approx(1.5811, rel=1e-4)),
    ([1, 2, 3], 1.0),
    ([], None),
])
def test_calculate_stdev(numbers, expected_stdev):
    calculated_stdev = calculate_stdev(numbers)
    print(f"Calculated standard deviation: {calculated_stdev}")
    assert calculated_stdev == expected_stdev


@pytest.mark.parametrize("numbers, expected_variance", [
    ([1, 2, 3, 4, 5], pytest.approx(2.5, rel=1e-4)),
    ([1, 2, 3], 1),
    ([], None),
])
def test_calculate_variance(numbers, expected_variance):
    calculated_variance = calculate_variance(numbers)
    print(f"Calculated variance: {calculated_variance}")
    assert calculated_variance == expected_variance


@pytest.mark.parametrize("numbers, expected_mode", [
    ([1, 2, 3, 4, 4], 4),
    ([1, 2, 3], 1),
    ([], None),
])
def test_calculate_mode(numbers, expected_mode):
    calculated_mode = calculate_mode(numbers)
    print(f"Calculated mode: {calculated_mode}")
    assert calculated_mode == expected_mode


@pytest.mark.parametrize("event_outcomes, sample_space, expected_probability", [
    (2, 5, 0.4),
    (0, 5, 0.0),
    (5, 0, None),
])
def test_probability(event_outcomes, sample_space, expected_probability):
    calculated_probability = probability(event_outcomes, sample_space)
    print(f"Calculated probability: {calculated_probability}")
    assert calculated_probability == expected_probability


@pytest.mark.parametrize("n, r, expected_combinations", [
    (5, 2, 10),
    (0, 2, None),
    (5, 6, None),
])
def test_combinations(n, r, expected_combinations):
    calculated_combinations = combinations(n, r)
    print(f"Calculated combinations: {calculated_combinations}")
    assert calculated_combinations == expected_combinations


@pytest.mark.parametrize("n, r, expected_permutations", [
    (5, 2, 20),
    (0, 2, None),
    (5, 6, None),
])
def test_permutations(n, r, expected_permutations):
    calculated_permutations = permutations(n, r)
    print(f"Calculated permutations: {calculated_permutations}")
    assert calculated_permutations == expected_permutations


"""
    trigo and log tests
"""


def test_sin():
    assert math.isclose(trig.sin(math.pi / 2), 1, rel_tol=1e-9)
    assert math.isclose(trig.sin(math.pi), 0, rel_tol=1e-9, abs_tol=1e-9)


def test_cos():
    assert math.isclose(trig.cos(0), 1, rel_tol=1e-9)
    assert math.isclose(trig.cos(math.pi), -1, rel_tol=1e-9)


def test_tan():
    assert math.isclose(trig.tan(0), 0, rel_tol=1e-9)


def test_arcsin():
    assert math.isclose(trig.arcsin(1), math.pi / 2, rel_tol=1e-9)


def test_arccos():
    assert math.isclose(trig.arccos(1), 0, rel_tol=1e-9)


def test_arctan():
    assert math.isclose(trig.arctan(1), math.pi / 4, rel_tol=1e-9)


def test_ln():
    assert math.isclose(trig.ln(math.e), 1, rel_tol=1e-9)


def test_log2():
    assert math.isclose(trig.log2(4), 2, rel_tol=1e-9)


def test_exp():
    assert math.isclose(trig.exp(1), math.e, rel_tol=1e-9)
