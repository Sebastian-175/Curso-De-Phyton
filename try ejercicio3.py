# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:43:41 2023

@author: usuario
"""

from math import exp
ex=1
try:
    while True:
        
        print(exp(ex))
        ex *=2
except OverflowError:   
    print("El numero es muy grande")