# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

N = int(input("Введите число N - количество элементов в массиве A[1..N]: "))
if N < 1:
    print("Введите число больше 0!")
else:
    i = 1
    A = []
    while (i <= N):
        A.append(i)
        i+=1
    print(*A)
    X = int(input("Введите число X: "))
    print(f"Cамый близк(ий/ие) по величине элемент/ы к заданному числу {X}:")
    nearest = None
    nearest2 = None
    if X > N: 
        nearest = N
    elif X < 1:
        nearest = 1
    elif X == N:
        nearest = X - 1
    elif X == 1:
        nearest = X + 1
    else: 
        nearest = X + 1
        nearest2 = X - 1
        print(nearest2)
    print(nearest)

