#!/usr/bin/python3
#_*_ coding: utf-8 _*_


"""
  multiplicador.py
  Multiplica dos numeros sense fer servir *
"""

__author__ = "Iker Rus"



import doctest
import sys

def multiplica(a, b):

    """
    >>> multiplica(2, 2)
        4
    >>> multiplica (2)
    Per a multiplicar, introdueix dos numeros
    """
    total = 0
    for i in range(abs(b)):
        total += a if b > 0 else -a
    return total

def ayuda():
    print("Per a multiplicar, introdueix dos numeros")

if __name__ == __name__:
    try:
        num1 =int(sys.argv[1])
        num2 =int(sys.argv[2])
        total = multiplica(num1, num2)
        print(f"El resultat es {total}")
    except:
        ayuda()


