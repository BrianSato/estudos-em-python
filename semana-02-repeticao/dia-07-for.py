"""
Arquivo: dia-07-for.py
Objetivo: Estrutura de repetição for em Phyton

"""
#RANGE - LOOP DE REPETIÇÃO DE COMEÇA NO 1 E VAI ATÉ O 5
for i in range(1,6):
    print("Valor",i)

print("Fim do Loop")

"""
EXERCICIO 1
 - Imprima os números de 1 a 10 usando for
"""
for i in range(1,11):
    print("Número", i)
print("Fim do loop")

"""
EXERCÍCIO 2
- Peça um número ao usuário
- Imprima a tabulada deste número (1 a 10)
"""
num = int(input("Informe um número inteiro:"))

for i in range(1,11):
    print(num,"x",i,"=",num*i)
print("Fim do Loop")
