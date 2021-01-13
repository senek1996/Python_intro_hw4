# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 01:20:17 2021

@author: Lenovo
ЗАДАЧА 4. ПОИСК НЕПОВТОРЯЮЩИХСЯ ЭЛЕМЕНТОВ
"""

from random import randrange

def gen(l):
    n_viewed=[] #просмотренные числа
    n=[]        #числа, встречающиеся только 1 раз
    for el in l:
        if el in n_viewed:
            try:
                n.remove(el)
            except:
                if len(n)==0: #список n пустой
                    n.append(el) #добавление первого числа ряда в массивы
                    n_viewed.append(el)
        else:
            n.append(el)
            n_viewed.append(el)
        
    
    for el in n:
        yield el

l=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]#[5,3,6,5,8,8,2,3,1,3]
gn=gen(l)
for el in gn:
    print(el)