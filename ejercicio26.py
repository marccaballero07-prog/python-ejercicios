import random

uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0

for i in range(100):
    tirada = random.randint(1, 6)

    if tirada == 1:
        uno += 1
    elif tirada == 2:
        dos += 1
    elif tirada == 3:
        tres += 1
    elif tirada == 4:
        cuatro += 1
    elif tirada == 5:
        cinco += 1
    else:
        seis += 1

print("Uno:", uno)
print("Dos:", dos)
print("Tres:", tres)
print("Cuatro:", cuatro)
print("Cinco:", cinco)
print("Seis:", seis)
