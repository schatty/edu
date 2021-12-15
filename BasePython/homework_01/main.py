"""
HW #1
Functions and data sctructures.
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [n**2 for n in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"
FILTER_TYPES = [ODD, EVEN, PRIME]


def is_prime(n) -> bool:
    """
    Returns if passed number is prime.
    """
    if n < 2:
        return False
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            return False
    return True


def filter_numbers(nums, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    assert filter_type in FILTER_TYPES, f"Allowed filter_type: {FILTER_TYPES}"

    if filter_type == ODD: 
        return list(filter(lambda x: x % 2 != 0, nums))
    elif filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, nums))
    else:
        return list(filter(is_prime, nums))
