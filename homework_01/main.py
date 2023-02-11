"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number**2 for number in args]


def is_prime(number):
    if number <= 1:
        return False
    if number % 2 == 0:
        return number == 2
    divider = 3
    while divider * divider <= number and number % divider != 0:
        divider += 2
    return divider * divider > number

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(number_list, command):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    res = []
    if command == PRIME:
        for number in number_list:
            if is_prime(number) == True:
                res.append(number)
    elif command == ODD:
        res = [number for number in number_list if number % 2 != 0]
    elif command == EVEN:
        res = [number for number in number_list if number % 2 == 0]
    return res
