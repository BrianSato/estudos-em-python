'''
EXERCICIO 1 - CONTAGEM CONTROLADA
1- PECA UM NÚMERO AO USUÁRIO
2- USE FOR PARA CONTAR DE 1 ATÉ ESTE NÚMERO
3- PARA CADA NÚMERO:
    SE FOR PAR - IMPRIMA "PAR"
    SE FOR IMPAR - IMPRIMA "IMPAR"
'''

num = int(input("Informe um número:"))

for i in range(1, num+1):
    if(i % 2 == 0):
        print("O número",i,"é par.")
    else:
        print("O número",i,"é impar.")

'''
EXERCÍCIO 2 - VALIDAÇÃO COM WHILE
CRIE UM PROGRAMA QUE:
1- PEÇA UMA NOTA ENTRE 0 E 10
2- ENQUANTO A NOTA FOR INVÁLIDA:
    PEÇA NOVAMENTE
3- QUANDO FOR VÁLIDA:
    IMPRIMA "NOTA REGISTRADA".
'''

nota = float(input("Informe a nota:"))

while nota < 0 or nota > 10:
    print("Valor Inválido, tente novamente!")
    float(input("Informe a nota:"))

print("Nota Registrada!")

'''
EXERCÍCIO 3 - SOMA ACUMULADA
CRIE UM PROGRAMA QUE:
1- USE WHILE
2- CONTINUE PEDINDO NÚMEROS
3- PARE QUANDO O USUÁRIO DIGITAR 0
4 - MOSTRE A SOMA TOTAL
'''

num = int(input("Informe um número e 0 para parar:"))
soma = 0

while num != 0:
    soma = num + soma
    num = int(input("Informe um número e 0 para parar:"))

print("A soma dos números informados é:",soma)
