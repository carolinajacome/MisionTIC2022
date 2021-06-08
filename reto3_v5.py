def simulador_prestamo_yo_le_fio(datos_venta:dict):
    saldoafinanciar=round((datos_venta["venta"]-datos_venta["cuota inicial"]),0)      
    TMV = ((1+ (datos_venta["interes anual"]/100))**(1/12)-1)
    den2= (1- (1+TMV)**(-datos_venta["cuotas"]))/TMV
    cuota= round((saldoafinanciar/den2),0)
    Valorinteres=round((saldoafinanciar*TMV),2)
    capitalabonado= round((cuota- Valorinteres),2)
    numerocuota= 0
    nuevoSaldo= (saldoafinanciar-capitalabonado)
    saldo=datos_venta["venta"]
    salida= dict()
    
    salida["saldo a financiar"] = round((datos_venta["venta"]-datos_venta["cuota inicial"]),0) 
    salida ["cuota"] =  round((saldoafinanciar/den2),0)
   
    #salida["amortización "]= [(numerocuota,capitalabonado,Valorinteres,cuota,saldoafinanciar)]
    #salida["amortización "]=[]
    numerocuota=1
    Valorinteres= round((saldoafinanciar*TMV),2)
    capitalabonado= round((cuota-Valorinteres),2)
    valorcuota= round((cuota),2)
    nuevoSaldo= round((saldoafinanciar-capitalabonado),2)
   
    salida["amortizacion"]= [(numerocuota,capitalabonado,Valorinteres,valorcuota,nuevoSaldo)]
    
    cantidadC= datos_venta["cuotas"]

    #ciclo
    


    return salida
datos_venta={
    "venta":2000000.0,
    "cuota inicial": 0.0,
    "cuotas": 6,
    "interes anual": 28.99
    }
    
print (simulador_prestamo_yo_le_fio(datos_venta))