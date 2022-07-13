#Programa que calcula o salário de um funcionário e seu aumento. Para salários acima de R$1250,00 aumenta 10%, menor ou = o aumento será de 15%
s =float(input('Qual o salário do funcionário? R$'))
if s>1250:
    print('Com 10% de aumento, o salário passará a ser: R${:.2f}'.format(s*0.10+s))
else:
    print('Com 15% de aumento, o salário passará a ser: R${:.2f}'.format(s*0.15+s))