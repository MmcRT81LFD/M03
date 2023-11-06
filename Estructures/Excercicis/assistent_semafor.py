#!/usr/bin/python3
#_*_ coding: utf-8 _*_


"""
  assistent_semafor.py
  Intstruccion de que fer en cas de trobar-nos amb un semadfor
"""

__author__ = "Iker Rus"

import sys
import doctest



def main(color):


    """
    Comprovacio de funcionament.

    >>> main("verd")
    Passa
    >>> main("groc")
    Corre!
    >>> main("vermell")
    Espera
    >>> main("")
    Ves a l'oculista
    """

    if color == "verd":
        print("Passa")
    elif color == "groc":
        print("Corre!")
    elif color == "vermell":
        print("Espera")
    else:
        print("Ves a l'oculista")



if __name__ == __name__:
    main(sys.argv[1])
