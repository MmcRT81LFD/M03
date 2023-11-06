import doctest
import sys

def multiplica(a, b):
    total = 0

    for i in range(abs(a)):
        total += a if b > 0 else -a
    print(f"El resultat es {total}")
    return total

def ayuda():
    print("Per a multiplicar, introdueix dos numeros")

if __name__ == __name__:
    try:
        num1 =int(sys.argv[1])
        num2 =int(sys.argv[2])
        multiplica(num1, num2)
    except:
        ayuda()


