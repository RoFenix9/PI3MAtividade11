def contar_digitos(numero):
    contador = 0

    if numero == 0:
        return 1

    while numero > 0:
        numero = numero // 10
        contador += 1

    return contador

numero = int(input("Digite um número inteiro: "))

print("Quantidade de dígitos:", contar_digitos(numero))
