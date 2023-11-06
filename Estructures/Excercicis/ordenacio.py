#Author Iker

# _*_ coding: utf-8 _*_
"""
ordenacio.py

programa ordena una llista de nombres introduits per l'usuari
"""

__author__   = "Iker"

def main(llista):

    for index in range(len(llista)):
        for x in range(len(llista)):
            if llista[index] < llista[x]:
                llista[index], llista[x] = llista[x], llista[index]

if __name__ == "__main__":
    llista = input("Introdueix els números separats per comes: ").split(",")
    llista = [int(i) for i in llista]
    main(llista)
    print(llista)                   

