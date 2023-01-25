print('TESTE DE FUNÇÕES')

print('Olá, meu nome é Hal')

nome = input('Qual o seu nome? ')

print('Prazer em te conhecer ', nome, '!')

hoje = int(input('Em que ano estamos hoje? '))

dia = int(input('Que dia você nasceu? '))

mes = input('Que mês você nasceu? ')

ano = int(input('Que ano você nasceu? '))

print('Você nasceu em', dia, 'de', mes, 'de', ano, ', correto?')

idade = hoje-ano

print('Você tem ', idade, '')

if idade < 18:
    print('Você é menor de idade')

elif idade > 18:
    print('Você é maior de idade')
    print('Está velho! kkkkkk')
            
print('Pergunte para mim uma multiplicação que te direi a resposta!')

print('Qual o primeiro número?')

n1 = int(input('primeiro número '))

print('Qual o segundo número?')

n2 = int(input('segundo número '))

mult = n1*n2

print('A resposta é', mult, '')

print('Sou mais inteligente do que você ;D')
