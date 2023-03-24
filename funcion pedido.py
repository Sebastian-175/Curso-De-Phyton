# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:48:11 2023

@author: usuario
"""

def pedido(calle,ciudad,CP):
    print("Favor de ingresar los siguientes datos:" , calle ,"St. ", ciudad, CP)
    
c=input("DIreccion: ")
ci=input("ciudad:")
cp=input("codigo postal: ")
pedido(c,ci,cp)