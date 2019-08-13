import numpy as np

# Problema da mochila (programacao dinamica - tabela)
def mochila_DP(p, v, m, L):
    # v = valores
    # p = pesos
    # m = quantidade de objetos
    # L = capacidade da mochila

    # Inicializando G com zeros
    # +1 pois a primeira linha e coluna eh relativa a mochila de capacidade 0
    G = np.zeros([m+1, L+1])

    # dec = array para guardar os itens que foram colocados na mochila
    dec = np.zeros([m+1, L+1])

    # conteudo da mochila
    conteudo = []
    
    # Item 0 considerado a mochila vazia
    # Comecando da linha 2
    for i in range(1, m+1):  # Para cada linha (peso)
        for j in range(L+1): # Para cada coluna (capacidade) de 0 ate L (inclusivo)
            
           # G[i-1, j] = Estado atual sem o item
           # G[i-1, j-p[i-1]] + v[i-1] = Estado com o item colocado
            
            # Verifica se o item cabe e vai ser inserido na mochila
            if (p[i-1] <= j) and ((G[i-1, j - p[i-1]] + v[i-1]) > G[i-1, j]): # item cabe
                G[i, j] = v[i-1] + G[i - 1, j - p[i-1]]
                dec[i, j] = 1
            
            else: # item nao sera inserido
                G[i, j] = G[i-1, j]
                # dec[i,j] = 0
    

    # Determinando o conteudo damochila
    
    # Percorrer dec de forma reversa
    for i in range(m - 1, 0, -1):

        if dec[i, j] == 1: # Se o item estiver na mochila

            # Adicionar ao conjunto conteudo
            conteudo.append(i-1)
            j = j - p[i-1] 

    print(G)
    print(conteudo)
    # print(conteudo)
    return G, conteudo
      

# TESTE ---------------------------------------------------------------

# pesos
p=[8, 3, 6, 4, 2]

# valores
v=[100, 60, 70, 15, 15]

#n de itens
m=5

#Capacidade
L=10

mochila_DP(p,v,m,L)
#  SAIDA ---------------------------------------------------------------
# [[  0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.]
#  [  0.   0.   0.   0.   0.   0.   0.   0. 100. 100. 100.]
#  [  0.   0.   0.  60.  60.  60.  60.  60. 100. 100. 100.]
#  [  0.   0.   0.  60.  60.  60.  70.  70. 100. 130. 130.]
#  [  0.   0.   0.  60.  60.  60.  70.  75. 100. 130. 130.]
#  [  0.   0.  15.  60.  60.  75.  75.  75. 100. 130. 130.]]
#  [2, 1]
