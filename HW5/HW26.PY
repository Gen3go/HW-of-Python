# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


# def Exponentiation(a, b):
#     exp = pow(a, b)
#     return exp

a = int(input("Введите число А: "))
b = int(input("Введите число B: "))

# print(Exponentiation(a, b))

def expt(a, b):
    if b == 0:
        return 1
    return b*expt(b, a-1)

print(expt(a, b))