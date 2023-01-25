"""
Crie um programa que recebe um número e imprima seu fatorial.
Método 5Q's para montar um algorítimo:
Analise criticamente o problema e descubra:
1. Quais os dados de entrada necessários?
Número para cálculo
2. O que devo fazer com esses dados?
Calculo fatorial do número dado
3. Quais as restrições desse problema?
O número não pode ser negativo e deve ser inteiro
4. Qual o resultado esperado?
Impressão do fatorial do número dado
5. Qual a sequência de passos para chegar ao resultado esperado (pseudo código)?
input do número
if número > 0
if número não é inteiro
fatorial = 1
loop de 1 até número
    fatorial = fatorial * 1
"""

print('Cálculo Fatorial')

num = int(input('Digite um número: '))
if num > 0:
    fatorial = 1
    for c in range(1, num + 1):
        fatorial = fatorial * c
    print(fatorial)
else:
    print('valor inválido')
