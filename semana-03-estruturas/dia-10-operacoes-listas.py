"""
EXERCICIO 1 (PRINCIPAL)
CRIE UMA LISTA VAZIA
PEÇA 5 NÚMEROS AO USUÁRIO
MOSTRE:
    SOMA
    MÉDIA
    MAIOR
    MENOR
    QUANTIDADE DE PARES E IMPARES
"""

#VARIÁVEIS UTILIZADAS
lista=[]
add_num = 0
soma = 0
media = 0
par = 0
impar = 0
#UTILIZANDO FOR PARA ADICIONAR OS NÚMEROS E VERIFICAR OS PARES E IMPARES
for i in range(5):
    add_num = int(input("Informe um número inteiro:"))
    lista.append(add_num)
    if(add_num % 2 == 0):
        par += 1
    else:
        impar +=1
#SOMANDO TODOS OS VALORES COM OUTRO LACO FOR
for i in lista:
    soma += i
#FAZENDO A MÉDIA DOS NÚMEROS UTILIZANDO O LEN
media = soma / len(lista)
#MOSTRANDO TODOS OS DADOS NO CONSOLE
print("A soma de todos os números é:",soma)
print("A média dos números informados é:",media)
print("O maior número é:",max(lista))
print("O menor número é:",min(lista))
print("Existem",par,"números pare(s)")
print("Existem",impar,"números impar(es)")

"""
EXERCÍCIO 2(DESAFIO LEVE)
PEÇA NÚMEROS AO USUÁRIO ATÉ ELE DIGITAR 0, ARMAZENE EM UMA LISTA E:
    MOSTRE A LISTA COMPLETA
    MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS
    MOSTRE A MÉDIA
"""
#VARIÁVEIS UTILIZADAS
lista2=[]
add_num2 = -1
soma2 = 0
media2 = 0
# PEDINDO OS VALORES AO USUÁRIOS UTILIZANDO LAÇO WHILE
while True:
    add_num2 = int(input("Digite um número para ser adicionado ou 0 para parar:"))
    if add_num2 == 0:
        break
    else:
        lista2.append(add_num2)
        soma2 += add_num2

#DEPOIS DE TERMINADO O LAÇO DIGITANDO 0, É FEITO A MÉDIA DOS VALORES.
media2 = soma2 / len(lista2)

#MOSTRANDOS OS VALORES NO CONSOLE
print("A lista Completa dos números informados é:",lista2)
print("Foram digitados",len(lista2),"números")
print(f"A média dos valores informados é:{media2:.2f}")
