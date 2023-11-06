#!/usr/bin/python3
#_*_ coding: utf-8 _*_


"""
  edat_gos.py
  Calclul anys de gos
"""

__author__ = "Iker Rus"


edat_huma = int(input('Introdueix els anys humans: '))


if edat_huma < 3:
	edat_gos = edat_huma * 10.5
	print(edat_huma, ' anys humans equivalen a ', edat_gos, ' anys de gos.' )
else:
	edat_gos = (edat_huma - 2) * 4 + 21
	print(edat_huma, ' anys humans equivalen a ', edat_gos, ' anys de gos')
