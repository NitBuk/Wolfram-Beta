import math
import unittest

import numpy as np

from calculus import (
    calculate_definite_integral,
    calculate_derivative,
    calculate_double_derivative,
    calculate_improper_integral,
    calculate_integral,
    calculate_limit,
)
from linear_algebra import (
    add_matrices,
    determinant,
    eigen,
    inverse,
    multiply_matrices,
    rank,
    scalar_multiply,
    solve_linear,
    solve_quadratic,
    subtract_matrices,
    trace,
    transpose,
)
from number_theory import (
    check_prime,
    factorial,
    fibonacci,
    find_gcd,
    find_lcm,
    power,
    prime_factorization,
    sqrt,
)
from statistics_and_probability import (
    calculate_mean,
    calculate_median,
    calculate_mode,
    calculate_standard_deviation,
    calculate_variance,
    combinations,
    permutations,
    probability,
)
import trigo_and_log as trig


class MathToolkitTests(unittest.TestCase):
    def assert_array_equal(self, actual, expected):
        np.testing.assert_array_equal(actual, expected)

    def test_calculus_helpers_are_deterministic(self):
        self.assertEqual(calculate_limit("x", 2), 2)
        self.assertEqual(calculate_derivative("x^2"), "2*x")
        self.assertEqual(calculate_integral("2*x"), "x**2")
        self.assertEqual(calculate_definite_integral("x", 0, 2), "2")
        self.assertEqual(calculate_double_derivative("sin(x)"), "-sin(x)")
        self.assertAlmostEqual(calculate_improper_integral("exp(-x)", 0), 1.0, places=7)

    def test_linear_algebra_helpers_are_deterministic(self):
        a = np.array([[3, 1], [1, 2]])
        b = np.array([9, 8])
        self.assert_array_equal(solve_linear(a, b), np.array([2, 3]))

        self.assertEqual(solve_quadratic(1, -3, 2), (2.0, 1.0))
        self.assertEqual(solve_quadratic(0, 2, -4), 2.0)
        self.assertEqual(solve_quadratic(0, 0, 1), "No unique solution")

        m1 = np.array([[1, 2], [3, 4]])
        m2 = np.array([[5, 6], [7, 8]])
        self.assert_array_equal(add_matrices(m1, m2), np.array([[6, 8], [10, 12]]))
        self.assert_array_equal(subtract_matrices(m1, m2), np.array([[-4, -4], [-4, -4]]))
        self.assert_array_equal(scalar_multiply(2, m1), np.array([[2, 4], [6, 8]]))
        self.assert_array_equal(multiply_matrices(m1, m2), np.array([[19, 22], [43, 50]]))
        self.assertAlmostEqual(determinant(m1), -2.0, places=7)
        self.assertEqual(transpose(m1).tolist(), [[1, 3], [2, 4]])
        self.assertEqual(trace(m1), 5)
        self.assertEqual(rank(m1), 2)
        self.assertTrue(np.allclose(inverse(m1), np.array([[-2.0, 1.0], [1.5, -0.5]])))

        eigenvalues, eigenvectors = eigen(np.array([[1, 2], [2, 1]]))
        self.assertTrue(np.allclose(sorted(eigenvalues.tolist()), [-1.0, 3.0]))
        self.assertEqual(eigenvectors.shape, (2, 2))

    def test_number_theory_helpers_are_deterministic(self):
        self.assertTrue(check_prime(17))
        self.assertFalse(check_prime(15))
        self.assertEqual(prime_factorization(18), [2, 3])
        self.assertEqual(power(2, 3), 8.0)
        self.assertEqual(sqrt(16), 4.0)
        self.assertIsNone(sqrt(-1))
        self.assertEqual(find_gcd(48, 18), 6)
        self.assertEqual(find_lcm(15, 20), 60)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(factorial(5), 120)

    def test_statistics_helpers_are_deterministic(self):
        values = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_mean(values), 3)
        self.assertEqual(calculate_mean((1, 2, 3)), 2)
        self.assertEqual(calculate_median(values), 3)
        self.assertAlmostEqual(calculate_standard_deviation(values), 1.5811, places=4)
        self.assertAlmostEqual(calculate_variance(values), 2.5, places=4)
        self.assertEqual(calculate_mode([1, 2, 3, 4, 4]), 4)
        self.assertEqual(probability(2, 5), 0.4)
        self.assertEqual(combinations(5, 2), 10)
        self.assertEqual(permutations(5, 2), 20)

    def test_trigonometry_and_log_helpers_are_deterministic(self):
        self.assertAlmostEqual(trig.sin(math.pi / 2), 1.0, places=7)
        self.assertAlmostEqual(trig.cos(0), 1.0, places=7)
        self.assertAlmostEqual(trig.tan(0), 0.0, places=7)
        self.assertAlmostEqual(trig.arcsin(1), math.pi / 2, places=7)
        self.assertAlmostEqual(trig.arccos(1), 0.0, places=7)
        self.assertAlmostEqual(trig.arctan(1), math.pi / 4, places=7)
        self.assertAlmostEqual(trig.ln(math.e), 1.0, places=7)
        self.assertAlmostEqual(trig.log2(4), 2.0, places=7)
        self.assertAlmostEqual(trig.exp(1), math.e, places=7)
