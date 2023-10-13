num = tuple(input("Введите число: "))
for i in num:
    if num.count(i) >= 2:
        print("Да, в числе есть 2 одинаковые цифры!")
        break
else:
    print("Нет, в числе нет 2-х одинаковых цифры!")