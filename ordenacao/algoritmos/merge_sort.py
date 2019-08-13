def merge(llista, rlista):
        """
        Merge duas lista em uma lista ordenada.
        """
        lista_final = []
        while llista or rlista: #Equanto existerem elementos na lista da direita ou esquerda
                if len(llista) and len(rlista):
                        if llista[0] < rlista[0]:
                                lista_final.append(llista.pop(0))
                        else:
                                lista_final.append(rlista.pop(0))

                # Para evitar o erro de com indice fora de range. Para lista com tamanhos diferentes
                if not len(llista):
                                if len(rlista): lista_final.append(rlista.pop(0))

                if not len(rlista):
                                if len(llista): lista_final.append(llista.pop(0))

        return lista_final

def mergeSort(lista):
        """
        Ordanação da lista pelo algoritmo mergesort
        """
        if len(lista) < 2: return list # Caso Base
        meio = len(lista) // 2 # Determinando o meio da lista
        return merge(mergeSort(lista[:meio]), mergeSort(lista[meio:])) # Chamada recursiva