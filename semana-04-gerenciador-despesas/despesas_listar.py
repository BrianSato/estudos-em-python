def listar_despesas(despesas):
    if not despesas:
        print("Nenhuma despesa adicionada")
        return
    print("------LISTA DE DESPESAS------")

    for i, despesa in enumerate(despesas, start=1):
        print(
            f"{i}.{despesa.get('data', 'sem data')} - " 
            f" R$ {despesa['valor']:.2f} - "
            f"{despesa['descricao']} - "
            f"{despesa.get('categoria', 'Sem categoria')}"
        )
