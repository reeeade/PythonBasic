with open("output_hw_13.1.txt", "w") as txt_file:
    text = input("Вводите текстовые данные\n"
                 "Для перехода на новый рядок нажмите 'Enter'\n"
                 "Ввод заканчивается когда будет введена пустая строка!\n>")
    while not text:
        text = input("Введите хотя бы один рядок!\n>")
    while text:
        txt_file.write(text + '\n')
        text = input(">")
    txt_file.write("-" * 20)
    print("Введена пустая строка.\nЗавершение записи в файл!")