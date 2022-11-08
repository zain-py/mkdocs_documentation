# calculator/calculations.py

"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import divide
    >>> divide(4.0, 2)
    2.0

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""


def add(a: float | int, b: float | int) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 5.0)
        9.0
        >>> add(4, 5)
        9.0

    Args:
        A number representing the first addend in the addition.
        A number representing the second addend in the addition.

    Returns:
        A number representing the sum of 'a' and 'b'.
    """
    return float(a + b)


def subtract(a: float | int, b: float | int) -> float:
    """Compute and return the difference of two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Args:
        A number representing the minuend in the subtraction.
        A number representing the substrahend in the subtraction.

    Returns:
        A number representing the difference of 'a' and 'b'.
    """
    return float(a - b)


def multiply(a: float | int, b: float | int) -> float:
    """Compute and return the product of two numbers.

    Examples:
        >>> multiply(2.0, 4.0)
        8.0
        >>> multiply(2, 4)
        8.0

    Args:
        A number representing the multiplicand in the multiplication.
        A number representing the multiplier in the multiplication.

    Returns:
        A number representing the product of 'a' and 'b'.
    """
    return float(a * b)


def divide(a: float | int, b: float | int) -> float:
    """Compute and return the quotient of two numbers.

    Examples:
        >>> divide(8.0, 2.0)
        4.0
        >>> divide(8, 2)
        4.0
        >>> divide(8, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: Division by zero!

    Args:
        A number representing the dividend in the division.
        A number representing the divisor in the division.

    Returns:
        A number representing the quotient of 'a' and 'b'.

    Raises:
        ZeroDivisionError: An error occurs when divisor is '0'.
    """
    if b == 0:
        raise ZeroDivisionError('Division by zero!')
    return float(a / b)
