def insertionSort(lista):

    # o loop e iniciado no segundo elemento pois se assume que o primeiro esta arranjado
    for i in range(1, len(lista)):
        chave = lista[i] # proximo elemento a ser inserido na parte arranjada
        j = i - 1
        while j>= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return(lista) 