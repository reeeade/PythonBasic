inp_string = input("Введите строку из 15+ символов: ")

if not inp_string:
    print("Строка пуста! Завершение программы . . .")
else:
    if len(inp_string) < 15:
        koef = 15 // len(inp_string) + 1
        inp_string *= koef

    new_list = list(inp_string)
    print("Полный список:", new_list)
    print("Последние 5 элементов:", new_list[-5:])
    print("Зеркальный список:", new_list[::-1])
    print("Все парные элементы:", new_list[::2])

    custom_list = new_list[:-5] + new_list[:5]
    print("5 элементов вначале = 5 элементам в конце списка:", custom_list)

