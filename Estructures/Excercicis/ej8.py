#!/usr/bin/python3

"""
  hello.py
  Calclul beneficis
"""

__author__ = "Iker"


punts = float(input('Introdueixi el seus punts: '))
sou = 2400


if punts == 0:
	print('Inaceptable')
	sou = sou * 0
	print ('Benefici: ', sou, ' €')
elif punts == 0.4:
	print('Aceptable')
	sou = sou * 0.4
	print ('Benefici: ', sou, ' €')
elif punts > 0.6:
	print('Meritoso')
	sou = sou * punts
	print('Benefici: ', sou, ' €')
else:
	print('Punts introduits incorrectes')
