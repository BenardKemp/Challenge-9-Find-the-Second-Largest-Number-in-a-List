def second_largest(numbers: list) -> int | float:
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    unique_numbers = set()

    for n in numbers:
        if not isinstance(n, (int, float)):
            raise TypeError("All items must be numbers")
        unique_numbers.add(n)

    if len(unique_numbers) < 2:
        raise ValueError("At least two unique numbers are required")

    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]

print(second_largest([3, 8, 18, 21, 5, 7, 20]))