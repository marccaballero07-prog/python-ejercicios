repetir = "s"
repeticiones = 0
suma_total = 0

while repetir == "s":
    n1 = int(input("Introduce un número: "))
    n2 = int(input("Introduce otro número: "))

    resultado = n1 + n2
    print("El resultado de la suma es:", resultado)

    repeticiones += 1
    suma_total += resultado

    repetir = input("¿Deseas repetir la operación s/n: ").lower()

print("Mensaje: Resumen.")
print("La suma total es:", suma_total, "y el número de repeticiones es:", repeticiones)
