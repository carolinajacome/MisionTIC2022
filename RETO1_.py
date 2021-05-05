
def simular_recaudo_producto(precio_base, cantidad, porcentaje_actual=0):
    #ENTRADAS
 #   precio_base = float (input("Ingrese el precio base: "))
    precio_base =  float(input("Ingrese el precio base: "))
    cantidad= int(input ("Ingrese la cantida de productos a vender: "))
    porcentaje_actual= int (input("Ingrese el valor actual del porcentaje"))
    #porcentaje_actual= (int, opcional)
    #ALGORITMO
   
    incremento_iva= (19-porcentaje_actual)
    valor_recaudado = float(((precio_base*incremento_iva)/100)*cantidad)

    print ("El valor recaudado es: " +str(valor_recaudado))

simular_recaudo_producto(100,1000) 
