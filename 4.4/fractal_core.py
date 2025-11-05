"""fractal_core.py

Small pure-Python functions used for non-visual testing of the recursive
fractal in `project.py`.

This module intentionally avoids turtle or any GUI dependencies so tests
can run in headless environments.
"""

from typing import Optional


def expected_calls(level: int, branches: int = 3) -> int:
    """Compute the expected number of recursive calls performed by
    the `drawTree` function in `project.py`.

    The `drawTree` implementation used in `4.4/project.py` returns 0 for
    level <= 0 and otherwise counts 1 (this call) plus `branches` times the
    calls at level-1. That produces the recurrence:

        T(0) = 0
        T(n) = 1 + branches * T(n-1)

    Args:
        level: recursion level (non-negative integer)
        branches: number of recursive sub-calls per node (default 3)

    Returns:
        int: expected number of recursive calls
    """
    if level <= 0:
        return 0
    # iterative approach to avoid deep recursion in test helper
    total = 0
    # compute bottom-up
    for lvl in range(1, level + 1):
        total = 1 + branches * total
    return total
