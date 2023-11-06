#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import sys

"""
qualificacions.py demana noms de mòduls i nota. Al final calcula nota mitja de cicle.
"""
__author__   = "Iker"

def main():
    """
    Funció principal: rep els noms i les qualificacions dels mòduls i 
    retorna la nota mitja.
    """
    nom_modul = None
    nota_acumulada = 0
    comptador_de_moduls = 0

    while nom_modul != "":
        nom_modul = input("Introdueix el nom del mòdul: ")

        if nom_modul != "":
            try:
                nota = float(input(f"Introdueix la nota de {nom_modul}: "))
                nota_acumulada += nota
                comptador_de_moduls += 1
            except ValueError:
                print("La nota ha de ser un número enter.")
                sys.exit(1)

    if comptador_de_moduls != 0:
        return nota_acumulada / comptador_de_moduls
    return None

if __name__ == "__main__":
    print(main())