# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 00:41:30 2021

@author: Lenovo
ЗАДАЧА 3: перебор чисел от 20 до 240, кратных 20 или 21
"""
for el in (el for el in range(20,241) if el%20==0 or el%21==0): print(el)