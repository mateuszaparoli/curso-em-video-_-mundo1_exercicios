#Conversor de temperaturas

tc = float(input('Informe a temperatura em °C: '))
f = ((9*tc)/5)+32
k = tc+273
print('A temperatura de {}°C corresponde a {}°F e a {}K.'.format(tc, f, k))