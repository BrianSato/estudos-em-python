"""
Arquivo: dia-06-while.py
Objetivo: Estrutura de repetição while em Phyton
"""

contador = 1

while contador <=5:
    print("Contador:", contador)
    contador += 1

print("Fim do loop")

"""
Exercício 1:
Crie um Programa que:
    Conte de 1 a 10
    Imprima cada número
"""
contador2 = 0

while contador2 <= 10:
    print("Número:",contador2)
    contador2 += 1
print("Fim do Loop")

"""
Exercício 2 (fixação)
Peça um número ao usuário e:
    Conte de 1 em 1 até este número usando WHILE
"""
contador3 = 1
limite = int(input("Informe um número inteiro:"))

while contador3 <= limite:
    print("Número:", contador3)
    contador3 += 1
