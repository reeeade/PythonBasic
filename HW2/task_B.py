name = input("Введите ваше имя: ")
patronymic = input("Введите ваше отчество: ")
age = int(input("Введите ваш возраст: "))

print("Привет ", patronymic, '.', sep='')
print(name, "это хорошее имя - мне нравится.")
print("До 100 лет тебе осталось жить", 100 - age, "лет")
