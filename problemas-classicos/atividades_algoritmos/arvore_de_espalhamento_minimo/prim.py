from math import inf

# funcao para retornar os vertices adjacentes de i
def adj(G, i):
    
    A = [] # inicializacao da lista de vertices adjacentes

    # Para cada aresta verificar se possui vertice adjacente a i
    for p, u, v in G['E']:
        # p = peso
        # u = origem
        # v = destino

        # se u == i o vertice v eh adjacente
        if u == i:
            A.append(v) # adicionar v a lista de adjacentes de i

        # se v == i o vertice u eh adjacente
        elif v == i:
            A.append(u) # adicionar u a lista de adjacentes de i
    
    return A

def prim(graph, w, r=0):
    # r = origem
    chave = [] # distancias
    
    pai = [] # pai do vertice
    
    # Chave inicializa com 0 para origem e inf para o restante
    # Pai inicializa com Null para todos os vertices
    for u in graph['V']:
        chave.append(inf)
        pai.append(None)
    chave[r] = 0
    
    # lista dos vertices do grafo
    Q = graph['V'][:]
    
    while Q: # Enquanto Q nao estiver vazia do:
        
        # Extrair u (minimo de Q)
        u = min(Q) 
        Q.remove(u)
        
        # Para cada vertice v adjacente a u, do:
        for v in adj(graph, u):
            
            # se (v pertence a Q) e (peso w(u,v) < que chave[v])
            # adicionar o caminho
            if (v in Q) and (w[u-1][v-1] < chave[v-1]):
                pai[v-1] = u
                chave[v-1] = w[u-1][v-1]

    print(sum(chave))
    print(pai)

# TESTES:
#graph = {
#        'V':[1, 2, 3, 4, 5],
#        'E':(
#            (2, 1, 2),
#            (2, 1, 3),
#            (4, 2, 3),
#            (5, 2, 4),
#            (5, 5, 2)
#            )
#        }
#
#w = [ [0,2,2,0,0],
#      [2,0,4,5,5],
#      [2,4,0,0,0],
#      [0,5,0,0,0],
#      [0,5,0,0,0] ]
#
#prim(graph,w)
