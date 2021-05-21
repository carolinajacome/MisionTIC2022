"""Diseñe un algoritmo que determine si un número real (x) se encuentra dentro del rango 
abierto-cerrado (3.5, 7.8]."""
def rangoa_c (numero):
    
    if numero >3.5 and numero<= 7.8:
        return "Pertenece al rango"
    else:
     return "fuera de rango"

print(rangoa_c(1))
print(rangoa_c(3))
print(rangoa_c(5))
print(rangoa_c(8))
print(rangoa_c(7))