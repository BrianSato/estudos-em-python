# LISTA FUNCOES UTILIZADAS
def menu():
    print("\n-------GERENCIADOR DE DESPESAS-------")
    print(" 1 - Adicionar despesa:")
    print(" 2 - Listar despesas")
    print(" 3 - Ver estatisticas")
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

def mostrar_total_e_media(despesas):
    if not  despesas:
        print("Nenhuma despesas adicionada.")
        return

    total = 0
    for despesa in despesas:
        total += despesa["valor"]
    media = total/ len(despesas)
    print(f"💰 Total gasto: R$ {total:.2f}")
    print(f"📊A média de despesas: R$ {media:.2f}")

def maior_menor_valor(despesas):
    if not despesas:
        print("Nenhuma despesa adicionada")
        return
    maior = despesas[0]["valor"]
    menor = despesas[0]["valor"]
    for despesa in despesas:
        if despesa["valor"] > maior:
            maior = despesa["valor"]
        elif despesa["valor"] < menor:
            menor = despesa["valor"]
    print(f" A maior despesa foi: R${maior:.2f}")
    print(f" A menor despesa foi: R${menor:.2f}")
