#!/usr/bin/env python3

import numpy as np
import os

# TODO: Mudar para relative import na producao
from construcao import construcaoGulosa, construcaoAleatoria
from movimentos import swap, reinsert
from f_avaliacao import f_avaliacao
from refinamento import vnd
from metaeuristica import vns
# from .construcao import construcaoGulosa, construcaoAleatoria
# from .movimentos import two_opt


# Para gerar Tabela Parcial:
# INSTANCES = [["bayg29", 1610],
#              ["bays29", 2020]]

# Para gerar Tabela Completa:
INSTANCES = [["bayg29", 1610],
             ["bays29", 2020],
             ["berlin52", 7542],
             ["bier127", 118282],
             ["brazil58", 25395],
             ["ch130", 6110],
             ["ch150", 6528],
             ["swiss42", 1273]]


def ler_instancia(nome_instancia):

    folder = os.path.join(os.path.dirname(__file__),
                          'instances', 'instancias_teste')

    file_path = os.path.join(folder, nome_instancia + '.txt')

    # Lendo a instancia
    with open(file_path, 'r') as f:
        NAME = f.readline().strip().split()[1]
        DIMENSION = int(f.readline().strip().split()[1])
        SECTION = f.readline().strip().split()[0]
        COST_MAT = np.loadtxt(f)

    return COST_MAT, NAME, DIMENSION, SECTION


def montar_tabela(INSTANCES=INSTANCES):

    print("---------------------------------------------------------------------------------------------------------------------------")
    print("                      |            Heuristica Construtiva               |               Heuristica Construtiva            |")
    print("                      |        Média           Melhor     Media     Gap |        Média           Melhor     Media     Gap |")
    print("Instancia       Ótimo |       solucão         solucão     tempo         |       solucão         solucão     tempo         |")
    print("---------------------------------------------------------------------------------------------------------------------------")

    for instance in INSTANCES:
        COST_MAT, NAME, _, _ = ler_instancia(instance[0])

        # Executar o vns 10x e calcular medias
        # Para Heuristica construtiva e meta-heuristica
        sum_solucoes_meta = 0
        sum_tempos_meta = 0

        sum_solucoes_construct = 0
        sum_tempos_construct = 0

        # Melhor solucao encontrada
        melhor_solucao_construct = np.inf
        melhor_solucao_meta = np.inf

        for _ in range(10):

            # HEURISTICA CONSTRUTIVA --------------------------------
            # Construcao Gulosa do vetor solucao inicial
            VS, tempo_construct = construcaoGulosa(COST_MAT)
            S = f_avaliacao(VS, COST_MAT)

            # Somando para a heuristica construtiva
            sum_solucoes_construct += S
            sum_tempos_construct += tempo_construct
            if S < melhor_solucao_construct:
                melhor_solucao_construct = S

            # META HEURISTICA --------------------------------------
            _, S__, tempo_meta = vns(S0=S,
                                     r=2,  # n de metodos de geracao de vizinhos
                                     busca_local=vnd,
                                     f_avaliacao=f_avaliacao,
                                     vizinhanca=[reinsert, swap],
                                     M=COST_MAT,
                                     VS=VS)

            # Atualizar o valor da melhor solucao
            if S__ < melhor_solucao_meta:
                melhor_solucao_meta = S__

            sum_solucoes_meta += S__
            sum_tempos_meta += tempo_meta

        # Calcular medias
        tempo_medio_construct = sum_tempos_construct/10
        tempo_medio_meta = sum_tempos_meta/10
        solucao_media_construct = sum_solucoes_construct/10
        solucao_media_meta = sum_solucoes_meta/10

        # Calculando o GAP
        gap_construct = (melhor_solucao_construct -
                         instance[1])/instance[1] * 100
        gap_meta = (melhor_solucao_meta -
                    instance[1])/instance[1] * 100
        print(
            f"{NAME} {instance[1]:8.0f} | {solucao_media_construct:15.0f} {melhor_solucao_construct:15.0f} {tempo_medio_construct:9.3f}{gap_construct:9.2f}| {solucao_media_meta:13.0f} {melhor_solucao_meta:15.0f} {tempo_medio_meta:9.3f}{gap_meta:9.2f}|")
    print("---------------------------------------------------------------------------------------------------------------------------")


montar_tabela()
