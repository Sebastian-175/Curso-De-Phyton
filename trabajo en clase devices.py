# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 11:09:40 2023

@author: usuario
"""

file = open("devices.txt", "a")
while True:
    newItem = input("ingrese un nuevo item: ")
    if newItem == "exit":
        print("All done!")
        break
    else:
        file.write(newItem + "\n")
file.close()