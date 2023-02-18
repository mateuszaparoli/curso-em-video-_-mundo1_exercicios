#Aluguel de Carros

print('-'*10, 'Calculadora de aluguel de carros', '-'*10)
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram percorridos com o carro nesse período? '))
p = (60*dias) + (0.15*km)
print('O preço a ser pago pelo aluguel é de R${:.2f}'.format(p))