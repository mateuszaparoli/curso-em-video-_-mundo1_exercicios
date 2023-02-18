#Pintando Parede

print('-'*10, 'Calculadora de tinta(use somente valores em m²)', '-'*10)

l = float(input('Largura da parede: '))
c = float(input('Comprimento da parede: '))
a = l*c
t = a/2

print('Sua parede tem dimensão de {}x{} e área de {}m²\nPara pintá-la você precisará de {}L de tinta.'.format(c, l, a, t))