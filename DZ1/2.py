# Задача 2: Найдите сумму цифр трехзначного числа.

num = int(input("Введите трёхзначное число: "))
if (100 <= num < 1000):
    firstnum = int(num / 100)
    secondnum = int(num / 10) - firstnum * 10
    thirdnum = num % 10
    sum = firstnum + secondnum + thirdnum
    print(f"Сумма цифр этого числа: {sum} = {firstnum} + {secondnum} + {thirdnum}")
else: print("Не трёхзначное число")