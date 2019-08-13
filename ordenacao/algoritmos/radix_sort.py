def countingSort(arr, exp1): 

    n = len(arr) 

    # Alocação para o array ordenado
    output = [0] * (n) 

    count = [0] * (10) # [0, 1, ... , 9]

    for i in range(0, n): 
        index = (arr[i]//exp1) % 10
        count[ index ] += 1

    for i in range(1,10): 
        count[i] += count[i-1] 

    # Construção do array de saída
    i = n-1
    while i>=0: 
        index = (arr[i]//exp1) % 10
        output[ count[ index ] - 1] = arr[i] 
        count[ (index)%10 ] -= 1
        i -= 1

    # Copiando para arr[]
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
    
    return arr

def radixSort(arr): 

    # Determinar o maior número para determinar a quantidade de digitos
    max1 = max(arr) 

    # Realiza-se countingSort para cada digito. O valor passado é exp
    # onde exp = 10^i onde i = digito atual.
    exp = 1
    while max1/exp > 1: # max1/exp percorre os digitos
        countingSort(arr,exp) 
        exp *= 10 # Avança o digito em uma casa.
    
    return arr


arr = [ 170, 45, 75, 90, 802, 24, 2, 66] 
print(radixSort(arr))