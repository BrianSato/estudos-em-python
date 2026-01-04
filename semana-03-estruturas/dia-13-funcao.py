"""
EXERCICIO DE FUNCAO
REFATORAR O CÓDIGO ANTERIOR SEPARANDO CADA FUNCIONALIDADE
EM FUNCOES DEIXANDO O CÓDIGO LIMPO.
FUNCOES SUGERIDAS:
 - MOSTRAR_MENU()
 - ADICIONAR_NUMERO(LISTA)
 - MOSTRAR_LISTA(LISTA)
 - MOSTRAR_ESTATISTICAS(LISTA)
"""
#LISTA FUNCOES UTILIZADAS NO PROGRAMA
def menuPrincipal():
    print("----------MENU-----------")
    print(" 1 - ADICIONAR NÚMERO")
    print(" 2 - MOSTRAR LISTA")
    print(" 3 - MOSTRAR ESTATÍSTICA")
    print(" 0 - SAIR.")
def adicionaNumero(lista):
    add_num = int(input("Informe um número inteiro:"))
    lista.append(add_num)
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
##FIM DA LISTA DE FUNÇÕES

##COMEÇO DO PROGRAMA
#VARIAVEIS UTILIZADAS
lista = []
while True:
    menuPrincipal()
    opcao = int(input("Digite uma das opções:"))
    if opcao == 0:
        break
    elif opcao == 1:
        adicionaNumero(lista)
    elif opcao == 2:
        mostraLista(lista)
    elif opcao == 3:
        qnt = len(lista)
        if qnt == 0:
            print("Não há valores dentro da lista.")
            continue
        else:
            mostra_estatistica(qnt,lista)
print("Fim do programa.")
