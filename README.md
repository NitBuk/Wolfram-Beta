# Wolfram-Beta

Wolfram-Beta is a personal educational math toolkit and terminal CLI. It keeps the core math helpers separate from the menu shell so the project can be read, tested, and extended like a small software system instead of a one-off script.

It covers five areas:

- Linear algebra
- Calculus
- Number theory
- Statistics and probability
- Trigonometry and logarithms

This repo is a local CLI project, not a deployed web app. Plotting opens a local Matplotlib window. Several submenu branches are still scaffolding, so the repository is intentionally honest about what is implemented today and what is still a placeholder.

## Quick Start

Requirements:

- Python 3.10+
- `pip`

Install and run:

```bash
git clone https://github.com/NitBuk/Wolfram-Beta.git
cd Wolfram-Beta
python3 -m pip install -e ".[dev]"
python3 -m wolfram_beta
```

`main.py` still works for compatibility:

```bash
python3 main.py
```

## Smallest Useful Demo

The fastest way to see the project working is to run the CLI and try the pure math helpers directly from Python.

```bash
python3 - <<'PY'
import numpy as np
from linear_algebra import determinant
from number_theory import find_gcd

print(find_gcd(48, 18))
print(determinant(np.array([[1, 2], [3, 4]])))
PY
```

## Supported Domains

- `linear_algebra.py` handles matrix arithmetic, determinants, inverses, eigenvalues, rank, transpose, trace, and a quadratic solver.
- `calculus.py` handles symbolic limits, derivatives, integrals, improper integrals, and a plotting helper.
- `number_theory.py` handles primality, prime factors, powers, square roots, GCD, LCM, Fibonacci, and factorial.
- `statistics_and_probability.py` handles mean, median, standard deviation, variance, mode, probability, combinations, and permutations.
- `trigo_and_log.py` handles the basic trig and logarithm functions.

## Project Structure

```text
Wolfram-Beta/
├── wolfram_beta/        # Installable CLI package and shared menu helpers
├── calculus.py          # Calculus helpers
├── linear_algebra.py    # Linear algebra helpers
├── number_theory.py     # Number theory helpers
├── statistics_and_probability.py
├── trigo_and_log.py
├── *_api.py             # Interactive menu layers
├── tests/               # Unittest coverage for deterministic helpers
├── pyproject.toml       # Packaging and lint config
└── README.md
```

## Developer Workflow

Run tests:

```bash
python3 -m unittest discover -s tests
```

Lint the code:

```bash
ruff check .
```

Format the code:

```bash
ruff format .
```

Local dev entrypoints:

- `python3 -m wolfram_beta`
- `python3 main.py`
- `wolfram-beta` after editable install

The math engine lives in the root helper modules, while the package entrypoint lives in [`wolfram_beta/cli.py`](wolfram_beta/cli.py).

## Why This Repo Matters

This project shows a few things recruiters and engineers usually care about:

- clear separation between pure logic and user interface code
- a reproducible install/test story
- comfort with numerical Python, SymPy, and NumPy
- honest scoping instead of inflated claims
- willingness to keep an older project maintainable instead of rewriting it from scratch

## Limitations

- Some submenu options are still scaffolding and do not yet have full interactive flows.
- `prime_factorization` returns unique prime factors, not repeated multiplicities.
- Plotting requires a local graphical environment.
- This is a toolkit, not a symbolic math platform or a production service.

## Recent Improvements

- Added an installable package entrypoint and console script.
- Replaced the root test dump with a focused `unittest` suite.
- Removed star imports and centralized menu rendering helpers.
- Added packaging metadata, `.gitignore`, and CI.
- Tightened the README to reflect the actual scope of the project.

## Roadmap

- Wire the remaining submenu actions to interactive prompts where it makes sense.
- Add a few more example-driven tests around plotting and edge cases.
- Split the helper modules into a package if I decide to evolve this from a toolkit into a larger library.
