def countingSort(lista, maxval):
    """CountingSort"""
    m = maxval + 1
    count = [0] * m               # inicializa com zeros
    for a in lista:
        count[a] += 1             # contagem de ocorrencias
    i = 0
    for a in range(m):            # emit
        for _ in range(count[a]): # - emit 'count[a]' copias de 'a'
            lista[i] = a
            i += 1
    return lista


# print(countingSort([1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1], 7 ))