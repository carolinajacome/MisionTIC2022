"""Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés
al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta
de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar 
por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
Redondear cada cantidad a dos decimales. """

n_depositado= int(input("Ingrese el depósito "))
#n_cantidadtiempo= int(input("Ingrese el tiempo del interés "))
#interes= n_depositado*0.04*n_cantidadtiempo
interes= 1.04 
ahorro_anio1= n_depositado*interes
#ahorro_anio1= interes1
print("Cantidad ahorro primer año:" + str(round(ahorro_anio1, 2)))
ahorro_anio2= ahorro_anio1*interes
print("Cantidad ahorro segundo año:" + str(round(ahorro_anio2, 2)))
ahorro_anio3= ahorro_anio2*interes
print ("La cantidad de ahorro el tercer año es: " + str(round(ahorro_anio3,2)))