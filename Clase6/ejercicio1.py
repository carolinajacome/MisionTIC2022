"""Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0. 
El algoritmo debe imprimir el valor ingresado,y de ser una nota mayor o igual a 4.0
deberá imprimir un mensaje de felicitaciones."""

def mensaje(nota):
    if nota <0.0 or nota >5.0:
        return f"Error, la nota está fuera de rango"
    
    msj_felicitacion=" "
    if nota>=4:
        msj_felicitacion="¡Felitaciones!"
    return f"su nota es {nota} {msj_felicitacion}"

print (mensaje(10))
print (mensaje(4))
print (mensaje(1))
print (mensaje(0))
print (mensaje(3))
print (mensaje(5))
print (mensaje(-10))
print (mensaje(3.7))
print (mensaje(4.0))