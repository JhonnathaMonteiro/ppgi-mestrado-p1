import numpy as np

# Problema da mochila (programacao dinamica - tabela)
def mochila_DP(p,v,capacidade):

    # Quantidade de elementos
    n = len(p)
    
    # Matriz valor
    # +1 pois a primeira linha e coluna eh relativa a mochila de capacidade 0 (vazia)
    G = np.zeros([n+1,capacidade+1])
    
    # Matriz de conteudo
    matrizConteudo = np.zeros([n+1,capacidade+1])
    
    # Item 0 considerado a mochila vazia
    # Comecando da linha 2
    for i in range(1, n + 1):  # Para cada linha (peso)

        for x in range(0, capacidade + 1): # Para cada coluna (capacidade)

            # Verifica se o item cabe na mochila
            if (x - p[i-1] >= 0):
                
                
                # G[i-1,x] = Estado atual sem o item
                # G[i-1, x-p[i-1]] + v[i-1] = Estado com o item colocado
                if (G[i-1,x] < G[i-1,x-p[i-1]] + v[i-1]):
                    G[i,x] = max(G[i-1,x], G[i-1, x-p[i-1]] + v[i-1])
                    matrizConteudo[i,x]=1
                
                else:
                    G[i,x] = G[i-1,x]
    
    return G,matrizConteudo          

def disclosure_content(matrizConteudo,p):
    [n,capacidade]=np.shape(matrizConteudo)
    n=n-1
    capacidade=capacidade-1
    content=[]
    k=capacidade
    for i in range(n,0,-1):
        if(matrizConteudo[i,k]==1):
            content.append(i-1)
            k=capacidade-p[i-1]                    
    return content



# TESTE

capacidade=10

p=[4, 7, 5, 3]

v=[40, 42, 25, 12]

[G,matrizConteudo] = mochila_DP(p,v,capacidade)  
print (G)
print (matrizConteudo)
print (disclosure_content(matrizConteudo,p))
