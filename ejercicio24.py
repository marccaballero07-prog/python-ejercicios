acumulado = 0
operaciones = 0

while acumulado <= 50:
    n1 = int(input("Introduce un número: "))
    n2 = int(input("Introduce otro número: "))

    resultado = n1 + n2
    acumulado += resultado
    operaciones += 1

    print("El resultado de la suma es:", resultado)

    if operaciones == 1:
        print("El total acumulado es:", acumulado, "y llevas", operaciones, "operación realizada")
    else:
        print("El total acumulado es:", acumulado, "y llevas", operaciones, "operaciones realizadas")

print("Fin del programa")
