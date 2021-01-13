# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 02:19:37 2021

@author: Lenovo

ЗАДАЧА 5. ВЫЧИСЛЕНИЕ ПРОИЗВЕДЕНИЯ ЧИСЕЛ ОТ 100 ДО 1000
С ПОМОЩЬЮ ФУНКЦИИ reduce
"""
from functools import reduce

def prod(a,b):
    return a*b

mas=range(100,1001)
print(reduce(prod,mas))