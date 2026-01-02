'''
OBJETIVO
CRIAR UM PROGRAMA QUE:
- USE ENTRADA
- DECISÃO
- REPETIÇÃO
- ACUMULADORES

DESCRIÇÃO DO DESAFIO
O PROGRAMA DEVE TER:
1- PEDIR NÚMEROS AO USUÁRIO REPETIDAMENTE
2- PARAR QUANDO O USUÁRIO DIGITAR 0
3 - AO FINAL MOSTRAR
    A QUANTIDADE DE NÚMEROS DIGITADOS(EXCETO O 0)
    A SOMA TOTAL
    A MÉDIA
    QUANTOS NÚMEROS FORAM PARES
    QUANTOS FORAM IMPARES
'''
num = 0
soma = 0
par = 0
impar = 0
qnt = 0

while True:
    num = int(input("Informe um número ou 0 para parar:"))
    if num == 0:
      break
    soma += num
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    qnt += 1
if qnt > 0:
    media = soma / qnt
else:
    media = 0

print("Você digitou",qnt,"números")
print("Você digitou ",par,"números pare(s)")
print("VocÊ digitou",impar,"números impar(res)")
print("A soma de todos os números é:",soma)
print(f"A média de todos os valores informados é:{media:.2f}")
