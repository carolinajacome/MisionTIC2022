"""Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, 
deberá aplicar un 19%.
"""
def calcularIva(precio, porcentajeIva=1.19):
   # total= precio*porcentajeIva
    return precio*porcentajeIva

print (calcularIva(1000,2))
print (calcularIva(1000))