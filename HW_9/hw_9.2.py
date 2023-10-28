from random import randint

matrix_size = int(input("Введите размер квадратной матрицы: "))
matrix = [[randint(1, 9) for _ in range(matrix_size)] for __ in range(matrix_size)]
print("Исходная матрица:")
for i in matrix:
    print(i)
d_sum = sum(matrix[i][i] for i in range(matrix_size))
print("Сумма чисел по диагонали:", d_sum)
last_sum = sum(matrix[i][-1] for i in range(matrix_size))
print("Сумма чисел последнего столбика:", last_sum)
