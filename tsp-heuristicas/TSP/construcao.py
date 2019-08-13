import random
import numpy as np
import time


# Heuristica do Vizinho Mais Proximo
def vizinho_mais_proximo(COST_MAT, S, C):

    # Cidade atual
    atual = S[-1]
    vizinhos = COST_MAT[atual]

    # Encontrar o vizinho menos distante da ultima cidade vizitada
    melhor_distancia = np.inf
    for vizinho, distancia in enumerate(vizinhos):
        if distancia != 0 and distancia < melhor_distancia:
            if vizinho not in S:
                melhor_distancia = distancia
                melhor_candidato = vizinho

    S.append(melhor_candidato)
    C.remove(melhor_candidato)


# CONSTRUCAO DA SOLUCAO
# construcao gulosa
def construcaoGulosa(COST_MAT, g_func=vizinho_mais_proximo):
    # tempo inicial
    start_time = time.time()

    # inicializando a solucao
    S = [0]

    # inicializando o conjunto C de elementos candidatos
    C = [i for i in range(1, len(COST_MAT))]

    # Enquanto C nao estiver vazio
    while C:
        g_func(COST_MAT, S, C)

    # tempo final
    exec_time = time.time() - start_time
    return S, exec_time


# construcao aleatoria
def construcaoAleatoria(COST_MAT, g_func=vizinho_mais_proximo):
    # tempo inicial
    start_time = time.time()

    # inicializando a solucao
    S = [0]

    # inicializando o conjunto C de elementos candidatos
    C = [i for i in range(1, len(COST_MAT))]

    # Enquanto C nao estiver vazio
    while C:
        # Esecolher aleatoriamente
        S.append(C.pop(random.randrange(len(C))))

    exec_time = time.time() - start_time
    return S, exec_time
