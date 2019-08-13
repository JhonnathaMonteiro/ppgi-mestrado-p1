def quickSort(lista):
        """
        Implementação do algoritmo quickSort
        """
        if len(lista) < 2: # caso base
            return lista
      
        else:
            pivot = lista[0] # O pivo é tomado como sendo o primeiro elemento da lista
            menores = [i for i in lista[1:] if i <= pivot] # Elementos menores que o pivot
            maiores = [i for i in lista[1:] if i > pivot] # Elementos maiores que o pivot
            return quickSort(menores) + [pivot] + quickSort(maiores) 