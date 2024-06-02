'''Escreva uma programa que solicita ao usuário uma temperatura em Celsius, converta para Fahrenheit e exiba o resultado.
A fórmula é: Fahrenheit = (Celsius * 9/5) + 32''' 

temp_celsius = int(input('Escreva a temperatura em Celsius: '))
conversao = (temp_celsius * 9/5) + 32

print('Este é o resultado em Fahrenheit: ', conversao)