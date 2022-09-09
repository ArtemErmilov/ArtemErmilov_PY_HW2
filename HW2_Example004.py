# Задача 4

# Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) 
# - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import datetime
from os import system
import time
system ('cls')





def range_myn (min_, max_):
    multiplicity = len(str(abs((int(max_))-1)-abs(int(min_))))
    if multiplicity >6:
        multiplicity=6
    dt = datetime.datetime.now()
    number = (dt.strftime('%f'))
    divider = str(int(number[6-multiplicity:])**int(number[5:]))
    divider = int(divider[len(divider)-multiplicity:])
    if min_>=0 and min_>=0:
         ret = float(min_)+((float(max_-1)-float(min_))/(((10**multiplicity))*divider))
    else:
        ret = float(min_)-(((float(min_)-float(max_-1))/((10**multiplicity))*divider))
    
    time.sleep(0.111)
    return round(ret)



list_myn =[]

for i in range(0,10):
    list_myn.append(range_myn (-100, 100))

print (list_myn)
