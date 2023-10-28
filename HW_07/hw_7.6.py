txt = """
Любіть Україну, як сонце, любіть,
як вітер, і трави, і води…
В годину щасливу і в радості мить,
любіть у годину негоди.
Любіть Україну у сні й наяву,
вишневу свою Україну,
красу її, вічно живу і нову,
і мову її солов’їну.
Між братніх народів, мов садом рясним,
сіяє вона над віками…
Любіть Україну всім серцем своїм
і всіми своїми ділами.
Для нас вона в світі єдина, одна
в просторів солодкому чарі…
Вона у зірках, і у вербах вона,
і в кожному серця ударі,
у квітці, в пташині, в електровогнях,
у пісні у кожній, у думі,
в дитячий усмішці, в дівочих очах
і в стягів багряному шумі…
"""

new_txt = txt.lower().replace(',', '').replace('.', '').replace('…', '')
new_txt_list = new_txt.split()

new_dict = {}
for i in new_txt_list:
    new_dict[i] = new_dict.get(i, 0) + 1

more_value = max(new_dict.values())
less_value = min(new_dict.values())
more_list = []
less_list = []
for i in new_dict:
    if new_dict[i] == more_value:
        more_list.append(i)
    if new_dict[i] == less_value:
        less_list.append(i)

more = ', '.join(more_list)
less = ', '.join(less_list)
print(f'Реже ({less_value} раз/а) встречаются слова/о: {less}')
print(f'Чаще ({more_value} раз/а) встречаются слова/о: {more}')
