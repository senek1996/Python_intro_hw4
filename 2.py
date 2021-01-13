# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 00:30:21 2021

@author: Lenovo
"""

from random import randrange

def gen(l):
    prev=9999999 #очень большое число
    for el in l:
        if el>prev:
            yield el
            
        prev=el
        

l=[]
for i in range(20):
    l.append(randrange(0,1000))

for el in gen(l):
    print(el)