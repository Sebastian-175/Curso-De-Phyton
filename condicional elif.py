# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:42:29 2023

@author: usuario
"""

x=int(input("Ingresar la Edad: "))
if x>=0 and x<=5:    
    print("De 0 a 5 años es un BEBE ")
elif x>=6 and x<=12:    
    print("De 6 a 12 años es un Infante ")
elif x>=13 and x<=19:    
    print("De 13 a 19 años es Adolecente ")
elif x>19 and x<=35:    
    print("De 20 a 35 años es Aulto Joven ")
elif x>35 and x<=60:    
    print("De 36 a 60 años es Adulo")
else:
    print("De 60 años en adelante es Adulto mayor") 