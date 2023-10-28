def is_equivalent_sum2num(_list, num):
    """
    The function checks if there are 2 numbers in _list, the sum of which is equivalent to num.

    :param _list: input list, which we check. Class list
    :param num: input number - the sum of the two numbers in the _list. Class int
    :return: True, if there are two numbers from the list whose sum is equivalent to target_sum, otherwise False
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
