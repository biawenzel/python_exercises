# Implementar uma solução que faça o tratamento de exceção para verificar se uma entrada é numérica
# Além disso, insista que o usuário digite um número válido

while True:
    try:
        x = int(input("Digite um número: "))
        break
    except ValueError:
        print("Entre com um número válido")
