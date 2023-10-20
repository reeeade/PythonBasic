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

more, less = None, None
for k, v in new_dict.items():
    if more is None or v > new_dict[more]:
        more = k
    if less is None or v < new_dict[less]:
        less = k
print(f"Наиболее встречаемое слово '{more}': {new_dict[more]} раз")
print(f"Наименее встречаемое слово '{less}': {new_dict[less]} раз")
