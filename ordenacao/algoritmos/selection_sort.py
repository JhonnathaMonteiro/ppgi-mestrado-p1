def selectionSort(lista):
    
    for i in range(len(lista)):
        min_idx = i # assume que o elemento com indice i e o menor
        for j in range(i+1, len(lista)): # comparacao com os elementos nao arranjados
            if lista[min_idx] > lista[j]:
                min_idx = j # atualizacao do indice com o menor elemento
        lista[i], lista[min_idx] = lista[min_idx], lista[i] # troca de posicao dos elementos
    
    return(lista)