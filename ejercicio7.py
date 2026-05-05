num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
    print("El número", num1, "es mayor que el número", num2)
elif num2 > num1:
    print("El número", num2, "es mayor que el número", num1)
else:
    print("Ambos números son iguales")
