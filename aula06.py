# faça um programa que para um raio mostre perímetri, área e volume
# área == Pi x R²
# perímetro == 2 x Pi x R
# Volume == 4 x Pi x R³ / 3
import math


def area(y):
    a = math.pi * y**2
    return a


def perimetro(n):
    a = 2 * math.pi * n
    return a


def volume(g):
    a = (4 * math.pi * g**3) / 3
    return a


entrada_1 = float(input("informe o raio: "))
print(f"a área é: {area(entrada_1):.3f}")
print(f"o perímetro é: {perimetro(entrada_1):.3f}")
print(f"o volume é: {volume(entrada_1):.3f}")
