# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

n = 10
i = 0
list = []
import random
while i < n:
    list.insert(i, *random.sample(range(1, 101), 1))
    i += 1
print(f"Данный массив: {list}")

min = int(input("Введите минимум диапазона (от 1 до 100): "))
max = int(input("Введите  максимум диапазона (от 1 до 100): "))

i = 0
list1 = []
while i < n:
    if list[i] >= min and list [i] <= max:
        list1.insert(i, i)
    i+=1
print(f"Индексы, значения в которых больше {min} и меньше {max}: {list1}")