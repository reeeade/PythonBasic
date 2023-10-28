def is_equivalent_sum2num(_list, num):
    """
    Функция проверяет, есть ли в _list 2 числа, сумма которых эквивалентна num.

    :param _list: Список чисел, который мы проверяем. Тип list
    :param num: Входное число - сумма двух чисел в _list. Тип int
    :return: True, если есть два числа из списка, сумма которых эквивалентна num, в противном случае False
    """
    checks_items = []
    for item in _list:
        diff = num - item
        if diff in checks_items:
            return True
        checks_items.append(item)
    return False


list1 = [1, 2, 3, 4]
num1 = 5
res1 = is_equivalent_sum2num(list1, num1)

list2 = [5, 6, 7, 8]
num2 = 4
res2 = is_equivalent_sum2num(list2, num2)

print(f'Сумма двух чисел в списке {list1} = числу {num1}? Ответ: {res1}')
print(f'Сумма двух чисел в списке {list2} = числу {num2}? Ответ: {res2}')
