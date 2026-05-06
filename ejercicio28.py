lista = []
repetir = "s"

while repetir == "s":
    letra = input("Introduce una letra: ")

    if letra not in lista:
        lista.append(letra)

    repetir = input("¿Deseas repetir s/n: ").lower()

print(lista)
