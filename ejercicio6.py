peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

imc = peso / (altura ** 2)

print("Si pesas", peso, "kilos y mides", altura, "tu IMC es:", round(imc, 2))

if imc >= 25:
    print("Hay sobrepeso")
