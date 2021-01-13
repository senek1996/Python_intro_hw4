# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:56:22 2021

@author: Lenovo
ЗАДАЧА 6_2. ПОВТОР ЭЛЕМЕНТОВ СПИСКА ЗАДАННОЕ КОЛИЧЕСТВО РАЗ
ПОРЯДОК АРГУМЕНТОВ: <список> <количество_раз>
список - строка
"""

from sys import argv
from itertools import cycle

i=1
cou=int(argv[2])

for el in cycle(argv[1]):
    if i>cou:
        break
    else:
        print(el)
        i+=1
    
