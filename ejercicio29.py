lista1 = ['a','b','D','x','r','X','3','h','w','i','2','i']

total = len(lista1)
numeros = 0
letras = 0
mayusculas = 0
suma_numeros = 0

for valor in lista1:
    if valor.isdigit():
        numeros += 1
        suma_numeros += int(valor)
    else:
        letras += 1
        if valor.isupper():
            mayusculas += 1

print("Número de valores:", total)
print("Cantidad de números:", numeros)
print("Cantidad de letras:", letras)
print("Cantidad de mayúsculas:", mayusculas)
print("Suma total de números:", suma_numeros)
