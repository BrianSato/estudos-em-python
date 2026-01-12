from datetime import datetime

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
        data = obter_data()

        despesa = {
            "valor": valor,
            "descricao": descricao,
            "categoria" : categoria,
            "data": data
        }

        despesas.append(despesa)
        print("✅ Despesa adicionada com sucesso!")
    except ValueError:
        print("❌ Valor inválido. Tente novamente")

def obter_data():
    while True:
        data = input("Informe a data (YYYY=MM-DD) ou ENTER para hoje:").strip()

        if not data:
            return datetime.today().strftime("%Y-%m-%d")

        try:
            datetime.strptime(data, "%Y-%m-%d")
            return data
        except ValueError:
            print("🚨Data inválida, tente novamente.")
