# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять
# из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  
# Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам 

stroka1 = "пара-ра-рам рам-пам-папам па-ра-па-да"
vowels = ["а", "е", "ё", "и", "й", "о", "у", "ы", "э", "ю", "я"]
phrases = stroka1.split()
if len(phrases) < 2:
    print("Мало фраз")
else:
    countVolwels = []
    for i in phrases:
        countVolwels.append(len([x for x in i if x.lower() in vowels]))

    if set(countVolwels) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")
