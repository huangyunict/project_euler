"""Solution for Project Euler problem 3: https://projecteuler.net/problem=3."""
from assertpy import assert_that
from sympy import primefactors


def solve_p3(n: int) -> int:
    """Solver for problem 3."""
    return primefactors(n)[-1]


if __name__ == '__main__':
    # Verify.
    assert_that(solve_p3(13195)).is_equal_to(29)
    assert_that(solve_p3(600851475143)).is_equal_to(6857)
    # Solution.
    print(solve_p3(600851475143))  # 6857
