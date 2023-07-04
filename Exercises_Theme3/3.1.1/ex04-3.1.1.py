# Implementar uma solução que some todos os números pares de uma lista
# Por exemplo: se a lista for [10, 2, 5, 7, 6, 3] o resultado deve ser 18

# 1ª opção
lista = [2, 6, 8, 3, 7, 10]
n = len(lista) # len devolve o comprimento da lista
soma = 0
for i in range(n):
    if (lista[i]%2 == 0):
        soma = soma + lista[i]
print(f'O somatório dos elementos pares da lista é: {soma}')

# 2ª opção
list = [2, 4, 4, 9]
sum = 0
for num in list:
    if (num%2==0):
        sum = sum + num
print(f'O somatório dos elementos pares da lista é: {sum}')
