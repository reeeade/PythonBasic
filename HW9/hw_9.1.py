from random import randint

int_elements = [randint(1, 500) for _ in range(26)]
print(int_elements)
sqr_elements = [i ** 2 for i in int_elements]
print(sqr_elements)
remnant_elements = [i % 11 for i in int_elements]
print(remnant_elements)
even_elements = [i for i in int_elements if i % 2 == 0]
print(even_elements)
odd_len_elements = [i for i in int_elements if len(str(i)) % 2 != 0]
print(odd_len_elements)
no_three_elements = [int_elements[i] for i in range(len(int_elements)) if i % 3 != 0]
print(no_three_elements)