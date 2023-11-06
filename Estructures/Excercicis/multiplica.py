#!/usr/bin/python3
#_*_ coding: utf-8 _*_


"""
  Multiplicador
"""

__author__ = "Iker Rus"


import sys

def multiplica(a, b):
    """
    Aquesta funció calcula la multiplicació de dos nombres fent iteracions de sumes.
    
    :param a: Primer nombre a multiplicar
    :param b: Segon nombre a multiplicar
    :return: Resultat de la multiplicació
    """
    result = 0
    for i in range(abs(b)):
        result += a if b > 0 else -a
    return result

def help_message():
    """
    Aquesta funció mostra un missatge d'ajuda quan sigui necessari.
    """
    print("Ús: multiplicador.py [nombre1] [nombre2]")
    print("Aquest programa calcula la multiplicació de dos nombres fent iteracions de sumes.")
    print("Exemple: multiplicador.py 5 3")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        help_message()
    else:
        try:
            num1 = int(sys.argv[1])
            num2 = int(sys.argv[2])
            result = multiplica(num1, num2)
            print(f"El resultat de la multiplicació és: {result}")
        except ValueError:
            print("Error: Siusplau, introduïu dos nombres enters com a arguments.")
