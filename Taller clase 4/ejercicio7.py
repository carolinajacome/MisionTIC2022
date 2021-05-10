"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos
y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado."""

cantidad_payasos= int (input("Ingrese la cantidad de payasos vendidos: "))
cantidad_munecas= int (input("Ingrese la cantidad de muñecas vendidas: "))
peso_Upayaso=112
peso_Umuneca=75

peso_payasos= cantidad_payasos*peso_Upayaso
peso_munecas= cantidad_munecas*peso_Umuneca

pesoTotal= peso_payasos+peso_munecas
print ("El peso total del paquete es ", pesoTotal, "g " "El peso para ",cantidad_payasos, " payasos es ",peso_payasos , " El peso para ",cantidad_munecas, " muñecas es ",peso_munecas )