numcajas=9
latas_caja=24
personas= 56
n_totallatas= numcajas*latas_caja
n_latasporpersona=(n_totallatas//personas)
n_latasSobrantes = (n_totallatas-(n_latasporpersona*personas))
print("La cantidad de latas que cada persona va a tomar es de "+ str(n_latasporpersona), "La cantidad de latas sobrantes es de "+str(n_latasSobrantes) )
