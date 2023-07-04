# Implementar uma solução para a seguinte questão:
# - se a nota for >= 7, estudante aprovado
# - se a nota for < 7 e >= 5, estudante de recuperação
# - se a nota for < 5, estudante reprovado

nota: float = eval(input('Insira sua nota'))
if (nota >= 7.0):
    print('Pessoa aprovada')
elif (nota < 5.0):
    print('Pessoa reprovada')
else:
    print('Pessoa em recuperação')
    