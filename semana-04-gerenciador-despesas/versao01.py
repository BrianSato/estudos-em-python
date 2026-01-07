"""
Funcionalidades da primeira versão
    - Menu interativo em console
    - Adicionar uma despesa:
        - valor (float)
        - descrição (string)
    - Listar todas as despesas
    - Mostrar total gasto
    - Validação de entrada (try/except)
    - Código limpo e organizado
"""

#FUNCOES UTILIZADAS
def menu():
    print("-------MENU-------")
    print(" 1 - ADICIONAR DESPESA:")
    print(" 2 - LISTAR TODAS AS DESPESAS")
    print(" 3 - MOSTRAR TOTAL GASTO:")
    print(" 0 - ENCERRA O PROGRAMA:")

def adiciona_despesa(despesas):
    try:
        valor = float(input("Informe o valor: R$ "))
        descricao = input("Informe a descrição: ")

        despesa = {
            "valor": valor,
            "descricao": descricao
        }

        despesas.append(despesa)
        print("Despesa adicionada com sucesso!")
    except ValueError:
        print("Valor inválido. Tente novamente.")


def listar_despesas(despesas):
     if not despesas:
         print("Nenhuma despesa adicionada")
         return
     print("------LISTA DE DESPESAS------")

     for i, despesa in enumerate(despesas, start=1):
         print(f"{i}. R$ {despesa['valor']:.2f} - {despesa['descricao']}")

def total_gasto(despesas):
    total = 0
    for despesa in despesas:
        total += despesa["valor"]
    print(f"O total das despesas é R$:{total:.2f}")


#VARIÁVEIS UTILIZADAS
despesas = []

# INICIO DO PROGRAMA
while True:

    menu()
    try:
        opcao = int(input(" DIGITE UMA DAS OPÇÕES ACIMA:"))
    except ValueError:
        print("Digite apenas números.")
        continue

    if opcao == 1:
        adiciona_despesa(despesas)
    elif opcao == 2:
        listar_despesas(despesas)
    elif opcao == 3:
        total_gasto(despesas)
    elif  opcao == 0:
        print("Programa Finalizado")
        break
    else:
        print("Opção Inválida")
