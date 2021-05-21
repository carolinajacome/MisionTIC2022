"""Diseñe un algoritmo que determine mayor número entre cuatro posibles números.
"""
def mayor (num1,num2,num3,num4):
    if num1> num2 and num1> num3 and num1>num4:
        return f"El mayor es el num1 " #+float(num1) 
    if num2> num1 and num2> num3 and num2>num4:
        return f"El mayor es el num2 " #+ float(num2)
    if num3> num1 and num3> num2 and num3>num4:
        return f"El mayor es el  num3" #+float(num3)
    if num4> num1 and num4> num2 and num4>num3:
        return f"El mayor es el num4 " #+ float(num4)

print(mayor(1,2,3,4))
print(mayor(4,4,3,4))
print(mayor(0,3,6,9))
print(mayor(-5,-2,0,2))
print(mayor(-5,-2,10,5))
print(mayor(-5,25,10,5))
print(mayor(65,0,10,5))