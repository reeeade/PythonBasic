# Задание А

print("заміна значень 2х змінних використовючи 3-тю змінну:")
var1 = 10
var2 = 20
print('var1 до замены = ', var1)
print('var2 до замены = ', var2)
temp_var = var1
var1 = var2
var2 = temp_var
print('var1 после замены = ', var1)
print('var2 после замены = ', var2)
print("----------")

print("заміна значень 2х змінних використовуючи властивості python:")
print('var1 до замены = ', var1)
print('var2 до замены = ', var2)
var1, var2 = var2, var1
print('var1 после замены = ', var1)
print('var2 после замены = ', var2)
print("----------")

print("заміна значень 2 змінних не використівуючи 2х попредніх варіантів")
print('var1 до замены = ', var1)
print('var2 до замены = ', var2)
var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2
print('var1 после замены = ', var1)
print('var2 после замены = ', var2)
print("----------")