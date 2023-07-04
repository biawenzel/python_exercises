# Implementar uma solução que verifique se um número é par ou ímpar

numero: int = eval(input("Digite um número inteiro"))
numero %= 2

if (numero == 0):
    print("O número é par.")
else:
    print("O número é ímpar.")

