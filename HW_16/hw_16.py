import argparse


def longest_words(file: str):
    """
    Функция для вывода слова/слов с самой большой длиной в текстовом файле

    :param file:Имя/путь текстового файла
    :return:Список слов с самой большой длиной в файле
    """
    with open(file, "r", encoding='utf-8') as art:
        text = art.read()
        words = text.replace('"', '').replace('\n', ' ').split()
        longest_words_list = [w for w in words if len(w) == max(len(i) for i in words)]
        if len(longest_words_list) == 1:
            return longest_words_list[0]
        else:
            return ', '.join(longest_words_list)


def usage():
    """
    Парсим аргумент командной строки

    :return: Объект аргументов(параметры запуска)
    """
    parser = argparse.ArgumentParser(
        description="Парсим файл и находим самые длинные слова/слово",
        epilog="Разработчик: Глеб Кулик",
        prog="Поисковик"
    )

    parser.add_argument(
        '-f', '--file',
        required=True,
        type=str,
        help='Название файла или путь к нему'
    )

    args = parser.parse_args()
    return args


def main():
    arguments = usage()
    try:
        words = longest_words(arguments.file)
    except FileNotFoundError:
        print("Файлы с таким именем не существует!!!")
    else:
        print(f"Самое длинное слово/слова в файле '{arguments.file}': {words}")


if __name__ == '__main__':
    main()
