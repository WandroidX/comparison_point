import random

personas = 40
valores = []
suma_valores = 0

while suma_valores != personas:
    cantidad_muestras = random.randint(4, 8)
    for muestra in range(0, cantidad_muestras):
        numero = random.randint(1, 10)
        valores.append(numero)
        suma_valores = sum(valores)
    if suma_valores != personas:
        valores = []

    else:
        print(suma_valores)
print(valores)
