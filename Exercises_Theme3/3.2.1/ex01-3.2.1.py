# Implementar uma solução que retorne a soma de todos os elementos pares de uma lista

def soma_pares(list):
    soma = 0
    for i in list:
        if (i % 2 == 0):
            soma += i
    return soma


lista = [0, 1, 2, 3, 4, 5]
soma = soma_pares(lista)
print(f'A soma dos elementos pares é: {soma}')
