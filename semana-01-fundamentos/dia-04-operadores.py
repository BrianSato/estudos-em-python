"""
Arquivo: dia-04-operadores.py
Objetivo: Trabalhar com operadores e expressões em Phyton
"""

#Operadores aritméticos
a=10
b=3
print("Soma:", a + b)
print("Subtração:",a - b)
print("Multiplicação:", a * b)
print("Divisção:", a / b)
print("Divisão inteira:", a // b)
print("Resto da divisão:",a % b)
print("Potência:", a ** b)

"""
Exercício:
- Peça dois números ao usuário
- Calcule:
    Soma;
    Subtração;
    Multiplicação;
    Divisão;
- Imprima todos os resultados.
"""
num1 = float(input("Informe o primeiro número:"))
num2 = float(input("Informe o segundo número"))
soma = num1 + num2
subt = num1 - num2
mult = num1 * num2
div = num1 / num2

print(f"A soma dos valores informados é:{soma:.2f}")
print(f"A subtração dos valores informados é:{subt:.2f}")
print(f"A multiplicação dos valores informados é:{mult:.2f}")
print(f"A divisão dos valores informados é:{div:.2f}")

