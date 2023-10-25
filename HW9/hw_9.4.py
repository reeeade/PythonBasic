data = [
    {"name": "Alisa", "country": "UA", "item": "socks", "price": 15},
    {"name": "Alisa", "country": "UA", "item": "socks", "price": 25},
    {"name": "Ben", "country": "US", "item": "pencil", "price": 95},
    {"name": "Alisa", "country": "UA", "item": "pencil", "price": 45},
    {"name": "Oleg", "country": "GB", "item": "socks", "price": 100},
    {"name": "Ben", "country": "US", "item": "pencil", "price": 10}
]

workers = set(_dict["name"] for _dict in data)
print("Работники:", workers)
new_dict = {name: sum(i["price"] for i in data if i["name"] == name) for name in workers}
print("Продажи за неделю:", new_dict)
