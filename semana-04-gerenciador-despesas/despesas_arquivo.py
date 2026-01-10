#  FUNCOES PARA SALVAR  E CARREGAR OS DADOS EM ARQUIVO

def salva_despesas(despesas):
    with open("despesas.txt", "w", encoding="utf-8") as arquivo:
        for despesa in despesas:
            linha = f"{despesa['valor']} | {despesa['descricao']}\n"
            arquivo.write(linha)
            
def carregar_despesas():
    lista_despesas = []
    try:
        with open("despesas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                valor, descricao = linha.strip().split(" | ")
                lista_despesas.append({
                    "valor": float(valor),
                    "descricao": descricao
                })
    except FileNotFoundError:
        pass    #arquivo ainda não existe
    return lista_despesas
