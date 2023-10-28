_str = "Python is good language to learn and in same time we like to tell that it is cool expereance for us"
new_str = _str.replace(' ', '').lower()

new_dict = {}
for i in new_str:
    new_dict[i] = new_dict.get(i, 0) + 1
print("Словарь букв и их вхождерний в исходную строку:", new_dict, sep="\n")
