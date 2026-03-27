"""Non-interactive command support for Wolfram Beta."""

from __future__ import annotations

import argparse
import ast
import json
from collections.abc import Sequence

import numpy as np

from calculus import (
    calculate_definite_integral,
    calculate_derivative,
    calculate_improper_integral,
    calculate_integral,
    calculate_limit,
)
from linear_algebra import determinant, inverse, trace, transpose
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


def _parse_matrix(raw_matrix: str) -> np.ndarray:
    """Parse a matrix from JSON or Python literal notation."""
    try:
        data = json.loads(raw_matrix)
    except json.JSONDecodeError:
        try:
            data = ast.literal_eval(raw_matrix)
        except (SyntaxError, ValueError) as exc:
            raise argparse.ArgumentTypeError(
                "Matrix must be JSON or Python literal notation, such as '[[1, 2], [3, 4]]'."
            ) from exc

    if not isinstance(data, list) or not data or any(not isinstance(row, list) for row in data):
        raise argparse.ArgumentTypeError("Matrix must be a non-empty list of lists.")

    try:
        matrix = np.array(data, dtype=float)
    except (TypeError, ValueError) as exc:
        raise argparse.ArgumentTypeError("Matrix entries must be numeric.") from exc

    if matrix.ndim != 2:
        raise argparse.ArgumentTypeError("Matrix must be two-dimensional.")
    return matrix


def _format_scalar(value: object) -> str:
    if isinstance(value, (np.integer, int)) and not isinstance(value, bool):
        return str(int(value))
    if isinstance(value, (np.floating, float)):
        number = float(value)
        if number.is_integer():
            return str(int(number))
        return format(number, ".12g")
    return str(value)


def format_result(value: object) -> str:
    """Convert a command result into a compact terminal-friendly string."""
    if isinstance(value, np.ndarray):
        return np.array2string(
            value,
            separator=", ",
            formatter={
                "int_kind": lambda x: str(int(x)),
                "float_kind": lambda x: _format_scalar(float(x)),
            },
        )
    if isinstance(value, tuple):
        return "(" + ", ".join(format_result(item) for item in value) + ")"
    if isinstance(value, list):
        return "[" + ", ".join(format_result(item) for item in value) + "]"
    return _format_scalar(value)


def _number_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("number", help="Number theory helpers")
    number_subparsers = parser.add_subparsers(dest="number_command", required=True)

    def add_simple(name: str, handler, *arguments: tuple[str, dict]) -> None:
        command = number_subparsers.add_parser(name)
        for arg_name, kwargs in arguments:
            command.add_argument(arg_name, **kwargs)
        command.set_defaults(handler=handler)

    add_simple("prime", lambda args: check_prime(args.value), ("value", {"type": int}))
    add_simple(
        "prime-factors",
        lambda args: prime_factorization(args.value),
        ("value", {"type": int}),
    )
    add_simple(
        "power",
        lambda args: power(args.base, args.exponent),
        ("base", {"type": float}),
        ("exponent", {"type": float}),
    )
    add_simple("sqrt", lambda args: sqrt(args.value), ("value", {"type": float}))
    add_simple(
        "gcd",
        lambda args: find_gcd(args.left, args.right),
        ("left", {"type": int}),
        ("right", {"type": int}),
    )
    add_simple(
        "lcm",
        lambda args: find_lcm(args.left, args.right),
        ("left", {"type": int}),
        ("right", {"type": int}),
    )
    add_simple("fibonacci", lambda args: fibonacci(args.value), ("value", {"type": int}))
    add_simple("factorial", lambda args: factorial(args.value), ("value", {"type": int}))


def _statistics_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("stats", help="Statistics and probability helpers")
    stats_subparsers = parser.add_subparsers(dest="stats_command", required=True)

    def add_values(name: str, handler) -> None:
        command = stats_subparsers.add_parser(name)
        command.add_argument("values", nargs="+", type=float)
        command.set_defaults(handler=handler)

    add_values("mean", lambda args: calculate_mean(args.values))
    add_values("median", lambda args: calculate_median(args.values))
    add_values("stdev", lambda args: calculate_standard_deviation(args.values))
    add_values("variance", lambda args: calculate_variance(args.values))
    add_values("mode", lambda args: calculate_mode(args.values))

    probability_parser = stats_subparsers.add_parser("probability")
    probability_parser.add_argument("event_outcomes", type=int)
    probability_parser.add_argument("sample_space", type=int)
    probability_parser.set_defaults(
        handler=lambda args: probability(args.event_outcomes, args.sample_space)
    )

    combinations_parser = stats_subparsers.add_parser("combinations")
    combinations_parser.add_argument("n", type=int)
    combinations_parser.add_argument("r", type=int)
    combinations_parser.set_defaults(handler=lambda args: combinations(args.n, args.r))

    permutations_parser = stats_subparsers.add_parser("permutations")
    permutations_parser.add_argument("n", type=int)
    permutations_parser.add_argument("r", type=int)
    permutations_parser.set_defaults(handler=lambda args: permutations(args.n, args.r))


def _trig_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("trig", help="Trigonometry and logarithm helpers")
    trig_subparsers = parser.add_subparsers(dest="trig_command", required=True)

    def add_unary(name: str, handler) -> None:
        command = trig_subparsers.add_parser(name)
        command.add_argument("value", type=float)
        command.set_defaults(handler=handler)

    add_unary("sin", lambda args: trig.sin(args.value))
    add_unary("cos", lambda args: trig.cos(args.value))
    add_unary("tan", lambda args: trig.tan(args.value))
    add_unary("arcsin", lambda args: trig.arcsin(args.value))
    add_unary("arccos", lambda args: trig.arccos(args.value))
    add_unary("arctan", lambda args: trig.arctan(args.value))
    add_unary("ln", lambda args: trig.ln(args.value))
    add_unary("log2", lambda args: trig.log2(args.value))
    add_unary("exp", lambda args: trig.exp(args.value))


def _calculus_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("calculus", help="Calculus helpers")
    calculus_subparsers = parser.add_subparsers(dest="calculus_command", required=True)

    derivative = calculus_subparsers.add_parser("derivative")
    derivative.add_argument("expression")
    derivative.set_defaults(handler=lambda args: calculate_derivative(args.expression))

    integral = calculus_subparsers.add_parser("integral")
    integral.add_argument("expression")
    integral.set_defaults(handler=lambda args: calculate_integral(args.expression))

    limit_parser = calculus_subparsers.add_parser("limit")
    limit_parser.add_argument("expression")
    limit_parser.add_argument("point", type=float)
    limit_parser.set_defaults(
        handler=lambda args: calculate_limit(args.expression, args.point)
    )

    definite_integral = calculus_subparsers.add_parser("definite-integral")
    definite_integral.add_argument("expression")
    definite_integral.add_argument("start", type=float)
    definite_integral.add_argument("end", type=float)
    definite_integral.set_defaults(
        handler=lambda args: calculate_definite_integral(args.expression, args.start, args.end)
    )

    improper_integral = calculus_subparsers.add_parser("improper-integral")
    improper_integral.add_argument("expression")
    improper_integral.add_argument("start", type=float)
    improper_integral.set_defaults(
        handler=lambda args: calculate_improper_integral(args.expression, args.start)
    )


def _linear_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("linear", help="Linear algebra helpers")
    linear_subparsers = parser.add_subparsers(dest="linear_command", required=True)

    def add_matrix_command(name: str, handler) -> None:
        command = linear_subparsers.add_parser(name)
        command.add_argument("--matrix", required=True, type=_parse_matrix)
        command.set_defaults(handler=handler)

    add_matrix_command("determinant", lambda args: determinant(args.matrix))
    add_matrix_command("trace", lambda args: trace(args.matrix))
    add_matrix_command("transpose", lambda args: transpose(args.matrix))
    add_matrix_command("inverse", lambda args: inverse(args.matrix))


def build_parser() -> argparse.ArgumentParser:
    """Build the top-level argparse parser."""
    parser = argparse.ArgumentParser(
        prog="wolfram-beta",
        description="Run Wolfram Beta in interactive mode or as a direct math command.",
    )
    subparsers = parser.add_subparsers(dest="domain", required=True)
    _linear_parser(subparsers)
    _number_parser(subparsers)
    _statistics_parser(subparsers)
    _trig_parser(subparsers)
    _calculus_parser(subparsers)
    return parser


def execute_command(argv: Sequence[str]) -> int:
    """Parse and execute a direct command."""
    parser = build_parser()
    args = parser.parse_args(list(argv))
    handler = getattr(args, "handler", None)
    if handler is None:
        parser.print_help()
        return 1

    result = handler(args)
    if result is None:
        return 1

    print(format_result(result))
    return 0
