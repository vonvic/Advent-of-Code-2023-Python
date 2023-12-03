"""Advent of Code Problem 01 Solution."""

def find_first_digit(s: str) -> int:
    return next(filter(lambda x: x.isdigit(), s))

def part_one_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    numbers: list[int] = []
    with open("01/input.txt", "r") as f:
        for line in f.readlines():
            first = find_first_digit(line)
            second = find_first_digit(line[::-1])
            number = int(f"{first}{second}")
            numbers.append(number)
    return sum(numbers)
        
def part_two_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    None
