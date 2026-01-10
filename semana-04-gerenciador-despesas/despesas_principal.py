#IMPORTANDO FUNCOES
import despesas_funcoes_vs01 as df
import despesas_arquiva_vs01 as da

#CARREGANDO DO ARQUIVO
despesas = da.carregar_despesas()

# INICIO DO PROGRAMA
while True:
    df.menu()
    try:
        opcao = int(input(" DIGITE UMA DAS OPÇÕES ACIMA:"))
    except ValueError:
        print("Digite apenas números.")
        continue

    if opcao == 1:
        df.adiciona_despesa(despesas)
    elif opcao == 2:
        df.listar_despesas(despesas)
    elif opcao == 3:
        df.mostrar_total_e_media(despesas)
        df.maior_menor_valor(despesas)
    elif  opcao == 0:
        print("👋 Programa encerrado.")
        break
    else:
        print("❌ Opção inválida.")

da.salva_despesas(despesas)
print("💾 Despesas salvas com sucesso.")
