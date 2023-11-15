def sum_or_conc(a, b):
    """
    Ф-я для нахождения суммы двух чисел. Если один и аргументов не является числом,
    то выполняется конкатенация

    :param a: Первое число/текст
    :param b: Второе число/текст
    :return: Сумма чисел или новый текст
    """
    try:
        _sum = a + b
        assert not (isinstance(a, str) and isinstance(b, str))
    except AssertionError:
        print(f"Ошибок нет! Но т.к два значения это текст, то была выполнена конкатенация!\n"
              f"Результат ---> {a + b}")
    except TypeError as er:
        _sum = str(a) + str(b)
        print(f"Вы попытались сложить число со строкой! Получили ошибку {type(er).__name__}!\n"
              f"Не беда! Была выполнена конкатенация!\nРезультат ---> {_sum}")
    else:
        print(f"Ошибок нет!\nРезультат ---> {_sum}")
    finally:
        print("*" * 50)


if __name__ == "__main__":
    sum_or_conc(3, 4)
    sum_or_conc('Hello', 555)
    sum_or_conc("Hello", "user")
