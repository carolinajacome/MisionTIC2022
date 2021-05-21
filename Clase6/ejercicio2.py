"""Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0.
 El algoritmo debe imprimir el valor ingresado, y un mensaje que indique si el estudiante 
 “Ganó el curso” o “Perdió el curso”.
 Se gana el curso solo si la nota definitiva es mayor o igual a 3.0."""


def validarnota(nota):
     #ValidarEntrada
        if nota <0.0 or nota >5.0:
            return f"Error, la nota está fuera de rango"
        #Algoritmo
        mensaje=" "
        if nota>=4:
            mensaje="¡Felitaciones,pasó el curso!"
        else:
             mensaje=" Perdió el curso!"
        return mensaje
    
print (validarnota(10))
print (validarnota(0))
print (validarnota(-6))
print (validarnota(5))
print (validarnota(3.0))
print (validarnota(2.90))
print (validarnota(4))