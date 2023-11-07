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
            return longest_words_list


if __name__ == '__main__':
    print("Слово/а с самой большой длиной:", longest_words('article.txt'))
