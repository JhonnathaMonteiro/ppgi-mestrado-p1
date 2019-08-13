# Implementação do heapsort
  
# Função para heapficação da subarvore no indice i com heap de tamanho n. 
def heapify(arr, n, i): 
    largest = i  # Inicialização do maior como sendo a raiz 
    l = 2 * i + 1     # esquerda = 2*i + 1 
    r = 2 * i + 2     # direita = 2*i + 2 
  
    # Verifica se a criança da esquerda da raiz existe e se ela é maior que a raiz
    if l < n and arr[i] < arr[l]: # l < n = index out of bounds
        largest = l 
  
    # Verifica se a criança da direita da raiz existe e se ela é maior que a raiz 
    if r < n and arr[largest] < arr[r]: # r < n = index out of bounds
        largest = r 
  
    # Mudança de raiz se necessário (filho maior que o pai)
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify da raiz (chamada recursiva da sub-arvore). 
        heapify(arr, n, largest) 

# Função principao para ordenar uma lista de determinado tamanho 
def heapSort(arr): 
    n = len(arr) 
  
    # Construção do maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # Extração dos elementos de um em um
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0)

    return arr