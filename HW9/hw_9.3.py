from random import randint

new_set = set(randint(1, 99) for _ in range(15))
print(new_set)
answer = "Да" if sum(i for i in new_set if i % 2 != 0) > sum(i for i in new_set if i % 2 == 0) else "Нет"
print(answer)
