# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:56:22 2021

@author: Lenovo
ЗАДАЧА 6_1. ВЫВОД ЧИСЕЛ ОТ ЗАДАННОГО ДО 20
ВХОД: одно целое число меньше 20. Если число больше 20,
то ничего не возвращается
"""

from sys import argv
from itertools import count

for el in count(int(argv[1])):
    if el>20:
        break
    else:
        print(el)
    
