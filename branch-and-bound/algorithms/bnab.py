# -*- coding: utf-8 -*-
import numpy as np
from copy import deepcopy
import os
from simplex import Simplex
from simplex_tableau import Tableau


def branch_bound(tableau_entrada,
                 spl_type="BIG_M",
                 pli_type="PURE",
                 i_art=[],
                 MAX_NODES=100,
                 n_phases=1,
                 n_vart=0):
    """
    Branch-and-Bound
    Metodo de busca: Busca em largura


    Para um MAX(PLI)
    iniciar com:
                 MelhorValor = Infinito (incumbente)
                 S = {PLI} Conjunto solucao
                 NoAtual = None

        1. Resolva um subproblema pelo metodo Simplex
            1.1 Se o problema for infeasible, descarte-o
            1.2 Para uma solucao X* de inteiros (Metodo de busca)
            1.2.1 Se Z de X*<=Z*, descarte o subproblema
            1.2.2 Senao, faca Z*=Z, X* e a nova incumbente
            1.2.3 Os demais subproblemas com Z < Z* sao descartados
            1.3 Se a solucao nao for inteira
            1.3.1 Se Z de X* <= Z*, descarte o problema, nao ha contribuicao
            1.3.2 Senao,
                a. Escolha um xi com maior (xi % 1)
                b. Crie dois novos subproblemas adicionando uma restricao com
                xi <= floor(xi*) no primeiro e xi >= ceiling(xi*) no segundo
        retorne a incubente ao final das ramificacoes.


    OBS.: Para PLI binario
    #TODO
    a. Escolha um xi quaquer que tenha um valor nao binario na solucao.
    b. Crie dois novos subproblemas adicionando uma restricao com
    xi = 0 no primeiro e xi = 1 no segundo

    Para PLI misto -> apenas as variaveis que devem ser inteiras podem criar
    subproblemas

    """

    def is_integer(x):
        return np.equal(np.mod(x, 1), 0)

    def is_binary(x):
        return ((x == 0) | (x == 1))

    def print_result(node_number, LB, UB, node):

        # FIXME: ajeitar para imprimir Infeasible na tabela final
        # if node.solution == "Infeasible!":
        #     Z = "Infeasible"
        # else:
        #     pass
        Z = node.Z

        abs_gap = UB - Z  # Gap absoluto
        rel_gap = abs_gap / UB * 100

        print(f"{node_number:9d}{(len(activeSet) - 1):11d}  |{LB:15.3f} " +
              f"{UB:15.3f} {rel_gap:11.2f}%  {Z:15.3f} |")

    def set_subproblema(PL, branch_var, case, n_vart, spl_type, pli_type="PURE"):

        n_phases = 1

        if case == 1:  # restricao <=
            # Inserindo uma nova coluna para a nova variavel de folga
            new_tableau = np.insert(PL.tableau0, -(n_vart+1), 0, axis=1)
            # Criando a nova linha a ser inserida no tableau
            new_line = np.zeros(new_tableau.shape[1])
            new_line[branch_var] = 1
            new_line[-(n_vart + 2)] = 1

            # Valor de bi para nova linha
            if pli_type == "PURE":
                new_line[-1] = np.floor(PL.X[branch_var])
            elif pli_type == "BIN":
                new_line[-1] = 0

            # Appending the new restriction
            new_tableau = np.append(new_tableau, [new_line], axis=0)

            if n_vart == 0:
                spl_type = "TWO_PHASES"

            if spl_type == "TWO_PHASES" and n_vart >= 1:
                n_phases = 2

        elif case == 2:  # restricao >=

            # Inserindo uma nova coluna para a variavel artificial
            new_tableau = np.insert(PL.tableau0, -1, 0, axis=1)

            # Inserindo uma nova coluna para a nova variavel de folga
            new_tableau = np.insert(new_tableau, -(n_vart + 1), 0, axis=1)

            # Criando a nova linha a ser inserida no tableau
            new_line = np.zeros(new_tableau.shape[1])
            new_line[branch_var] = 1
            new_line[-2] = 1

            # Coeficiente para Variavel de foga da ineq ">=" (-1)
            new_line[-(n_vart + 2)] = -1

            # Valor de bi para nova linha
            if pli_type == "PURE":
                new_line[-1] = np.ceil(PL.X[branch_var])
            elif pli_type == "BIN":
                new_line[-1] = 0

            # Novo tableau de entrada
            new_tableau = np.append(new_tableau, [new_line], axis=0)

            # indices das linhas com variaveis artificias
            i_art.append(new_tableau.shape[0] - 1)

            if spl_type == "TWO_PHASES":
                # Nova funcao objetivo W
                # Ta somando so duas linhas em P5
                W = -sum(new_tableau[-(n_vart):])

                # Zerando os coeficientes das variaveis artificiais em W
                # Ta somando so duas linhas em P5
                W[-(n_vart + 1):-1] = 0

                # Adicionando nova FO
                new_tableau = np.append([W], new_tableau, axis=0)

                # Config do PL
                n_phases = 2

        PL = Simplex(new_tableau,
                     n_phases=n_phases,
                     n_vart=n_vart,
                     spl_type=spl_type,
                     i_art=i_art)

        PL.run()

        # Removing i_art index of infeasible solotio
        if not PL.feasible:
            del i_art[-1]

        return PL

    # ==========================================================================
    # Initial condition

    # pli_type = "BIN"
    activeSet = []
    bestVal = -np.inf
    currentBest = None

    tableau_entrada = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                   '..', 'instances', tableau_entrada))
    print("Input tableau: ", tableau_entrada)
    # Problema inicial
    P0 = Simplex(tableau_entrada,
                 n_phases=n_phases,
                 n_vart=n_vart,)

    nVAR = P0.tableau.shape[0] - 1  # or user input

    P0.run()
    activeSet.append(P0)
    node_counter = 0
    uper_bound = np.inf
    # ==========================================================================

    print("--------------------------------------------------------------------------------------")
    print("         Nodes        |                      Objective Bounds                        |")
    print("     Expl    ActvSet  |    LB(Incubent)             UB         Gap%                Z |")
    print("--------------------------------------------------------------------------------------")

    while activeSet:

        currentNode = activeSet[0]
        print_result(node_counter, bestVal, uper_bound, currentNode)
        node_counter += 1

        if node_counter >= MAX_NODES:
            print("Terminating: MAX_NODES reached")
            break

        # 1.1 Se o problema for infeasible, descarte-o
        if not currentNode.feasible:  # Problema Infeasible
            activeSet.pop(0)

        else:  # Problema feasible

            # 1.2 Para uma solution X* de inteiros
            if pli_type == "PURE":
                incubent_viable = all(is_integer(currentNode.X))
            elif pli_type == "BIN":
                incubent_viable = all(is_binary(currentNode.X))
            else:
                raise NotImplementedError("PLI method unknow")

            if incubent_viable:

                # 1.2.1 Se Z de X*<=Z*, descarte o subproblema
                if currentNode.Z <= bestVal:
                    # removendo o node
                    activeSet.pop(0)

                # 1.2.2 Senao, faca Z*=Z, X* e a nova incumbente
                else:
                    bestVal = currentNode.Z
                    currentBest = deepcopy(currentNode)
                    activeSet.pop(0)

                # 1.2.3 Os demais subproblemas com Z < Z* sao descartados
                for solution in activeSet:
                    if solution.Z < bestVal:
                        activeSet.remove(solution)

            # 1.3 Se a solution nao for inteira
            else:
                # 1.3.1 Se Z de X* <= Z*, descarte o problema, nao ha contribuicao
                if currentNode.Z <= bestVal:
                    # removendo o node
                    activeSet.pop(0)
                else:
                    uper_bound = np.floor(currentNode.Z)
                    # a. Escolha um xi quaquer que tenha um valor nao inteiro na solution.
                    # Escolhendo sempre o primeiro que tiver o maior x % 1
                    # indice de x na solution
                    branch_var = np.argmax(np.mod(currentNode.X[:2], 1))

                    # b. Crie dois novos subproblemas adicionando uma restricao com
                    # xi <= floor(xi*) no primeiro e xi >= ceiling(xi*) no segundo

                    # Subproblema 1
                    PL1 = set_subproblema(currentNode, branch_var,
                                          case=1,
                                          n_vart=currentNode.n_vart,
                                          spl_type=spl_type,
                                          pli_type=pli_type)
                    # Subproblema 2
                    PL2 = set_subproblema(currentNode,
                                          branch_var, case=2,
                                          n_vart=currentNode.n_vart + 1,
                                          spl_type=spl_type,
                                          pli_type=pli_type)

                    activeSet.pop(0)
                    activeSet.extend([PL1, PL2])

    print("--------------------------------------------------------------------------------------")
    print("Terminating...\n")
    print("Results:")
    print(f"Z: {currentBest.Z}")

    for i in range(nVAR):
        print(f"X{i + 1} = {currentBest.X[i]}")


# ++++++++++++++++++++++++++++++TEST++++++++++++++++
branch_bound("IN02",  # SLIDE example
             spl_type="BIG_M",
             pli_type="PURE",
             i_art=[],
             MAX_NODES=100,
             n_phases=1,
             n_vart=0)
