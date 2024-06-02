'''Escreva um programa que solicita três números do usuário, encontre e exiba o maior número fornecido.'''

numero = int(input('Digite um número: '))
numero2 = int(input('Digite um número novamente: '))
numero3 = int(input('Digite um número para finalizar: '))

if numero > numero2 and numero > numero3:
    print('Número 1 é maior :', numero)

elif numero2 > numero and numero2 > numero3:
    print('Número 2 é maior :', numero2)

else: 
    print('Número 3 é maior: ', numero3)