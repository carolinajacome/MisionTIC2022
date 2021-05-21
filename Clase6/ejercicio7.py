
"""
Diseñe un algoritmo que permita imprimir un mensaje según un carácter dado por el usuario,
independiente que sea ingresado en mayúscula o minúscula, según la Tabla:

Carácter	Mensaje a imprimir

 'a'	       Android
 'i'     	    IOS
 otro	    Opcion inválida
"""
def carac (caracter):
    if len(caracter)!=1:
        return "ERROR Cáracter inválido"
    if caracter=="a" or caracter =="A":
        return ("Android")
    elif caracter =="i" or caracter =="I":
        return ("IOS")

