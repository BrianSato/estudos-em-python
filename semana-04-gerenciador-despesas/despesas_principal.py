#IMPORTANDO FUNCOES
import gerenciador_funcoes_vs01 as gf

#VARIÁVEIS UTILIZADAS
despesas = []

# INICIO DO PROGRAMA
while True:
    gf.menu()
    try:
        opcao = int(input(" DIGITE UMA DAS OPÇÕES ACIMA:"))
    except ValueError:
        print("Digite apenas números.")
        continue

    if opcao == 1:
        gf.adiciona_despesa(despesas)
    elif opcao == 2:
        gf.listar_despesas(despesas)
    elif opcao == 3:
        gf.mostrar_total_e_media(despesas)
        gf.maior_menor_valor(despesas)
    elif  opcao == 0:
        print("👋 Programa encerrado.")
        break
    else:
        print("❌ Opção inválida.")
