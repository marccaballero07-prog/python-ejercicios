pares = 0
impares = 0

for numero in range(1, 51):
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("El total de pares es:", pares)
print("El total de impares es:", impares)
