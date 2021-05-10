"""Escribir una función que calcule el área de un círculo y otra que calcule 
el volumen de un cilindro usando la primera función."""
#constante pi
import math 

def areacirculo(radio):

    return math.pi*pow(radio, 2)
print (areacirculo(6))

"""v=(pi*r^2)*h"""
def volumencilindro (radio,altura):
    return (areacirculo(radio)*altura)

print (round(volumencilindro(8,15),2))
