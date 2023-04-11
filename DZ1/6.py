# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

number = int(input("Введите шестизначное число: "))

firstpart = int(number / 1000)
secondpart = int(number % 1000)

firstnum1 = int(firstpart / 100)
secondnum1 = int(firstpart / 10) - firstnum1 * 10
thirdnum1 = firstpart % 10
sum1 = firstnum1 + secondnum1 + thirdnum1

firstnum2 = int(secondpart / 100)
secondnum2 = int(secondpart / 10) - firstnum2 * 10
thirdnum2 = secondpart % 10
sum2 = firstnum2 + secondnum2 + thirdnum2

if(sum1 == sum2):
    print("Счастливый билет!")
else: print("Не счастливый билет, повезёт в другой раз!")