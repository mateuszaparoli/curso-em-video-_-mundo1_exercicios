#Conversor de medidas

n = float(input('Qual o valor em metros a ser convertido? '))

print('{:.1f}m em cm vale {:.0f}cm, em mm vale {:.0f}, em dm vale {:.0f}, em dam {:.4f}, em hm {:.4f} e em km {:.5f} de nada!'.format(n, n*100, n*1000, n*10, n/10, n/100, n/1000))