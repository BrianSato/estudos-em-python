"""
EXERCICIO 1 - MAIOR E MENOR NA UNHA
SEM USAR MAX() NEM MIN()
    USE A LISTA JÁ CRIADA
    DESCUBRA:
        - MAIOR VALOR
        - MENOR VALOR
DICA MENTAL:
    O PRIMEIRO NÚMERO DA LISTA VIRA O PADRÃO DE COMPARAÇÃO.
"""
#VARIÁVEIS UTILIZADAS
lista = [2,9,4,8,6,]
menor = lista[0]
maior = lista[0]

for n in lista:
    if maior < n:
        maior = n
    if menor > n:
        menor = n

print("O maior número da lista é:",maior)
print("O menor número da lista é:",menor)

"""
EXERCÍCIO 2
COM A MESMA LISTA:
- CALCULE A MÉDIA
- CONTE QUANTOS NÚMEROS SÃO:
    MAIORES QUE A MÉDIA
    MENORES QUE A MÉDIA
**SEM USAR FUNÇÕES PRONTAS ALÉM DE LEN()
"""
#VARIÁVEIS UTILIZADAS
soma =  0
qnt = len(lista)
qnt_maior = 0
qnt_menor = 0

for i in lista:
    soma += i

media = soma/qnt
for i in lista:
    if media < i:
        qnt_maior += 1
    else:
        qnt_menor += 1

print("A soma dos valores dentro da lista é:",soma)
print("A quantidade de valores dentro da lista é:",qnt)
print(f"A média dos valores dentro da lista é:{media:.2f}")
print("A quantidade de valores maiores que a média é:",qnt_maior)
print("A quantidade de valores menores que a média é:",qnt_menor)
