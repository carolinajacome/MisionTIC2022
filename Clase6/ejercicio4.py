"""Diseñe un algoritmo que determina si un número es par o impar. Recuerde que un número es par 
si el resto de una división entera con el número 2 es cero"""

def par(numero):
    if numero%2==0:
        return "El numero es par"
    else:
        return "El número es impar"

print(par(2))
print(par(-2))
print(par(0))
print(par(5))
print(par(1000003))