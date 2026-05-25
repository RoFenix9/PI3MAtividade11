def calcular_raiz(n, x):
    resultado = n ** (1 / x)
    return resultado

n = float(input("Digite o radicando: "))
x = float(input("Digite a ordem da raiz: "))

print("Resultado:", calcular_raiz(n, x))
