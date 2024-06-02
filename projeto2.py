'''Faça um programa que solicita um número ao usuário e verifica se esse número é par ou ímpar e exiba a resposta.'''

numero = int(input('\nDigite qualquer número para verificar se é ímpar ou par: '))
if numero % 2 == 0:
    print('Número par')
else:
    print('Número ímpar')