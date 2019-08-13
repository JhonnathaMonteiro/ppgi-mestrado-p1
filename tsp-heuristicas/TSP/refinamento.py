def vnd(f_avaliacao, vizinhanca, r, S, M, VS):
    # M = matriz de custos, para ser utilizada na funcao
    # geradora de vizinhaca

    # vizinhanca: lista com as funcoes geradoras de vizinhaca
    # vizinhanca[0] = Reinsert
    # vizinhanca[1] = Swap

    # r = numero de estruturas diferentes de vizinhanca
    k = 1
    while k <= r:
        # Encontrar melhor vizinho de S
        VS_, S_ = vizinhanca[k-1](S, M, VS[:])
        if S_ < S:
            S = S_
            VS = VS_
            k = 1
        else:
            k += 1
    return VS, S
