def update_hero(**kwargs):
    """
    Ф-я перезаписывает текстовый файл, изменяя параметры внесенные
    в качестве аргументов ф-ии. Остальные параметры остаются неизменными

    :param kwargs: Параметры, которые мы хотим изменить
    """
    with open('hero.ini', 'r') as hero:
        dict_hero = {}
        for line in hero.readlines():
            param = line.replace('\n', '').split('=')
            key, value = param
            dict_hero[key] = value

    with open('hero.ini', 'w') as hero:
        for k, i in kwargs.items():
            if k in dict_hero:
                dict_hero[k] = i
        for k, v in dict_hero.items():
            line = f"{k}={v}\n"
            hero.write(line)


if __name__ == '__main__':
    update_hero(hero="Spider", power=240, Y=1.6, X=1.4, Z=2)
