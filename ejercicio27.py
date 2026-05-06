cantidad = int(input("¿Cuántos números quieres introducir? "))

lista = []

for i in range(cantidad):
    numero = int(input("Introduce un número: "))
    lista.append(numero)

lista.sort()

print(lista)
