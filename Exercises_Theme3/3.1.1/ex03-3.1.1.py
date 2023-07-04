# Implementar uma solução que resolva a seguinte questão:
# Calcular o valor de uma compra, sendo que o preço unitário é R$10,00
# - até 10 unidades, não há desconto
# - entre 11 e 20 unidades, o desconto é de 10%
# - acima de 20 unidades, desconto de 20%

unidades = eval(input('Digite a quantidade que quer comprar'))
valor = unidades * 10
if (unidades <= 10):
    valor = valor
elif (unidades <= 20):
    valor = valor * 0.9
else:
    valor = valor * 0.8

print(f'Valor total da compra: {valor}')
