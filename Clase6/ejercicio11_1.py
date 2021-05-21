
def aspirantes (sexo,edad,estatura):
    if sexo=="F": 
        if estatura>1.60 and edad>=20 and edad<=25:
            return "Es mujer y es apta para el ejército"
    else :
        return "no es apta"

print(aspirantes("F",20,1.60))
        