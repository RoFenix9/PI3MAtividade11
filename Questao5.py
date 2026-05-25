def verificar_palindromo(texto):
    if texto == texto[::-1]:
        return True
    else:
        return False

palavra = input("Digite uma palavra: ")

print(verificar_palindromo(palavra))
