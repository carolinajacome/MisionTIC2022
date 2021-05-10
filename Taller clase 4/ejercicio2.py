"Escribir una función que reciba un número entero positivo y devuelva su factorial."

import math

def factorial(n):
    """Función que calcula el factorial de un número entero positivo.
    Parámetros
    n: Es un entero positivo.
    Devuelve el factorial de n.
    
    """
    f=1
    for i in range (1,n+1):
        f*=i
    return f

    

print(factorial(4))
print(factorial(20))