"""
EXERCICIO DE APLICAÇÃO DE TRY/EXCEPT
REFATORAR O CÓDIGO ANTERIOR PARA INSERIR EXCEÇÕES
EVITANDO ASSIM QUE O USUÁRIO DIGITE DADOS INVÁLIDOS
OCASIONANDO EM ERROS NO PROGRAMA
"""
#LISTA FUNCOES UTILIZADAS NO PROGRAMA
def menu_principal():
    print("----------MENU-----------")
    print(" 1 - ADICIONAR NÚMERO")
    print(" 2 - MOSTRAR LISTA")
    print(" 3 - MOSTRAR ESTATÍSTICA")
    print(" 4 - SALVAR OS DADOS EM ARQUIVO.TXT")
    print(" 5 - CARREGAR OS DADOS DE ARQUIVO.TXT")
    print(" 0 - SAIR.")
def adiciona_numero(lista):
    # USO DE TRY PARA EVITAR MENSAGENS DE ERRO E PARALIZAÇÃO DO PROGRAMA POR PARTE DO USUÁRIO
    try:
        add_num = int(input("Informe um número inteiro:"))
        lista.append(add_num)
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")
def mostraLista(lista):
    print("Lista dos números informados:", lista)
def mostra_estatistica(lista):
    soma = 0
    par = 0
    impar = 0
    qnt = len(lista)
    maior = lista[0]
    menor = lista[0]

    for n in lista:
        # SOMA OS VALORES DA LISTA
        soma += n
        # VERIFICAN MAIOR E MENOR VALOR
        if n > maior:
            maior = n
        if n < menor:
             menor = n

    for i in lista:
        # VERIFICA PAR E IMPAR
        if i % 2 == 0:
            par += 1
        else:
            impar += 1
    # CALCULA A MÉDIA
    media = soma / qnt
    # IMPRIME NO CONSOLE OS DADOS PRO USUARIO
    print("ESTATÍSTICAS DOS VALORES INFORMADOS:")
    print("A soma dos valores é:", soma)
    print("A quantidade de valores informados é:", qnt)
    print(f"A média dos valores é:{media:.2f}")
    print("O maior valor é:", maior, ".e o menor valor é:", menor)
    print("Existem ", par, "par(es), e", impar, "impar(es)")

def salvar_em_arquivo(lista):
    with open("arquivo.txt", "w") as arquivo:
        for n in lista:
            arquivo.write(str(n) + "\n")

def carregar_do_arquivo(lista):
    lista.clear()
    # USO DE TRY PARA EVITAR MENSAGENS DE ERRO E PARALIZAÇÃO DO PROGRAMA POR PARTE DO USUÁRIO
    try:
        with open("arquivo.txt","r") as arquivo:
            for linha in arquivo:
                numero = int(linha.strip())
                lista.append(numero)
    except FileNotFoundError:
        print("Arquivo não encontrado, nenhum dado carregado")

##FIM DA LISTA DE FUNÇÕES

##COMEÇO DO PROGRAMA
#VARIAVEIS UTILIZADAS
lista = []
while True:
    menu_principal()

    try:
        opcao = int(input("Digite uma das opções: "))
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        continue

    if opcao == 0:
        break
    elif opcao == 1:
        adiciona_numero(lista)
    elif opcao == 2:
        mostraLista(lista)
    elif opcao == 3:
        qnt = len(lista)
        if qnt == 0:
            print("Não há valores dentro da lista.")
            continue
        else:
            mostra_estatistica(lista)
    elif opcao == 4:
        salvar_em_arquivo(lista)
        print("Dados Salvos com Sucesso!")
    elif opcao == 5:
        carregar_do_arquivo(lista)
        print("Dados Carregados com Sucesso!")
    else:
        print("Opção inválida, tente novamente")
print("Fim do programa.")
