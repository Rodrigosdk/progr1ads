'''
Atividade 6

Escreva um programa que leia um valor inteiro e calcule o seu quadrado
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        value = int(input("insira um valor: "))

        # Mostra na tela o resutado
        print(f"Você dígito {value} e seu quadrado é {value*value}")

        # Canselar o loop
        break

    # Tratamento de erros com valor de argumento inadequado
    except (ValueError):
        # Limpar a tela
        os.system("clear")

        print("="*80)

        # Mostra mensagem de erro em cor vermelha e centralizado
        print("{}Erro: só é permitido números inteiros {}".format(
            '\033[31m', '\033[m').center(80))
        print("="*80)


    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):

        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break
