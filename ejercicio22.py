repetir = "s"

while repetir == "s":
    n1 = int(input("Introduce un número: "))
    n2 = int(input("Introduce otro número: "))

    print("El resultado de la suma es:", n1 + n2)

    repetir = input("¿Deseas repetir la operación s/n: ").lower()

print("Programa finalizado")