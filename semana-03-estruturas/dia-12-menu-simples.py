"""
EXERCPICIO MENU SIMPLES
CRIE UM PROGRAMA QUE TENHA:
    1 - ADICIONAR NÚMERO
    2 - MOSTRAR LISTA
    3 - MOSTRAR ESTATÍSTICAS
    0 - SAIR

ESTATÍSTICAS DEVE MOSTRAR:
    - SOMA
    - MÉDIA
    - MAIOR
    - MENOR
    - QUANTIDADE DE PARES E IMPARES
"""
#VARIÁVEIS UTILIZADAS
menu = 0
lista = []
add_num = 0
soma = 0
media = 0
par = 0
impar = 0

#COMEÇO DO LOOP
while True:
    print("----------MENU-----------")
    print(" 1 - ADICIONAR NÚMERO")
    print(" 2 - MOSTRAR LISTA")
    print(" 3 - MOSTRAR ESTATÍSTICA")
    print(" 0 - SAIR.")
    menu = int(input("Digite uma das opções:"))

    if menu == 0:
        break
    elif menu == 1:
        add_num = int(input("Informe um número inteiro:"))
        lista.append(add_num)
    elif menu == 2:
        print("Lista dos números informados:",lista)
    elif menu == 3:
        soma = 0
        par = 0
        impar = 0
        qnt = len(lista)
        if qnt == 0:
            print("Não há valores dentro da lista.")
            continue
        else:
            maior = lista[0]
            menor = lista[0]

            for n in lista:
                #SOMA OS VALORES DA LISTA
                soma += n
                #VERIFICAN MAIOR E MENOR VALOR
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
        #CALCULA A MÉDIA
        media = soma/qnt
        #IMPRIME NO CONSOLE OS DADOS PRO USUARIO
        print("ESTATÍSTICAS DOS VALORES INFORMADOS:")
        print("A soma dos valores é:",soma)
        print("A quantidade de valores informados é:",qnt)
        print(f"A média dos valores é:{media:.2f}")
        print("O maior valor é:",maior,".e o menor valor é:",menor)
        print("Existem ",par,"par(es), e",impar,"impar(es)")

print("Fim do programa.")
