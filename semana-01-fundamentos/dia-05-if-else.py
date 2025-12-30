"""
Arquivo: dia-05-if-else-py
Objetivo: Estruturas de decisão com if e else
"""

idade= int(input("Digite sua idade:"))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

print("===============================")

"""
Exercício 1:
Crie um prorgrama que:
    Peça duas notas
    Calcule a média
    Se média for >= 6 : APROVADO
    Se não: REPROVADO
"""

nota1 = float(input("Informe a primeira nota:"))
nota2 = float(input("Informe a segunda nota:"))
media = (nota1 + nota2)/2

print("O Resultado do exercicio 1 é:")

if media >=6:
    print("APROVADO!")
else:
    print("REPROVADO")
print("============================")

"""
Exercício 2:
Peça um número e diga se ele é:
    POSITIVO
    NEGATIVO
    ZERO
"""
num = float(input("Informe um número:"))

if num == 0:
    print("O número informado é ZERO")
elif num < 0:
    print("O número informado é NEGATIVO")
else:
    print("O número informado é POSITIVO")
