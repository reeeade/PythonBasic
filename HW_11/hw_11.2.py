def is_prime(num: int) -> bool:
    """
    Ф-я для определения является ли число простым или нет

    :param num: Проверяемое число
    :return: True если число простое. В противном случае False
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True


def generate_prime(n: int, z: int):
    """
    Ф-я генератор для генерирования последовательности простых чисел в указанном диапазоне

    :param n: Начало диапазона
    :param z: Конец диапазона
    :return: generate object of prime numbers
    """
    for num in range(n, z + 1):
        if is_prime(num):
            yield num


if __name__ == '__main__':
    from random import randint

    begin = randint(1, 50)
    end = randint(51, 100)

    print(f"Простые числа в диапазоне от {begin} до {end}:")
    for item in generate_prime(begin, end):
        print(item, end=" ")
