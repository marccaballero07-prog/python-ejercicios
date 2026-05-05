num1 = float(input("Introduce el primer número (0-10): "))
num2 = float(input("Introduce el segundo número (0-10): "))

if num1 < 0 or num1 > 10 or num2 < 0 or num2 > 10:
    print("Uno o los dos números están fuera de los límites establecidos")
else:
    if num1 > num2:
        print("El número", num1, "es mayor que el número", num2)
    elif num2 > num1:
        print("El número", num2, "es mayor que el número", num1)
    else:
        print("Ambos números son iguales")
