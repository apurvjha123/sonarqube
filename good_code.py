def add_numbers(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


def is_even(num: int) -> bool:
    """Return True if the number is even, else False."""
    return num % 2 == 0


def main():
    print("5 + 3 =", add_numbers(5, 3))
    print("Is 10 even?", is_even(10))


if __name__ == "__main__":
    main()
