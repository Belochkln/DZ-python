# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum(a, b):
    if a <= 0 and b <= 0:
        return 0
    elif a == 0:
        return 1 + sum(a,b - 1)
    elif b == 0:
        return 1 + sum(a - 1,b)
    return 1 + 1 + sum(a - 1,b - 1)

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
print(f"Сумма чисел : {sum(A, B)}")