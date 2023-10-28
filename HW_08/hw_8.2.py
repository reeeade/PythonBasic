list1 = [1, 2, 3, 4, 5, 6, 7, 3, 51, 74, 44, 1, 4, 99]
list2 = [3, 4, 2, 1, 8, 99, 76, 44, 3, 5, 6, 1, 2, 3, 7, ]
intersec = set(list1) & set(list2)
count = len(intersec)
print(f'Общие, уникальные числа для двух списков: {intersec}\n'
      f'Их количество: {count}')
