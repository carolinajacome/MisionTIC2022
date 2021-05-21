"""La oficina de aguas de la ciudad requiere crear un algoritmo que le permita liquidar las
facturas de sus clientes durante cada mes. El cobro de cada factura se realiza de la siguiente forma:
se cobra el cargo fijo, el consumo de agua en el periodo, es decir, la cantidad de metros consumidos
y el servicio de recolección de basuras y alcantarillado. Construya un algoritmo que, al ingresarle 
es estrato socioeconomico del predio y la cantidad de metros cúbicos de agua consumidos, 
permita determinar el valor de la factura a pagar. Todos estos cobros se llevan a cabo dependiendo
 del estrato socioeconómico al que pertenezca el predio, de acuerdo con la siguiente tabla
 Estrato	Cargo Fijo	Metro3 consumido	Basuras y alcantarillado
    1	       $2500	          $2200	                $5500
    2	       $2800	           $2350	            $6200
    3	       $3000	          $2600	                $7400
    4	       $3300	         $3400	                $8600
    5	       $3700	           $3900	            $9700
    6	       $4400	           $4800	            $11000
 """
def facturas (estrato,metros):
     if estrato<0 or estrato >6:
        return "Error en el estrato .Válido 1 a 6"
     if metros<0:
        return "Error los metros consumidos deben ser mayores a 0"
     cargo_fijo1= 2500
     cargo_fijo2= 2800
     cargo_fijo3= 3000
     cargo_fijo4=3300
     cargo_fijo5= 3700
     cargo_fijo6=4400
     metro1=2200
     metro2=2350
     metro3=2600
     metro4=3400
     metro5=3900
     metro6=4800
     bas_alc1=5500
     bas_alc2=6200
     bas_alc3=7400
     bas_alc4=8600
     bas_alc5=9700
     bas_alc6=11000
     factura1= (cargo_fijo1+ metro1*metros +bas_alc1)
     factura2= (cargo_fijo2+ metro2*metros +bas_alc2)
     factura3= (cargo_fijo3+ metro3*metros +bas_alc3)
     factura4= (cargo_fijo4+ metro4*metros +bas_alc4)
     factura5= (cargo_fijo5+ metro5*metros +bas_alc5)
     factura6= (cargo_fijo6+ metro6*metros +bas_alc6)
     
     if estrato ==1:    
        return factura1
     if estrato ==2:
         return factura2
     if estrato ==3:
         return factura3
     if estrato ==4:    
        return factura4
     if estrato ==5:
         return factura5
     if estrato ==6:
         return factura6

print(facturas(1,1))
print(facturas(4,3))
print(facturas(0,0))
print(facturas(4,-2))