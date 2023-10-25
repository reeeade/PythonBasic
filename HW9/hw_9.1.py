from random import randint

int_elements = [randint(1, 500) for _ in range(25)]
print("Список int_elements:", int_elements)
sqr_elements = [i ** 2 for i in int_elements]
print("Список з квадратів int_elements:", sqr_elements)
remnant_elements = [i % 11 for i in int_elements]
print("Список з остач ділення на 11 елементів int_elements:", remnant_elements)
even_elements = [i for i in int_elements if i % 2 == 0]
print("Список з парних елементів int_elements:", even_elements)
odd_len_elements = [i for i in int_elements if len(str(i)) % 2 != 0]
print("Список з непарною кількістю цифр:", odd_len_elements)
no_three_elements = [int_elements[i] for i in range(len(int_elements)) if i % 3 != 0]
print("Список з елементів, що стоять на позиціях які не є кратними 3:", no_three_elements)