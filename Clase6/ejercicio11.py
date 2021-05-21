"""La oficina de incorporación del ejército necesita un algoritmo que le pueda permitir saber si un
aspirante a ingresar a la institución como soldado es apto o no para poder vincularlo.
Para que una persona sea apta, debe cumplir los siguientes requisitos:
Si es mujer, su estatura debe ser superior a 1.60 mts y su edad debe estar entre 20 y 25 años.

Si el aspirante es hombre, se estatura debe ser superior a 1.65 mts y su edad debe estar entre los 18
 y 24 años.
Tanto mujeres como hombres deben ser solteros. Diseñe el algoritmo de tal forma que permita informar
 si un aspirante es apto o no para ingresar al ejercito."""

def aspirante (sexo,estatura,edad):
    #estaturam= range(1.60)
    #if sexo!= "mujer" or sexo=="Mujer" or sexo== "F" or sexo == "Femenino" or sexo=="hombre" or sexo=="Hombre" or sexo== "M" or sexo == "Masculino":
      #  return "Sexo inválido,los valores a ingresar son: F o M"
    if estatura<0:
        return "Estatura inválida"
    if edad<0:
        return "Estatura inválida"
    edadm= edad>=20 and edad<=25
    #if (sexo== "mujer" or sexo=="Mujer" or sexo== "F" or sexo == "Femenino") and (estatura>1.60) and (edad>=20 and edad<=25) :
    if (sexo=="mujer"):
        if estatura>1.60 and edadm :
            return "Pasó al ejercito,es mujer"
    #elif sexo== "hombre" or sexo=="Hombre" or sexo== "M" or sexo == "Masculino":
       # if estatura>1.65 and (edad>=18 and edad<=24):
          #  return "pasó al ejercito,es hombre"

print (aspirante("mujer",1.50,20))
print (aspirante("M",1.60,20))
print (aspirante("hombre",160,20))
