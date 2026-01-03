"""
Arquivo: dia-09-listas.py
Objetivo: Introdução a listas em Python
"""

numeros = [10,20,30,40,50]

print(numeros)
print("Primeiro Elemento:",numeros[0])
print("Último Elemento:",numeros[-1])

#PERCORRENDO A LISTA
for n in numeros:
    print("Valor:",n)
#ADICIONA ELEMENTO A LISTA
numeros.append(60)
print(numeros)
#TAMANHO DA LISTA
print("Quantidade de elementos:",len(numeros))

"""
EXERCICIO 1
CRIE UMA LISTA COM 5 NÚMEROS E:
- IMPRIMA TODOS USANDO FOR
- MOSTRE O MAIOR E O MENOR NÚMERO
"""

lista = [1,5,7,9,50]
for n in lista:
    print(n)

print("O maior número é:",max(lista))
print("O menor número é:",min(lista))

"""
EXERCÍCIO 2(FIXAÇÃO)
- CRIE UMA LISTA VAZIA
- PEÇA 5 NÚMEROS AO USUÁRIO
- ADICIONE NA LISTA
- MOSTRE A LISTA FINAL
"""
lista2 = []
add_num = 0
for i in range(1,6):
    add_num = int(input("Informe um número inteiro:"))
    lista2.append(add_num)
print(lista2)
