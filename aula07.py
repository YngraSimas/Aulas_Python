#faça um programa que peça 2 números inteiros e 1 número real e mostre:
#a) o produto do dobro do primeiro número com a metade do segundo número: (n*2) * (m/2)
# produto == multiplicação
#b) a soma do triplo do primeiro número com o terceiro número: n*3+p
#c) o terceiro número elevado ao cubo: p**3
#número real == /R, formado pela junção de 2 conjuntos: número racional,(Q),
# representado por fração e número irracional,(I), seu padrão não é possível
# ser representado por fração


def pdm(n, m):
    a = (n*2) * (m/2)
    return a


def st(n, p):
    a = n * 3 + p
    return a


def c(p):
    a = p ** 3
    return a


entrada_1 = int(input("Digite um número inteiro: "))
entrada_2 = int(input("Digite outro número inteiro: "))
entrada_3 = float(input("Digite um número real: "))
print(f"O produto do dobro do número {entrada_1} com a metade do número "
f"{entrada_2} é:", pdm(entrada_1, entrada_2))
print(f"A soma do triplo do número {entrada_1} com o número {entrada_3} "
      f"é:", st(entrada_1, entrada_3))
print(f"O terceiro número elevado ao cubo é igual a:", c(entrada_3))