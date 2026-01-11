#IMPORTANDO FUNCOES
import despesas_menu as desp_menu
import despesas_arquivo as desp_arq
import despesas_listar as desp_list
import despesas_calculos as desp_calc
from despesas_filtrar import filtrar_por_categoria as catg_filt
from despesas_adicionar import escolher_categorias as catg_esc
from despesas_adicionar import adiciona_despesa as desp_add

#CARREGANDO DO ARQUIVO
despesas = desp_arq.carregar_despesas()

# INICIO DO PROGRAMA
while True:
    desp_menu.menu()
    try:
        opcao = int(input(" DIGITE UMA DAS OPÇÕES ACIMA:"))
    except ValueError:
        print("Digite apenas números.")
        continue

    if opcao == 1:
        desp_add(despesas)
    elif opcao == 2:
        desp_list.listar_despesas(despesas)
    elif opcao == 3:
        categoria = catg_esc()
        filtradas = catg_filt(despesas,categoria)
        if not filtradas:
            print("Nenhuma categoria encontrada para esta categoria")
        else:
            print(f"---- Categoria : {categoria} ----")
            for i, despesa in enumerate(filtradas, start=1):
                print(
                    f"{i}. R$ {despesa['valor']:.2f} - "
                    f"{despesa['descricao']}"
                )
    elif opcao == 4:
        desp_calc.mostrar_total_e_media(despesas)
        desp_calc.maior_menor_valor(despesas)
    elif  opcao == 0:
        print("👋 Programa encerrado.")
        break

    else:
        print("❌ Opção inválida.")

desp_arq.salva_despesas(despesas)
print("💾 Despesas salvas com sucesso.")
