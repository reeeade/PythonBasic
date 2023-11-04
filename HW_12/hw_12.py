from random import randint


def create_sorted_matrix(m: int):
    """
    Функция создает, а затем сортирует матрицу(двухмерный список). Алгоритм сортировки:
    Порядок колонок сортируется относительно суммы колонки(по возрастанию суммы) методом пузырька.
    Сами же колонки сортируются в зависимости от четности или нечетности номера колонки по порядку.
    Четные сортируются по увеличению сверху вниз, а нечетные наоборот. Так же методом пузырька.

    :param m: Размер 'квадратной' матрицы.
    :return: Отсортированный, согласно условий двухмерный список.
    """
    matrix = [[randint(1, 50) for _ in range(m)] for __ in range(m)]
    sum_col = [sum(col) for col in zip(*matrix)]
    for n in range(m - 1):
        for i in range(m - 1 - n):
            if sum_col[i] > sum_col[i + 1]:
                sum_col[i], sum_col[i + 1] = sum_col[i + 1], sum_col[i]
                for j in matrix:
                    j[i], j[i + 1] = j[i + 1], j[i]

    for j in range(m):
        for n in range(m - 1):
            for i in range(m - n - 1):
                if (j + 1) % 2 == 0 and matrix[i][j] > matrix[i + 1][j]:
                    matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
                if (j + 1) % 2 != 0 and matrix[i][j] < matrix[i + 1][j]:
                    matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
    matrix.append(sum_col)
    return matrix


def print_matrix(matrix: list):
    """
    Функция для вывода в консоль, отформатированную в виде таблички матрицу.

    :param matrix: Двухмерный список(список списков)
    """
    for i in range(len(matrix) - 1):
        print(' | '.join(str(elem).rjust(len(str(max(matrix[-1])))) for elem in matrix[i]))
    print('-' * ((len(str(max(matrix[-1]))) + 3) * (len(matrix) - 1)))
    print(' | '.join(str(elem).rjust(len(str(max(matrix[-1])))) for elem in matrix[-1]))


if __name__ == '__main__':
    matrix_size = int(input("Введите размер 'квадратной' матрицы больше 5:"))
    while matrix_size <= 5:
        matrix_size = int(input("Введите размер 'квадратной' матрицы !!БОЛЬШЕ!! 5:"))
    print_matrix(create_sorted_matrix(matrix_size))
