'''
1 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe 
contraram para desenvolver o programa que calculará os reajustes.
- Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:
-- salários até R$ 280,00 (incluindo) : aumento de 20%
-- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
-- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
-- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
-- o salário antes do reajuste;
-- o percentual de aumento aplicado;
-- o valor do aumento;
-- o novo salário, após o aumento.
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        value_salary = float(input("Insira o valor do seu salário: "))

        if value_salary <= 280:
            # Calcula o novo valor do salário
            cal = value_salary + (value_salary * 20/100)

            # Mostra na tela o resutado
            print(f"o salário antes do reajuste: R${value_salary}")
            print(f"o percentual de aumento aplicado: 20%")
            print(f"o valor do aumento: R${value_salary * 20/100}")
            print(f"Novo salário: R${cal}")

        elif value_salary >= 280 and value_salary <= 700:
            # Calcula o novo valor do salário
            cal = value_salary + (value_salary * 15/100)

            # Mostra na tela o resutado
            print(f"o salário antes do reajuste: R${value_salary}")
            print(f"o percentual de aumento aplicado: 15%")
            print(f"o valor do aumento: R${value_salary * 15/100}")
            print(f"Novo salário: R${cal}")

        elif value_salary >= 700 and value_salary <= 1500:
            # Calcula o novo valor do salário
            cal = value_salary + (value_salary * 10/100)

            # Mostra na tela o resutado
            print(f"o salário antes do reajuste: R${value_salary}")
            print(f"o percentual de aumento aplicado: 10%")
            print(f"o valor do aumento: R${value_salary * 10/100}")
            print(f"Novo salário: R${cal}")

        elif value_salary <= 1500:
            # Calcula o novo valor do salário
            cal = value_salary + (value_salary * 5/100)

            # Mostra na tela o resutado
            print(f"o salário antes do reajuste: R${value_salary}")
            print(f"o percentual de aumento aplicado: 5%")
            print(f"o valor do aumento: R${value_salary * 5/100}")
            print(f"Novo salário: R${cal}")

        # Canselar o loop
        break

    # Tratamento de erros com valor de argumento inadequado
    except (ValueError):
        # Limpar a tela
        os.system("clear")

        print("="*80)

        # Mostra mensagem de erro em cor vermelha e centralizado
        print("{}Erro: Erro: só é permitido números e pontos {}".format(
            '\033[31m', '\033[m').center(80))
        print("="*80)

    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):

        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break
