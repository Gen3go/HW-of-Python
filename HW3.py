# Задача 3: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

number = int(input("Введите число билета: "))

firsthalf = int(round(number / 1000))
secondhalf = int(number % 1000)

a = int(firsthalf / 100)
b = int(firsthalf / 10 % 10)
c = int(firsthalf % 10)
d = int(secondhalf / 100)
e = int(secondhalf / 10 % 10)
f = int(secondhalf % 10)

summfirsthalf = a + b + c
summsecondhalf = d + e + f

if summfirsthalf == secondhalf:
    print("У Вас счастливый билетик")
else: 
    print("У Вас не счастливый билетик")



# print("Введите число билета по одной цифре:  ")
# a = input()
# b = input()
# c = input()
# d = input()
# e = input()
# f = input()

# if a + b + c == d + e + f:
#     print("У Вас счастливый билет!!!")

# else:
#     print("У Вас не счастливый билет")
