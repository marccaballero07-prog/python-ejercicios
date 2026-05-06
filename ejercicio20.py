pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0
suma_total = 0

numero = int(input("Introduce un número: "))

while numero != -99:

    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

    suma_total += numero

    numero = int(input("Introduce un número: "))

print("RESUMEN")
print("El número de pares es", pares)
print("El número de impares es", impares)
print("El número de positivos es", positivos)
print("El número de negativos es", negativos)
print("El número de ceros es", ceros)
print("El total es", suma_total)
