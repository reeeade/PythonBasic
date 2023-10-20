list1 = ["one", "two", "three", "four", "five"]
list2 = [1, 2, 3, 4, 5]
new_dict = {}

for i in range(len(list1)):
    new_dict[list1[i]] = list2[i]
print("Получившийся словарь:", new_dict)
