# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 14:21:55 2021

@author: Lenovo
ЗАДАЧА 7. ГЕНЕРАТОР ФАКТОРИАЛОВ
"""

#функция факториала
def fct(n):
    if n<0:
        raise ValueError('Факториал отрицательного числа не существует!')
    elif n>=0 and n<=1:
        return 1
    else:
        return n*fct(n-1)


#генератор
def fact(n):
    numbs=[]
    for i in range(1,n+1):
        numbs.append(fct(i))
    
    for el in numbs:
        yield el
    

n=int(input('Введите числа, по которое необходимо вывести их факториалы:'))
for el in fact(n):
    print(el)