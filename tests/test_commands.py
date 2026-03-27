import unittest
from contextlib import redirect_stdout
from io import StringIO

from wolfram_beta.commands import execute_command, format_result


class CommandModeTests(unittest.TestCase):
    def run_command(self, argv):
        buffer = StringIO()
        with redirect_stdout(buffer):
            exit_code = execute_command(argv)
        return exit_code, buffer.getvalue().strip()

    def test_number_prime_factors_command(self):
        exit_code, output = self.run_command(["number", "prime-factors", "84"])
        self.assertEqual(exit_code, 0)
        self.assertEqual(output, "[2, 3, 7]")

    def test_linear_determinant_command(self):
        exit_code, output = self.run_command(
            ["linear", "determinant", "--matrix", "[[1, 2], [3, 4]]"]
        )
        self.assertEqual(exit_code, 0)
        self.assertEqual(output, "-2")

    def test_calculus_derivative_command(self):
        exit_code, output = self.run_command(["calculus", "derivative", "x**2 + 1"])
        self.assertEqual(exit_code, 0)
        self.assertEqual(output, "2*x")

    def test_format_result_handles_matrices(self):
        self.assertEqual(format_result([[1, 2], [3, 4]]), "[[1, 2], [3, 4]]")


if __name__ == "__main__":
    unittest.main()
