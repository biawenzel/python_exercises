# Implementar uma solução que calcule o fatorial de um número [n! = n(n-1)!]

# Estratégia 1
def fatorial_iterativo(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


# Estratégia 2
def fatorial_recursivo(num):
    if (num == 0) or (num == 1):
        return 1
    return num*fatorial_recursivo(num-1)


numero = 5
print(f'O fatorial do número {numero} é: {fatorial_iterativo(numero)}')
print(f'O fatorial do número {numero} é: {fatorial_recursivo(numero)}')