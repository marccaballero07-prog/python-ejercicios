import random

lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]

secreta = random.choice(lista)
palabra = ""

while palabra != secreta:
    palabra = input("Introduce la palabra secreta: ")
    if palabra != secreta:
        print("SIGUE JUGANDO")

print("ACERTASTE")
