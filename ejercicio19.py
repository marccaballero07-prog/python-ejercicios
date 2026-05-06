a = int(input("Introduce el primer intervalo: "))
b = int(input("Introduce el segundo intervalo: "))

resultado = ""

if a < b:
    for i in range(a, b + 1):
        resultado += str(i) + "-"
else:
    for i in range(a, b - 1, -1):
        resultado += str(i) + "-"

print(resultado[:-1])  
