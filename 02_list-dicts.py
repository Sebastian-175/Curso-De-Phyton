# Create a list of the BRICS countries

country = [ "Brazil","Russia","India","China", "South Africa"]

"""Create a dictionary of BRICS capitals.
Note that South Africa has 3
 capitals. Therefore, we embed a list inside
the dictionary.
"""

capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": ["Pretoria","Cape Town","Bloemfontein"]
           }

# Print the list and dictionary
print(country)
print(capitals)
"""
What response did you get?
ESTABAN DECLARADAS COMO TEXTO LOS NOMBRES DE LA LISTA Y EL DICCIONARIO 
Why did the list and dictionary
 contents not print?
Fix the code and run the script again.
"""
print( capitals["South Africa"][1] )
print( capitals["South Africa"][2] )
"""
Why did you get an error for the
 2nd capital of South Africa?
 SE HACE LA LLAMADA A LA KEY DEL DICCIONARIO PERO SE DEBE PONER POR SEPARADO
 LA UBICACION DEL VALOR DE LA LISTA
Hint: Check the syntax for the 
index value.
"""
