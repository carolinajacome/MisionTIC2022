"""Diseñe un algoritmo que permita imprimir un mensaje según la nota definitiva de un estudiante
 entre 0.0 y 5.0, de acuerdo conla Tabla:
  
note	Message to print
< 3.0	Insufficient
<= 3.5	Acceptable
<= 4.0	Outstanding
<= 5.0	Excellent
 
 """

def nota_final (note):
    if note <0 or note >5.0:
        return "Nota inválida"
    if note <3.0:
        return "Insufficiente"
    if note <=3.5:
        return "Acceptable"
    if note <=4.0:
        return "Outstanding"
    if note <=5.0:
        return "Excellent"

print(nota_final(1))
print(nota_final(10))
print(nota_final(0))
print(nota_final(-5))
print(nota_final(4))
print(nota_final(3.5))
print(nota_final(2))
print(nota_final(3))
print(nota_final(6))