# lambda x, y=5: round((x ** 2 + y ** 2) ** 0.5, 2)
list_x = [1, 2, 3, 4, 5]
list_y = [3, 6, 5, 8, 9]

gip_list1 = map(lambda x, y=5: round((x ** 2 + y ** 2) ** 0.5, 2), list_x)
print("Список значений гипотенуз при передачи только одного списка:", list(gip_list1), sep="\n")
gip_list2 = map(lambda x, y=5: round((x ** 2 + y ** 2) ** 0.5, 2), list_x, list_y)
print("Список значений гипотенуз при передачи двух списков:", list(gip_list2), sep="\n")
