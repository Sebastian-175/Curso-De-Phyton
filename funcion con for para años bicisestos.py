# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 21:45:26 2023

@author: usuario
"""

def es_bisiesto(año):
	return not año % 4 and (año % 100 or not año % 400)

for año in range(1800, 2021):
	if es_bisiesto(año):
		print(año, end=' ')