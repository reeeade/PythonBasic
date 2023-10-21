test = [1, 2, 3, 3, 2, 6, "hello", "python", [3, 4, "test"], (1, 5, 7), {"one": 1, "two": 2}]
new_set = set()
hash_types = (int, float, str, tuple, frozenset, bool)
for i in test:
    if type(i) in hash_types:
        new_set.add(i)
print("Итоговое множество, состоящее только из хешируемых данных:", new_set, sep='\n')
