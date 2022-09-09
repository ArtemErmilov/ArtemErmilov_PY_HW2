# Задача 3
# Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе 
# стороны читалось одинаково, но есть одно "но".

# Если перевернутое число не равно исходному, то они складываются 
# и проверяются на палиндром еще раз.

# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

from os import system
system ('cls')

def check_palindrom(number): # определение палиндрома 
    print(number, end='\t')

    if (len(number))==1:
        print ('Не палиндром')
        return False

    for i in range((len(number)-1)):
     if number[i]!=number[(len(number)-1)-i]:
            print ('Не палиндром')
            return False

    print ('Палиндром')
    return True



number =  input ('Введите целочисленное число от 1: ')

while number.isdigit() == False or int (number) <1:
    number =input ('Вы ввели число не правильно, введите его заново от 1: ')


print ('-'*50)
while check_palindrom(number) == False:
    number = str (int(number)+int(number[::-1]))
    



