#!/usr/bin/python3        
# _*_ coding: utf-8 _*_   

"""
    Ens indica el color d'una posició a un escaquer.
    Exemple d'ús:
    python3 color_posicio.py b3
    blanc  
"""

__author__ = "Xavi Quesada"  #-> Qui ha creat el programa.

import sys
COLOR_CLAR = "blanc"
COLOR_FOSC = "negre"

def main(posicio):
    """
    És el punt d'entrada al nostre programa
    >>> main("a1")
    negre
    >>> main("h8")
    negre
    >>> main("b3")
    blanc
    >>> main("e7")
    negre
    >>> main("g2")
    blanc
    >>> main("j2")
    ===================================
    Entrada invàlida.
    Necessites introduïr una posició.
    Ex: $ python3 color_posicio.py b3
    blanc
    ===================================
    >>> main("g9")
    ===================================
    Entrada invàlida.
    Necessites introduïr una posició.
    Ex: $ python3 color_posicio.py b3
    blanc
    ===================================
    """

    color_inicial = COLOR_FOSC
    color_alternatiu = COLOR_CLAR
    color_posicio = ""

    columnes_que_comencen_blanques = ["b", "d", "f", "h"]
    columna = posicio[0]
    fila = int(posicio[1:])

    if fila>=9 or columna>="i":
        print("===================================")
        print("Entrada invàlida.")
        print("Necessites introduïr una posició.")
        print("Ex: $ python3 color_posicio.py b3")
        print("blanc")
        print("===================================")
    else:
        if columna in columnes_que_comencen_blanques:
            if fila % 2 == 0:
                color_posicio="negre"
            else:
                color_posicio="blanc"
        elif fila:
            if fila % 2 == 0:
                color_posicio="blanc"
            else:
                color_posicio="negre"

        print(color_posicio)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("===================================")
        print("Necessites introduïr una posició.")
        print("Ex: $ python3 color_posicio.py b3")
        print("blanc")
        print("===================================")
    else:
        main(sys.argv[1])
