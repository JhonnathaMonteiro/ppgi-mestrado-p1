
parent = dict()


def make_set(vertice):
    # Criar um conjunto para arvore associado ao vertice
    parent[vertice] = vertice


# Funcao recursiva - retorna o vertice ancestral de v (vertice)
def find_set(vertice):
    if parent[vertice] != vertice: # Se parent[vertice] = vertice (caso base)
        parent[vertice] = find_set(parent[vertice]) # find_set(parent[vertice]) chamada recursiva
    return parent[vertice]


# Une os conjuntos das arvores que conte os vertices u e v
def union(u, v, edges):
    ancestor1 = find_set(u)
    ancestor2 = find_set(v)
    # Verifica se nao estao conectados
    if ancestor1 != ancestor2:
        parent[ancestor1] = ancestor2


def kruskal(graph):
    # A = vazio
    mst = set()
    
    # Criar uma floresta onde cada vertice eh uma arvore independente.
    for vertice in graph['V']:
        make_set(vertice)

    edges = list(graph['E']) # Arestas
    
    # Ordena as arestas em ordem ascendente para
    # garantindo que a arvore seja minima
    edges.sort()
    
    # Para cada aresta (aresta) no conjunto de aresta (edges)
    for edge in edges:
        weight, u, v = edge
        
        # Verifica se a aresta atual nao forma um ciclo
        # find_set(i) = ancestral de i
        if find_set(u) != find_set(v): # se o conjunto de u for diferente do de v
            mst.add(edge) # conjunto solucao
            union(u, v, edges) # fazer a uniao dos dois conjuntos

    return mst

# input graph E formato (peso, u, v)
#graph = {
#        'V':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        'E':(
#            (2, 1, 2),
#            (2, 1, 3),
#            (2, 2, 3),
#            (1, 2, 6),
#            (1, 3, 4),
#            (5, 4, 6),
#            (4, 6, 7),
#            (7, 4, 5),
#            (6, 7, 5),
#            (1, 4, 10),
#            (2, 5, 10),
#            (8, 5, 8),
#            (2, 5, 9),
#            (3, 8, 9),
#            )
#        }
#
#mst = kruskal(graph)
#print("Minimal Spanning Tree:")
#print(mst)
#mst_weight = 0
#for edge in mst:
#    weight, u, v = edge
#    mst_weight += weight
#
#print("Cost: ")
#print(mst_weight)
