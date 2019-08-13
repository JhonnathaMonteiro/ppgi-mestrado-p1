from random import randint
from f_avaliacao import f_avaliacao


def reinsert(S, M, VS, gen_aleatorio=False):
    # S = Valor da Solucao
    # M = Matriz de custo
    # VS = Vetor Solucao
    n = len(VS)  # tamanho do vetor solucao
    BS = S  # Melhor solucao <--- S
    solucao = [BS, 0, 0]  # Formato [BS, i, j]
    if not gen_aleatorio:
        for i in range(1, n-1):
            for j in range(i+1, n):
                S_ = S  # Solucao a ser avaliada <--- S
                S_ = S_ - M[VS[i]][VS[i-1]]  # Primeira Quebra
                S_ = S_ - M[VS[i]][VS[i+1]]  # Segunda Quebra
                S_ = S_ + M[VS[i-1]][VS[i+1]]  # Primeira Add
                if j == n-1:  # n-1 = maior indice que pode ser acessado em VS
                    k = 0
                else:
                    k = j + 1
                S_ = S_ - M[VS[j]][VS[k]]  # Terceira quebra
                S_ = S_ + M[VS[j]][VS[i]]  # Segunda Add
                S_ = S_ + M[VS[i]][VS[k]]  # Terceira Add

                if S_ < BS:  # Testar vizinho
                    BS = S_
                    solucao = [BS, i, j]

        if solucao[1] == solucao[2]:
            return VS, S
        else:
            # Construir VS com solucao

            # Removendo i do vetor VS e o atribuido a variavel xi
            xi = VS.pop(solucao[1])

            # Inserindo xi na posicao j
            VS.insert(solucao[2], xi)  # +1 pois o vetor foi encurtado em .pop
            return VS, BS
    else:
        # Gerar vizinho aleatorio
        # RANDOM
        i = randint(1, n-2)
        j = randint(i+1, n-1)

        S_ = S  # Solucao a ser avaliada <--- S
        S_ = S_ - M[VS[i]][VS[i-1]]  # Primeira Quebra
        S_ = S_ - M[VS[i]][VS[i+1]]  # Segunda Quebra
        S_ = S_ + M[VS[i-1]][VS[i+1]]  # Primeira Add
        if j == n-1:  # n-1 = maior indice que pode ser acessado em VS
            k = 0
        else:
            k = j + 1
        S_ = S_ - M[VS[j]][VS[k]]  # Terceira quebra
        S_ = S_ + M[VS[j]][VS[i]]  # Segunda Add
        S_ = S_ + M[VS[i]][VS[k]]  # Terceira Add

        BS = S_
        solucao = [BS, i, j]

        # Removendo i do vetor VS e o atribuido a variavel xi
        xi = VS.pop(solucao[1])

        # Inserindo xi na posicao j
        VS.insert(solucao[2], xi)  # +1 pois o vetor foi encurtado em .pop

        return VS, BS


def swap(S, M, VS, gen_aleatorio=False):
    # S = Valor da Solucao
    # M = Matriz de custo
    # VS = Vetor Solucao
    n = len(VS)  # tamanho do vetor solucao
    BS = S  # Melhor solucao <--- S
    solucao = [BS, 0, 0]  # Formato [BS, i, j]

    if not gen_aleatorio:
        for i in range(1, n-1):
            for j in range(i+1, n):
                S_ = S  # Solucao a ser avaliada <--- S

                # Checando se j esta no limite
                if j == n-1:  # n-1 = maior indice que pode ser acessado em VS
                    k = 0
                else:
                    k = j + 1

                if j - i == 1:  # swap de nos proximos
                    S_ = S_ - M[VS[i-1]][VS[i]]  # Primeira Quebra
                    S_ = S_ - M[VS[j]][VS[k]]  # Segunda Quebra

                    S_ = S_ + M[VS[i-1]][VS[j]]
                    S_ = S_ + M[VS[i]][VS[k]]

                else:

                    S_ = S_ - M[VS[i-1]][VS[i]]  # Primeira Quebra
                    S_ = S_ - M[VS[i]][VS[i+1]]  # Segunda Quebra

                    # para j
                    S_ = S_ - M[VS[j-1]][VS[j]]  # Terceira quebra
                    S_ = S_ - M[VS[j]][VS[k]]    # Quarta quebra

                    # Inserindo i, j
                    # i
                    S_ = S_ + M[VS[j-1]][VS[i]]  # Segunda Add
                    S_ = S_ + M[VS[i]][VS[k]]  # Terceira Add

                    # j
                    S_ = S_ + M[VS[i-1]][VS[j]]  # Segunda Add
                    S_ = S_ + M[VS[j]][VS[i+1]]  # Terceira Add

                if S_ < BS:  # Testar vizinho
                    BS = S_
                    solucao = [BS, i, j]

        if solucao[1] == solucao[2]:
            return VS, S
        else:
            # Construir VS com solucao

            # Variavel axiliar para o swap entre i e j
            temp_var = VS[solucao[1]]

            # swap
            VS[solucao[1]] = VS[solucao[2]]
            VS[solucao[2]] = temp_var

            return VS, BS
    else:
        # Gerar vizinho aleatorio
        # RANDOM
        i = randint(1, n-2)
        j = randint(i+1, n-1)

        S_ = S  # Solucao a ser avaliada <--- S

        # Checando se j esta no limite
        if j == n-1:  # n-1 = maior indice que pode ser acessado em VS
            k = 0
        else:
            k = j + 1

        if j - i == 1:  # swap de nos proximos
            S_ = S_ - M[VS[i-1]][VS[i]]  # Primeira Quebra
            S_ = S_ - M[VS[j]][VS[k]]  # Segunda Quebra

            S_ = S_ + M[VS[i-1]][VS[j]]
            S_ = S_ + M[VS[i]][VS[k]]

        else:

            S_ = S_ - M[VS[i-1]][VS[i]]  # Primeira Quebra
            S_ = S_ - M[VS[i]][VS[i+1]]  # Segunda Quebra

            # para j
            S_ = S_ - M[VS[j-1]][VS[j]]  # Terceira quebra
            S_ = S_ - M[VS[j]][VS[k]]    # Quarta quebra

            # Inserindo i, j
            # i
            S_ = S_ + M[VS[j-1]][VS[i]]  # Segunda Add
            S_ = S_ + M[VS[i]][VS[k]]  # Terceira Add

            # j
            S_ = S_ + M[VS[i-1]][VS[j]]  # Segunda Add
            S_ = S_ + M[VS[j]][VS[i+1]]  # Terceira Add

            BS = S_
            solucao = [BS, i, j]

            # Variavel axiliar para o swap entre i e j
            temp_var = VS[solucao[1]]

            # swap
            VS[solucao[1]] = VS[solucao[2]]
            VS[solucao[2]] = temp_var

        return VS, BS
