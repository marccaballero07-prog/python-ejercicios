import random

secreto = random.randint(1, 10)
numero = 0

while numero != secreto:
    numero = int(input("Introduce un número: "))
    if numero != secreto:
        print("Sigue intentando")

print("Acertaste")
