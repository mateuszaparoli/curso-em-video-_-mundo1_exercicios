#Reajuste Salarial

si = float(input('Qual é seu salário atual? R$'))
a = float(input('De quantos % será seu aumento? '))
sf = si*(1+(a/100))
print('Seu salário, após o aumento de {:.2f}%, será de R${:.2f}'.format(a, sf))