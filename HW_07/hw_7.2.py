from random import randint

new_dict = {}
mp = 1
for i in range(20):
    new_dict[i] = randint(1, 20)
    mp *= new_dict[i]
print("Сгенерированный словарь:", new_dict)
print("Результат умножения чисел в словаре:", mp)
