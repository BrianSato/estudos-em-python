def filtrar_por_categoria(despesas, categoria):

     return[
        despesa for despesa in despesas
        if despesa.get("categoria") == categoria
    ]
