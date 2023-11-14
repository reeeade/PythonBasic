import argparse


def usage():
    # python Lesson14.py --file file_to_read.txt
    parser = argparse.ArgumentParser(
        description="Parse file and demo information.",
        epilog="Designed by developer Ivanna Ivannivna Juk",
        prog="Lesson14"
    )
    parser.add_argument(
        '-f', '--file',
        required=True,  # обовязковый параметр для вводу
        type=str,  # тип даних
        help='Повний або відносний шлях до файлу'  # пояснення для опцій
    )
    parser.add_argument(
        '-o', '--opacity',
        # required=True,  # обовязковый параметр для вводу
        type=str,  # тип даних
        help='sdgewgwhwh'  # пояснення для опцій
    )
    args = parser.parse_args()
    return args


def main():
    argument = usage()
    print('argument.file:', argument.file)
    print('argument.opacity:', argument.opacity)


if __name__ == '__main__':
    main()
