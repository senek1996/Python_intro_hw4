# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 00:07:46 2021
@author: Lenovo

ЗАДАЧА 1: РАСЧЕТ ЗП СОТРУДНИКА
ПОРЯДОК ПЕРЕДАЧИ ПАРАМЕТРОВ:
    СТАВКА (руб/ч) - ВЫРАБОТКА (ч) - ПРЕМИЯ (руб)
"""
from sys import argv

print('Зарплата сотрудника: {0} р.'.format((float(argv[1])*float(argv[2]))+float(argv[3])))