# Задача 2
# Напишите программу, которая принимает на вход число N и выдает 
# набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from os import system

system ('cls')

number =  input ('Введите целочисленное число от 1: ')

while number.isdigit() == False or int (number) <1:
    number =input ('Вы ввели число не правильно, введите его заново от 1: ')

nev_list = []
number=int (number)

for i in range (1,number+1):
    sum=1
    for n in range (1,i+1):
        sum=sum*n
    nev_list.append(sum)

print(nev_list)