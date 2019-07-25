def soma(y, n):
    a = y + n
    return a


print(soma(1, 1))


def subtracao(y, n):
    a = y - n
    return a


print(subtracao(1, 2))


def multiplicacao (y, n):
    a = y * n
    return a

print(multiplicacao(2, 3))


def divisao (y, n):
    a = y / n
    return a

print (divisao(3, 2),type(divisao(3, 2)))


def potencia (y, n):
    a = y ** n
    return a

print(potencia(4, 5))


def divisao_inteira(y, n):
    a = y // n
    return a

print(divisao_inteira(11, 3))

def resto_da_divisao(y,n):
    #o que resta da divisao inteira
    #exemplo: 11/3= 3 e o resto= 2
    a = y % n
    return a

print(resto_da_divisao(11, 3))

def diferenca(y,n):
    a = y != n
    return a

print(diferenca(7, 11))