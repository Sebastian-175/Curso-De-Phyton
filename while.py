# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 19:23:09 2023

@author: usuario
"""

x=input("Ingrese el # que debo contar")
x=int(x)
contador=1

while(True):
    print (contador)
    contador+=1
    if contador>x:
        break
    print ("Dentro del bucle" )
print ("Final")
    