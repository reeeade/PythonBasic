num = int(input("Введите число: "))
i = 0
print(num, '>--квадраты--->', end=" ")
while i ** 2 <= num:
    print(i ** 2, end=" ")
    i += 1
