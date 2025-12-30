"""
Arquivo: dia-03-input.py
Objetivo: Entrada de dados com input() e conversão de tipos de dados
"""

#Lendo texto
nome = input("Digite seu nome:")
print("Nome digitado:",nome)

#Lendo número inteiro
idade = int(input("Digite sua idade:"))
print("Idade:",idade)

#Lendo número decimal
altura = float(input("Digite sua altura:"))
print("Altura:", altura)

"""
Exercício:
1-Pedir o nome do usuário
2-Pedir dois números inteiros
3-Imprimir o nome e a  sonha dos dois números informados.
"""

nome = input("Informe seu nome:")
num1 = int(input("Informe o primeiro número inteiro:"))
num2 = int(input("Informe o segundo número inteiro:"))
soma = num1+num2
print("Seu nome é:", nome)
print("A soma dos números informados é:", soma)
