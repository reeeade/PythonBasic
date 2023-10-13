inp_num = int(input("Введите число: "))
# Проверка на ввод первого символа.
# Не допускается, чтоб список был пустым.
# Иначе при расчете среднего ар. будет ошибка(попытка деления на 0)
while inp_num == 0:
    inp_num = int(input("Введите хотяб одно значение неравное нулю!: "))
inp_list = []

while inp_num != 0:
    inp_list.append(inp_num)
    inp_num = int(input("Введите число: "))
else:
    print('-' * 20, "ВВЕДЕН 0!", '-' * 20, sep='\n')
print('Итоговый список:', inp_list)
print('1. Сумма чисел:', sum(inp_list))
print('2. Среднее арифметическое:', sum(inp_list) / len(inp_list))
print('3. Максимум:', max(inp_list), '\n', ' ', 'Минимум:', min(inp_list))
# Блок проверки четных и нечетных чисел
even, odd = 0, 0
for i in inp_list:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print('4. Четных чисел:', even, '\n', ' ', 'Нечетных чисел:', odd)
