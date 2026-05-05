caracter = input("Introduce un carácter: ")

if caracter.islower():
    print("La letra es minúscula")

elif caracter.isupper():
    print("La letra es mayúscula")

elif caracter.isnumeric():
    print("El valor introducido es un número")

else:
    print("El valor introducido es un símbolo")
