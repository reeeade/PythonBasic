from colour_for_lesson.mcolour import styled, color_text, color_back


def style_all(txt: str):
    """
    Ф-я применяет форматирование ко всему тексту (стиль, цвет фона и текста)

    :param txt: Текст для форматирования
    :return: Отформатированный текст
    """
    new_txt = []
    for line in txt.splitlines():
        colour = color_text(line, 'black')
        back = color_back(colour)
        style = styled(back)
        new_txt.append(style)
    return '\n'.join(new_txt)


def style_someone(txt: str, *args):
    """
    Ф-я выбирает ключевые слова, переданные в качестве аргументов через запятую и делает их жирными

    :param txt:Текст в котором выбираются ключевые слова
    :param args: Ключевые слова для выделения
    :return: Текст с выделенными ключевыми словами
    """
    new_txt = txt
    for word in args:
        new_txt = new_txt.replace(word, styled(word, "1m"))
    return new_txt


text = """Зацвітає калина,
Зеленіє ліщина,
Степом котиться диво-луна,
Це моя Україна,
Це моя Батьківщина,
Що, як тато і мама, одна.
"""

if __name__ == '__main__':
    new_text = style_all(text)
    print(style_someone(new_text, 'Україна', 'Батьківщина'))
