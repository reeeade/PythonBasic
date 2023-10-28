from random import randint


def generate_matrix(h=5, w=5):
    """
    Функция создает двухмерный список, заполненный случайными числами от 0 до 200

    :param h: Высота "матрицы"(количество строк). По-умолчанию 5
    :param w: Ширина "матрицы"(количество столбцов). По-умолчанию 5
    :return: Двухмерный список
    """
    matrix = [[randint(0, 200) for _ in range(w)] for __ in range(h)]
    return matrix


def print_symmetrical_table(matrix):
    """
    Функция печатает симметрическую табличку(колонки не разъезжаются) с выравниванием по левому краю

    :param matrix: Двухмерный список(список списков)
    """
    max_size = max(len(str(num)) for row in matrix for num in row)
    for row in matrix:
        print(' | '.join(str(elem).ljust(max_size) for elem in row))
    # for i in matrix:
    #     for j in i:
    #         print(f"{j:<{max_size + 2}}", end="")
    #     print()


print("Первая функция не получает параметры")
print_symmetrical_table(generate_matrix())
print("Первая функция получает 1 параметр")
print_symmetrical_table(generate_matrix(3))
print("Первая функция получает 2 параметра")
print_symmetrical_table(generate_matrix(4, 7))
