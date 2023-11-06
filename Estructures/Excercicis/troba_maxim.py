#!/usr/bin/python3
# _*_ coding: utf-8 _*_

"""
troba_maxim.py rep números naturals de forma seqüencial i termina al rebre un de negatiu.
Al terminar informa de quin ha estat el nombre més gran introduït.
"""
__author__   = "Iker"
__email__    = "f1vw3k71e8@proton.me"
__license__  = "GPL V3"

def main():
    num = 0
    maxim = None
    while num >= 0:
        num = int(input("Introdueix un número natural: "))
        if num >= 0:
            maxim = num
    return maxim

if __name__ == "__main__":
    print(f"El màxim ha estat: {main()}")

