"""Crea un programa que dado un número entero que designa un periodo de tiempo 
expresado en segundos, imprima el equivalente en días, horas, minutos y segundos.
Por ejemplo:

300000 segundos serán 3 días, 11 horas, 20 minutos y 0 segundos.
7400 segundos serán 0 días, 2 horas, 3 minutos y 20 segundos."""

n_tiempo= int (input("Ingrese el número en segundos "))
minuto=60
hora= 3600
dia= 86400
dias= n_tiempo