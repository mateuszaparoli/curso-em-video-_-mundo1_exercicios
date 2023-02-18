#Conversor de Moedas

print('-'*10,'BEM VINDO AO CONVERSOR DE MOEDAS 5G', '-'*10)

n = float(input('Qual o valor em reais você quer converter? ' ))
m = (input('Para qual moeda você deseja converter(euro, dolar)? '))

dolar = n/5.24
euro = n/5.53

if (m == 'dolar'):
    print('R${:.2f} = {:.2f}dolares'.format(n, dolar))
else:
    print('R${:.2f} = {:.2f}euros'.format(n, euro))
