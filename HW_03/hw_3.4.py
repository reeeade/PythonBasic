year = int(input("Введите год для проверки в диапазоне от 1900 до 1_000_000: "))
if 1900 < year < 1_000_000:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                print(year, "является высокосным")
            else:
                print(year, "не явялется высокосным")
        else:
            print(year, "являеся высокосным")
    else:
        print(year, "не явялется высокосным")
else:
    print(year, "не соответствует условиям проверки!!!")
