from cgitb import reset


valor = float(input('Digite o valor do produto: R$ '))
desc = valor - (valor * 5 / 100)
print('O valor do produto é de R${}, com os 5% de desconto fica R${:.2f}'.format(valor, desc))