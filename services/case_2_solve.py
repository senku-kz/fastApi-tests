from typing import Union, List


def solve_quadratic(a: float, b: float, c: float) -> Union[str, List[float]]:
    """Solves the quadratic equation ax^2 + bx + c = 0."""
    # Handle the case where it's not a quadratic equation
    if a == 0:
        if b == 0:
            return "Infinite solutions" if c == 0 else "No solution"
        return [round(-c / b, 6)]  # Return a single root in a list

    # Calculate the discriminant
    d = b**2 - 4*a*c
    if d < 0:
        return "No real roots"  # No roots
    elif d == 0:
        # One root
        x = -b / (2 * a)
        return [round(x, 6)]  # Return a single root in a list
    else:
        # Two roots, sorted in ascending order
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)
        return sorted([round(x1, 6), round(x2, 6)])  # Return a list of roots
