# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
a1 = int(input("Введите первый элемент: "))
d = int(input("Введите  разность: "))
n = int(input("Введите количество элементов: "))

i = 0
list = []
while i < n:
    list.insert(i, a1)
    a1 = a1 + d
    i += 1
print(f"Полученная арифметическая прогрессия: {list}")