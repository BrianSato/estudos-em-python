# LISTA FUNCOES UTILIZADAS
def menu():
    print("\n-------GERENCIADOR DE DESPESAS-------")
    print(" 1 - Adicionar despesa:")
    print(" 2 - Listar despesas")
    print(" 3 - Mostrar total gasto")
    print(" 0 - Sair")

def adiciona_despesa(despesas):
    try:
        valor = float(input("Informe o valor: R$ "))
        descricao = input("Informe a descrição: ")

        despesa = {
            "valor": valor,
            "descricao": descricao
        }

        despesas.append(despesa)
        print("✅ Despesa adicionada com sucesso!")
    except ValueError:
        print("❌ Valor inválido. Tente novamente")


def listar_despesas(despesas):
     if not despesas:
         print("Nenhuma despesa adicionada")
         return
     print("------LISTA DE DESPESAS------")

     for i, despesa in enumerate(despesas, start=1):
         print(f"{i}. R$ {despesa['valor']:.2f} - {despesa['descricao']}")

def total_gasto(despesas):

    if not  despesas:
        print("Nenhuma despesas adicionada.")
        return

    total = 0
    for despesa in despesas:
        total += despesa["valor"]
    print(f"\n💰 Total gasto: R$ {total:.2f}")


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
        print("👋 Programa encerrado.")
        break
    else:
        print("❌ Opção inválida.")
