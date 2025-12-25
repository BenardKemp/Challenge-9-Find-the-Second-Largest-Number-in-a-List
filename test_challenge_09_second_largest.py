import pytest

from Challenge_9_Find_the_Second_Largest_Number_in_a_List import second_largest


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 2),
        ([5, 5, 3, 1], 3),
        ([-1, -5, -3], -3),
        ([10, 8, 9, 9], 9),
        ([100, 50, 75], 75),
        ([1.5, 2.5, 3.5], 2.5),
    ],
)
def test_second_largest_valid_cases(numbers, expected):
    assert second_largest(numbers) == expected


@pytest.mark.parametrize(
    "numbers",
    [
        [1],
        [2, 2],
        [3, 3, 3],
        [5, 5, 5, 5],
    ],
)
def test_second_largest_requires_two_unique_values(numbers):
    with pytest.raises(ValueError):
        second_largest(numbers)


@pytest.mark.parametrize(
    "bad_input",
    [
        "123",
        123,
        None,
        True,
        False,
        {"a": 1},
        (1, 2, 3),
    ],
)
def test_second_largest_rejects_non_list_input(bad_input):
    with pytest.raises(TypeError):
        second_largest(bad_input)


@pytest.mark.parametrize(
    "bad_list",
    [
        [1, "2", 3],
        [1, None, 3],
        [1, [], 3],
        [1, {}, 3],
        [1, object(), 3],
    ],
)
def test_second_largest_rejects_non_numeric_elements(bad_list):
    with pytest.raises(TypeError):
        second_largest(bad_list)
