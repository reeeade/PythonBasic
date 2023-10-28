num = int(input("Введите целое пятизначное число -> "))
threes = num // 3
sixes = num // 6
num, units = divmod(num, 10)
num, ten = divmod(num, 10)
num, hundred = divmod(num, 10)
num, thousand = divmod(num, 10)
num, tens_of_thousand = divmod(num, 10)

print("Десяток тысяч :", tens_of_thousand)
print("Тысяч :", thousand)
print("Сотен :", hundred)
print("Десяток :", ten)
print("Едениц :", units)

print("Троек в числе :", threes)
print("Шестерок в числе :", sixes)