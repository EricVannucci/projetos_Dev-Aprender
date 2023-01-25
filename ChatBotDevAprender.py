# Introdução
print('Olá, seja bem-vindo à DevAprender!')
nome = str(input('Digite seu nome: ')).strip().title()
email = str(input('Digite seu e-mail: ')).strip()

# Menu
print(f'{nome}, sobre o que você gostaria de saber hoje?\n')
print('\033[96m=-\033[m' * 35)
print('[1] - Vale a pena aprender Python?\n'
      '[2] - Quanto tempo leva-se para conseguir um emprego com Python?\n'
      '[3] - Quando eu vou saber que estou BOM para conseguir um emprego?\n'
      '[4] - Onde me recomenda estudar Python para conseguir um emprego hoje?\n'
      '[5] - Sair')
print('\033[96m=-\033[m' * 35)

# Escolha do usuário
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print(' Na minha visão vale muito apena, isso porque Python é uma das linguagens que mais cresce\n'
          ' no mundo e possui salários mensais que vão desde R$2100,00 a até mais R$10000,00 no Brasil,\n'
          ' além de contar com uma média anual de $85.000 dólares nos EUA.\n')
elif opcao == 2:
    print(' Isso varia muito com o nível de esforço, dedicação e busca diária por vagas de cada indivíduo.\n'
          ' Alguns conseguem com menos de 3 meses e outros com mais, tudo depende do quanto você já sabe\n'
          ' ou está disposto a correr atrás para aprender.\n')
elif opcao == 3:
    print(' Primeiro entenda, ninguém vai te dizer ou chegar magicamente um dia e te dizer que você está\n'
          ' BOM o suficiente para conseguir um emprego ou fazer dinheiro com seu conhecimento de \n'
          ' programação, seja em Python ou qualquer outra linguagem ou habilidade, você simplesmente tem\n'
          ' que começar dar a sua cara a tapa e começar a aplicar para oportunidades ou até mesmo começar\n'
          ' a criar elas, desde o dia que você já domina os fundamentos de uma linguagem (se estamos falando\n'
          ' de Python, recomendo aprender no mínimo os 5 pilares de programação.\n')
elif opcao == 4:
    print(' Você pode estudar através de vídeos gratúitos no YouTube, livros e sites de programação,\n'
          ' porém se buscar um lugar com suporte 1 a 1, estrutura sequencial, projetos novos todos os\n'
          ' meses dos ano e um curso que vai te ensinar toda a base e habilidades mais lucrativas que\n'
          ' precisa para criar aplicações em python e estar pronto para o mercado, recomendo o\n'
          ' cursodepython.net\n')
elif opcao == 5:
    print('Até logo, espero ter ajudado! Outras dúvidas escreva para devaprender@hotmail.com')
    exit()
else:
    print('\033[31mOpção inválida, tente novamente!\033[m\n')
# Loop Menu


def start():
    print(f'{nome}, sobre o que mais você gostaria de saber hoje?\n')
    while True:
        print('\033[96m=-\033[m' * 35)
        print('[1] - Vale a pena aprender Python?\n'
              '[2] - Quanto tempo leva-se para conseguir um emprego com Python?\n'
              '[3] - Quando eu vou saber que estou BOM para conseguir um emprego?\n'
              '[4] - Onde me recomenda estudar Python para conseguir um emprego hoje?\n'
              '[5] - Sair')
        print('\033[96m=-\033[m' * 35)
# Nova escolha do usuário

        opcao1 = int(input('Digite sua opção: '))
        if opcao1 == 1:
            print(' Na minha visão vale muito apena, isso porque Python é uma das linguagens que mais cresce\n'
                  ' no mundo e possui salários mensais que vão desde R$2100,00 a até mais R$10000,00 no Brasil,\n'
                  ' além de contar com uma média anual de $85.000 dólares nos EUA.\n')
        elif opcao1 == 2:
            print(' Isso varia muito com o nível de esforço, dedicação e busca diária por vagas de cada indivíduo.\n'
                  ' Alguns conseguem com menos de 3 meses e outros com mais, tudo depende do quanto você já sabe\n'
                  ' ou está disposto a correr atrás para aprender.\n')
        elif opcao1 == 3:
            print(' Primeiro entenda, ninguém vai te dizer ou chegar magicamente um dia e te dizer que você está\n'
                  ' BOM o suficiente para conseguir um emprego ou fazer dinheiro com seu conhecimento de \n'
                  ' programação, seja em Python ou qualquer outra linguagem ou habilidade, você simplesmente tem\n'
                  ' que começar dar a sua cara a tapa e começar a aplicar para oportunidades ou até mesmo começar\n'
                  ' a criar elas, desde o dia que você já domina os fundamentos de uma linguagem (se estamos falando\n'
                  ' de Python, recomendo aprender no mínimo os 5 pilares de programação.\n')
        elif opcao1 == 4:
            print(' Você pode estudar através de vídeos gratúitos no YouTube, livros e sites de programação,\n'
                  ' porém se buscar um lugar com suporte 1 a 1, estrutura sequencial, projetos novos todos os\n'
                  ' meses dos ano e um curso que vai te ensinar toda a base e habilidades mais lucrativas que\n'
                  ' precisa para criar aplicações em python e estar pronto para o mercado, recomendo o\n'
                  ' cursodepython.net\n')
        elif opcao1 == 5:
            print('Até logo, espero ter ajudado! Outras dúvidas escreva para devaprender@hotmail.com')
            exit()
        else:
            print('\033[31mOpção inválida, tente novamente!\033[m\n')


if __name__ == '__main__':
    start()
