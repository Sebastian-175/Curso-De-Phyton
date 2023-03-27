# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 11:05:07 2023

@author: usuario
"""

lista=[]
archivo=open("devices.txt")
for item in archivo:
    item=item.strip()
    lista.append(item)
    print(item)
archivo.close()