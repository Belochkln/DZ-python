# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке.


shoutout = 'пара-ра-рам рам-пам-папам па-ра-па-да'

def Rhythm(shoutout):
    shoutout = shoutout.split()
    list_1 = []

    for word in shoutout:
        sum_gl = 0
        for i in word:
            if i in 'ауоыиэяюёе':
                sum_gl += 1
        list_1.append(sum_gl)
    return len(list_1) == list_1.count(list_1[0])
   
if Rhythm(shoutout):
    print('Парам пам-пам')
else:
    print('Пам парам')




























# letters = ['а','е','и','о','у','ё','ю','я']
# temp = 0
# ammount = 0
# story = input("Введите стих: ")
# sep_story = story.split(sep=' ')

# for letter in sep_story[0]:
#     if letter in letters:
#        temp = temp + 1
# list = []
# i = 0
# while i < len(sep_story):
#     j=0
#     while j < len(sep_story[i]):
#         word = sep_story[i]
#         if word[j] in letters:
#             ammount = ammount + 1
#         j = j + 1
#     list.insert(i, ammount)
#     ammount = 0
#     i = i + 1 
  
# z = 0
# while z < len(sep_story):
#     if sep_story[0] == sep_story[z]:
#         continue
#     if z == len(sep_story) - 1:
#         print("Парам пам-пам")
#     else: 
#         print("Пам парам")
#         break
#     z = z + 1