import time


def vns(S0,  # solucao inicial
        r,   # numero de estruturas diferentes de vizinhaça
        busca_local,  # fubncao de busca_local (VND)
        f_avaliacao,  # funcao de avaliacao
        vizinhanca,  # Lista com os func. de movimentos de vizinhaca
        M,  # Matriz de custo
        VS,  # Vetor solucao
        MAX_CONSEC_FAIL=10,  # Número máximo de falhas consecultivas
        MAX_TIME=20,  # Tempo máximo de execução
        ):

    S = S0  # Solucao corrente

    # Tempo inicial (utilizado no criterio de parada)
    start_time = time.time()

    # Contador de falhas consecutivas (criterio de parada 1)
    fail_counter = 0

    # Tempo de execução (criterio de parada 2)
    exec_time = 0

    while (fail_counter < MAX_CONSEC_FAIL) and (exec_time < MAX_TIME):

        k = 1  # Tipo de estrutura de vizinhança corrente
        while k <= r:
            # Gere um vizinho qualquer (aleatorio)
            VS_, S_ = vizinhanca[k-1](S, M, VS[:], gen_aleatorio=True)
            
            # Aumentar o nivel de pertubacao
            for _ in range(10):
                VS_, S_ = vizinhanca[k-1](S_, M, VS_[:], gen_aleatorio=True)

            # Busca Local (VND)
            VS__, S__ = busca_local(f_avaliacao, vizinhanca, r, S_, M, VS_[:])

            if S__ < S:
                S = S__
                VS = VS__
                k = 1

                # Zerar contador de falhas consecutivas
                fail_counter = 0
            else:
                k += 1
        fail_counter += 1
        exec_time = time.time() - start_time
    return VS, S, exec_time
