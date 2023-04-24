# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки

n = int(input("Введите количество кустов: "))
berry = []
i = 0
while i < n:
    berry.insert(i, int(input(f"Введите количество ягод на {i+1} кусте: ")))
    i += 1


i = n - 1
sum = berry[i] + berry[i - 1] + berry[i - 2]
while (i >= 0):

    j = i
    while j >= 0:
        if (sum < berry[j-1] + berry[j - 2] + berry[j - 3]):
            sum = berry[j-1] + berry[j - 2] + berry[j - 3]
            j -= 1 
        else:
            j -= 1
    i -= 1
print(f"Максимальное количество собранных ягод: {sum}")