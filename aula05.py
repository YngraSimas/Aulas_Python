# faça um  programa que transforme metros em cm


def metro_cm(y):
    a = float(y*100)
    return a


entrada_1 = float(input("informe quanto(s) metro(s): "))
print(f"a conversão de {entrada_1}m é de: {metro_cm(entrada_1)}cm")