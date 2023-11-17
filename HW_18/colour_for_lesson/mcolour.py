"""
Модуль для форматирования текста, вывода предупреждений
Возможность изменить цвет текста, цвет фона, стиль текста
Так же в виде словарей представлены коды для выбора цвета фона и текста
"""

_back_colour = {
    'red': '41m',
    'black': '40m',
    'green': '42m',
    'yellow': '43m',
    'blue': '44m',
    'purple': '45m',
    'biruza': '46m',
    'white': '47m'
}

_colour = {
    'red': '31m',
    'black': '30m',
    'green': '32m',
    'yellow': '33m',
    'blue': '34m',
    'purple': '35m',
    'biruza': '36m',
    'white': '37m'
}


def color_text(text: str, colour_name: str) -> str:
    """
    Ф-я устанавливает цвет текста

    :param text: Текст для смены цвета
    :param colour_name: Название цвета из словаря colour
    :return: Текст с измененным цветом
    """
    coloured_txt = '\033[' + _colour[colour_name] + text + '\033[0m'
    return coloured_txt


def color_back(text: str, colour_name: str = _back_colour['purple']) -> str:
    """
    Ф-я для изменения цвета фона в тексте

    :param text: Текст для смены цвета фона
    :param colour_name: Код цвета из таблицы кодов для фона (по-умолчанию розовый)
    :return: Текст с измененным цветом фона
    """
    clean_style_code = '\033[0m'
    back_color = f'\033[{colour_name}{text}{clean_style_code}'
    return back_color


def styled(text: str, code: str = "3m") -> str:
    """
    Ф-я для изменения стиля текста

    :param text: Текст для смены стиля
    :param code: Код, соответствующий стилю текста (курсив, жирный и т.д)
    :return: Текст с измененным стилем
    """
    clean_style_code = '\033[0m'
    styled_txt = f'\033[{code}{text}{clean_style_code}'
    return styled_txt


def error_message(message: str) -> str:
    """
    Ф-я для вывода предупреждающего текста 'Error' перед основным текстом

    :param message: Основной текст
    :return: Предупреждение + основной текст
    """
    status = "ERROR"
    error = color_text(f"{status:<8} ", _colour['red'])
    _message = color_text(message, _colour['yellow'])
    err_message = error + _message
    return err_message


def warning_message(message: str) -> str:
    """
    Ф-я для вывода предупреждающего текста 'Warning' перед основным текстом

    :param message: Основной текст
    :return: Предупреждение + основной текст
    """
    status = "WARNING"
    warn = color_text(f"{status:<8} ", _colour['yellow'])
    _message = color_text(message, _colour['biruza'])
    warn_message = warn + _message
    return warn_message


def info_message(message: str) -> str:
    """
    Ф-я для вывода предупреждающего текста 'Info' перед основным текстом

    :param message: Основной текст
    :return: Предупреждение + основной текст
    """
    status = "INFO"
    info = color_text(f"{status:<8} ", _colour['purple'])
    _info_message = info + message
    return _info_message
