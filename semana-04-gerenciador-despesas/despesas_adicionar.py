CATEGORIAS = {
        1: "Alimentos",
        2: "Pagamento de Boletos",
        3: "Gastos com o Carro",
        4: "Cartao de Credito"
    }

def escolher_categorias():
    print("---- Opcões de Categoria: ----")
    for codigo, nome in CATEGORIAS.items():
        print(f"{codigo} - {nome}")
    try:
        opcao = int(input("Informe o número da categoria:"))
        return CATEGORIAS.get(opcao, "Outras Despesas")
    except ValueError:
        return ("Outras Despesas")

def adiciona_despesa(despesas):
    try:
        valor = float(input("Informe o valor:"))
        descricao = input("Informe a descrição: ")
        categoria = escolher_categorias()

        despesa = {
            "valor": valor,
            "descricao": descricao,
            "categoria" : categoria
        }

        despesas.append(despesa)
        print("✅ Despesa adicionada com sucesso!")
    except ValueError:
        print("❌ Valor inválido. Tente novamente")
