#Calculando Descontos

pi = float(input('Qual o preço original do produto? R$'))
d = float(input('Qual o valor (em porcentagem) do desconto? '))
pf = pi*(1-(d/100))
print('O produto que custava R${:.2f} com um desconto de {:.1f}'.format(pi, d), '%', 'custará R${:.2f}!'.format(pf))