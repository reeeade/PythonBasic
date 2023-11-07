import json

data = [
    {'student': 'Vitaliy', 'marks': [2, 2, 2, 4, 3, 3, 4, 5, 5, 5, 4], 'age': 18},
    {'student': 'Ivan', 'marks': [5, 5, 5, 5, 5, 5, 5, 4, 4], 'age': 18},
    {'student': 'Stepan', 'marks': [2, 2, 4, 3, 3, 3, 5, 3], 'age': 19},
    {'student': 'Locky', 'marks': [2, 2, 2, 3, 3], 'age': 20},
    {'student': 'Halk', 'marks': [2, 2, 2, 4], 'age': 18},
    {'student': 'Kolobok', 'marks': (5, 5, 3, 5, 4), 'age': 416},
]

print("DATA", data)

data_str = json.dumps(data)
print(data_str)

with open("my-file.json", 'w', encoding='utf-8') as fid:
    json.dump(data, fid, indent=4)

with open("my-file.json", 'r', encoding='utf-8') as fid:
    r_data = json.load(fid)

print(r_data)