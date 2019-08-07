# faça um programa que some 4 notas e apresente a média


def media_nota(y, n, g, r):
    a = float(y + n + g + r) / 4
    return a


entrada_1 = float(input("digite a primeira nota: "))
entrada_2 = float(input("digite a segunda nota: "))
entrada_3 = float(input("digite a terceira nota: "))
entrada_4 = float(input("digite a quarta nota: "))
print(f"a média entre {entrada_1} e {entrada_2} e {entrada_3}"
      f" e {entrada_4} é:", media_nota(entrada_1, entrada_2, entrada_3, entrada_4))
