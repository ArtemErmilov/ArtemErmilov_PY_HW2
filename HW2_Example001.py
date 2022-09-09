# Задача 1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его 
# цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11


from os import system

system ('cls')


number_in = input('Введите число: ')


number = number_in.replace('-','0')
number = number.replace('.','0')

while number.isdigit() == False or number_in.count('-')>1 or (number_in.count('-')==1 and number_in[0]!='-') or number_in.count('.')>1:
    number_in = input('Вы ввели число не правильно, введите число заново: ')
    number = number_in.replace('-','0')
    number = number.replace('.','0')
    number.isdigit()

sum_number = 0
for i in number[:]:
    sum_number=sum_number+int(i)

print (f'Сумма цифр в числе {number_in} равняется ',sum_number)
