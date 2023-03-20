# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:31:46 2023

@author: usuario
"""

x=input("Ingresa sus Nombres: ")
y=input("Ingresa sus Apellidos: ")
espacio=" "

print("Bienvenido al sistema de reconocimiento: " , x ,espacio,y)  
print("\n")
print("Para continuear con el registro ingrese  su edad por favor")  
print("\n")
z=int(input("Edad: "))
print("\n")

if z<18:
    
     print ("Menor de edad") 
     print("\n")
     print("Para continuear con el registro debe ser mayor de edad")  
     print("\n")
     x=input("Ingresa sus Nombres: ")
     y=input("Ingresa sus Apellidos: ")
     espacio=" "
     print("\n")
     print("Bienvenido al sistema de reconocimiento: " , x ,espacio,y)  
     print("\n")
     print("Para continuear con el registro ingrese  su edad por favor")  
     print("\n")
     z=int(input("Edad: "))
     print("\n")
     print("Edad registrada de : " , z , "\n" , "Como punto final ingrese si ubicacion") 
     u=input("Ubicacion: ")
     print("\n")
     print("Bienvenido estimado: " , x , espacio, y ,espacio,"loacaliado en la ciudad de: ", u , espacio ,"con la edad de: " , z )
     
else:   
     print("\n")
     print("Edad registrada de : " , z , "\n" , "Como punto final ingrese si ubicacion") 
     print("\n")
     u=input("Ubicacion: ")
     print("\n")
     print("Bienvenido estimado: " , x , espacio, y ,espacio,"loacaliado en la ciudad de: ", u , espacio ,"con la edad de: " , z )

 

    
        
           