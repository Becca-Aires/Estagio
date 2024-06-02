'''Faça um programa que calcula o Índice de Massa Corporal (IMC) do usuário.
A fórmula é: IMC = peso / altura².'''

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))

imc = peso / (altura**2)

print('O resultado do Índice de Massa Corporal', imc)