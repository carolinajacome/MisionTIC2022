"""Diseñe un algoritmo que determine si un número real (x) se encuentra dentro de uno de los 
siguientes rangos: (3.5, 7.8], [9.3, 4.5) y [23.4, 45.3]."""
def rangoa_c (numero):
    
    if (numero >3.5 and numero<= 7.8) or (numero >=9.3 and numero< 4.5) or  (numero >=23.4 and numero<= 45.3):
        return "Pertenece a algunos de los siguientes rangos (3.5, 7.8]  [9.3, 4.5) y [23.4, 45.3]"
    
    else:  
        return "No pertenece a ningún rango"

print(rangoa_c(1))
print(rangoa_c(3))
print(rangoa_c(5))
print(rangoa_c(-3))
print(rangoa_c(50))
print(rangoa_c(9.4))
print(rangoa_c(4.5))
print(rangoa_c(23.4))
