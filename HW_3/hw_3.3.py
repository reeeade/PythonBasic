name = "Глеб"
password = "12345"
inp_pass = input("Введите пароль: ")
if inp_pass != password:
    print("Неверный пароль! В доступе отказано!")
else:
    print(name, ", с возвращением. Пароль верный. Доступ разрешен!")
