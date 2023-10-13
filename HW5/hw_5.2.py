num = int(input("Введите натуральное число: "))
for i in range(1, num + 1):
    num_str = str(i)
    sqr_str = str(i ** 2)
    if num_str == sqr_str[-len(num_str):]:
        print(num_str, '*', num_str, '=', sqr_str)
