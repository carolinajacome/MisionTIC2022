"""Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan,
el descuento que se le hace por no ser fresca y el coste final total.""" 

barrasV_noDia= int (input ("Ingrese el número de barras vendidas que no son del día "))
precio_pan= 3.49
precio_dcto= precio_pan*0.60
precio_dcto_final= precio_pan-precio_dcto

total=precio_dcto*barrasV_noDia

print("El precio habitual de la barra de pan por unidad es de", precio_pan, "€",
"El descuento que se realizó por ser fresca es de",precio_dcto, "€"," El valor total a pagar es de",
precio_dcto_final, "€")