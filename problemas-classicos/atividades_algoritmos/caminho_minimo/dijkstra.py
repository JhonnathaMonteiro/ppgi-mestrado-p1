#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import inf


def _iss(G, s):
    """Inicializador de fonte unica

    :G: Grafo
    :s: Fonte
    :returns: distancias e parentes

    """
    
    # Similar ao PRIM
    d = [] # distancias
    p = [] # pai
    for u in G['V']:
        d.append(inf)
        p.append(None)

    d[s] = 0
    return d, p


def _adj(G, i):
    """Funcao para calcular vertices adjuntos

    :G: Grafo
    :i: Vertice
    :returns: lista com verices adjuntos

    """
    
    # Similar ao PRIM
    A = []
    for s, d, _ in G["E"]:
        if i == d:
            A.append(s)
        elif i == s:
            A.append(d)
    return A


def dijkstra(G, w, s):
    """Implementacao do algoritmo de dijkstra

    :G: Grafo
    :w: Matriz Adj
    :s: Origem
    :returns: d = Lista com as menores distancia entre
                  vetice s e os outros vetices do grafo.
              p = Parentes
              

    """
    
    # Incializacao de fonte unica
    d, p = _iss(G, s)  # d = distancia; p = parente
    
    S = []
    Q = G["V"][:] # lista com os vertices do grafo
    
    while Q: # enquanto existirem itens em Q, do:
        
        # u <- extract-min(Q)
        u = min(Q)
        Q.remove(u)
        
        S.append(u)
        for v in _adj(G, u):
            
            # ralaxacao(u,v,w)
            # atualizar d[v] e p[v] pelo exame do impacto da aresta
            if d[v] > (d[u] + w[u][v]):
                d[v] = d[u] + w[u][v]
                p[v] = u

    return d, p


# input graph E formato (origem, destino, peso)
graph = {
    'V': [0, 1, 2, 3],
    'E': (
        (0, 1, 10),
        (0, 2, 20),
        (1, 2, 5),
        (1, 3, 16),
        (2, 3, 20),
    )
}

# Teste
w = [[0, 10, 20, 0], [10, 0, 5, 16], [20, 5, 0, 20], [0, 16, 20, 0]]
s = 0  # Origem
print(dijkstra(graph, w, s))
