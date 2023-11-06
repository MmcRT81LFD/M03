#!/usr/bin/python3
#_*_ coding: utf-8 _*_


"""
  edat_gos.py
  Calclul anys de gos
"""

__author__ = "Iker Rus"



def main():
    opcioJug1, opcioJug2  = "",""

    while opcioJug1 != "sortir" and opcioJug2 != "sortir":
        
        print("Jugador 1, seleccioni opcio\n")
        print("Pedra")
        print("Paper")
        print("Tissora")
        print("\nSortir")
        opcioJug1 = input()
        print("\n")

        print("Jugador 2, seleccioni opcio\n")
        print("Pedra")
        print("Paper")
        print("Tissora")
        print("\nSortir")
        opcioJug2 = input()
        print("\n")


        if opcioJug1 == "pedra" and opcioJug2 == "pedra":
            print("Empat!")
        elif opcioJug1 == "tissora" and opcioJug2 == "tissora":
            print("Empat!")
        elif opcioJug1 == "paper" and opcioJug2 == "paper":
            print("Empat!")

        elif opcioJug1 == "pedra" and opcioJug2 == "paper":
            print("Guanya Jugador 2")
        elif opcioJug1 == "pedra" and opcioJug2 == "tissora":
            print("Guanya Jugador 1")

        elif opcioJug1 == "paper" and opcioJug2 == "pedra":
            print("Guanya Jugador 1")
        elif opcioJug1 == "paper" and opcioJug2 == "tissora":
            print("Guanya Jugador 2")

        elif opcioJug1 == "tissora" and opcioJug2 == "paper":
            print("Guanya Jugador 1")
        elif opcioJug1 == "tissora" and opcioJug2 == "pedra":
            print("Guanya Jugador 2")


        elif opcioJug1 != "pedra" and "paper" and "tissora" and "sortir" and opcioJug2 == "pedra" and "paper" and "tissora" and "sortir":
            print("El jugador 1 ha introduit un valor erroni")
            print("Guanya Jugador 2")
        elif opcioJug2 != "pedra" and "paper" and "tissora" or "sortir" and opcioJug1 == "pedra" and "paper" and "tissora" and "sortir":
            print("l jugador 2 ha introduit un valor erroni")
            print("Guanya Jugador 1")
        elif opcioJug1 != "pedra" and "paper" and "tissora" and "sortir" and opcioJug2 != "pedra" and "paper" and "tissora" and "sortir":
            print("Els dos jugadors han introduit un valor incorrecte")
            print("Empat!")
if __name__ == __name__:
    main()
