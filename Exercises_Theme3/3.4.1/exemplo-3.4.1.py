# Implementar uma solução que faça o tratamento de exceção pra verificar se a entrada é realmente um número

try:
    x = int(input("Digite um número: "))
except ValueError:
    print("Entre com um número válido")
