#Faça um programa que peça dois números e informe a soma


def soma(y, n):
    a = y + n
    return a


entrada_1 = int(input("digite um número inteiro: "))
entrada_2 = int(input("digite outro número inteiro: "))
print(f"a soma entre {entrada_1} e {entrada_2} é:", soma(entrada_1, entrada_2))
