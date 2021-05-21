"""Diseñe un algoritmo que permita solicitar tanto el nombre como la edad de una persona y
posteriormente indicar si es “Mayor de edad” o “Menor de edad” según la información ingresada. 
Una persona se considera mayor de edad si tiene 18 años o más."""

def edadf (nombre,edad):
    if edad <=-1:
        return "Error, la edad está fuera de rango"

    mensaje= " "
    if edad >=18:
       return  "Es mayor de edad"
    else:
       return "Es menor de edad"

nombre= input("Ingrese el nombre")
edad =int (input ("Ingrese la edad"))
print (edadf(nombre,edad))