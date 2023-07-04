# Implementar uma solução que determine se um número é primo ou não primo (primo = divisível por 1 e ele mesmo)

def eh_primo(n):
    if (n < 2):
        return False
    i = n // 2  # divisão inteira (//)
    while (i > 1):
        if (n % i == 0):
            return False
        i -= 1
    return True


def imprimir_resultado(numero, resultado):
    mensagem = f'O número {numero} NÃO é primo.'
    if (resultado):
        mensagem = f'O número {numero} é primo.'
    return mensagem


numero = 5
resultado = eh_primo(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)

