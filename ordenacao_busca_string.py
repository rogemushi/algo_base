def ordenar_e_verificar(prescricao, estoque):
    prescricao = sorted(prescricao)
    estoque = sorted(estoque)

    for medicamento in prescricao:
        # usando busca binária
        indice = bin_search(estoque, medicamento)
        # na ausencia do medicamento, é retornado já como falso        
        if indice == -1:
            return False
        else:
            # na presença é retirado da lista
            estoque.pop(indice)

    return True
    
def bin_search(lista, elemento):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


prescricao, estoque = map(list, input().split())
print(ordenar_e_verificar(prescricao, estoque))
