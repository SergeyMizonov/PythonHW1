# Урок 1. Ввод-Вывод, операторы ветвления
# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# n = int(input("Введите трехзначное число: "))

# sum = 0

# while n > 0:
#           item = n % 10
#           sum += item
#           n //= 10
 
# print("Сумма: ", sum)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# s=int(input("Введите число журавликов: "))
# print((s//6), ((s//6)*4), (s//6))

# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

# n = input("Введите шестизначное число: ")
# sum1 = int(n[0]) + int(n[1]) + int(n[2])
# sum2 = int(n[3]) + int(n[4]) + int(n[5])
# if sum1 == sum2:
#     print('Счастливый')
# else:
#     print('Обычный')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите размер шоколадки n: "))
m = int(input("Введите размер шоколадки m: "))
k = int(input("Введите количество долек k: "))

if k < m*n and (k%m==0 or k%n==0):
          print("Yes")
else:
          print("No")