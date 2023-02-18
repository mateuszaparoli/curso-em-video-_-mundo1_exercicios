#Média Aritmética

n1 = float(input('Sua primeira nota: '))
n2 = float(input('Sua segunda nota: '))
n = (n1 + n2)/2

if(n > 6):
    print('Parabéns, sua nota é: {:.1f} e você foi aprovado no curso!'.format(n))
else:
    print('Sinto muito, sua nota é: {:.1f} e você reprovou nessa matéria'.format(n))