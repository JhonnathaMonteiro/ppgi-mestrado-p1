# -*- coding: utf-8 -*-
import numpy as np
from copy import deepcopy

np.set_printoptions(formatter={'float': '{: 0.3f}'.format})


class Tableau(object):
    def __init__(self, tableau, n_phases, n_vart=0):
        self.tableau = None
        self.A = None                 # Matriz A
        self.b = None                 # Vetor b
        self.c = None                 # Vetor de coeficientes da funcao Obj.
        self.Z = None                 # Valor da Funcao Objetivo
        self.X = None                 # Vetor com os valores de x
        self.n_phases = n_phases      # Numero de fases
        self.n_VB = None              # Numero de variaveis basicas
        self.n_vart = n_vart          # Numero de variaveis artificiais
        self.i_art = None             #
        self.optimum = False          # Condicao otima atingida ?
        self.unbounded = False        # Problema irrestrito ?
        self.A0 = None                # Valor Inicial da Matriz A
        self.b0 = None                # Valor Inicial do vetor b
        self.tableau0 = None          # Tableau Inicial
        self.__load_tableau(tableau)

    def __load_tableau(self, tableau):
        if type(tableau) == str:
            self.tableau = np.loadtxt(tableau, delimiter=' ')

        elif type(tableau) == list:
            self.tableau = np.array(tableau)

        elif type(tableau) == np.ndarray:
            self.tableau = tableau

        self.set_var()

    def __trocar_base(self, pivot_line, pivot_column):
        self.VB[pivot_line - self.n_phases] = pivot_column

    def get_pivot(self):

        pivot_column = np.argmin(self.c)  # Bland

        ratio = [b/a if a > 0 and b >= 0 else np.inf for b,
                 a in zip(self.b, self.tableau[self.n_phases:, pivot_column])]

        ratio = np.array(ratio)

        # least ocorrence
        pivot_line = np.where(ratio == ratio.min())[0][-1] + 1

        ocorrences = np.where(ratio == ratio.min())[0] + 1
        mask = np.isin(ocorrences, self.i_art)

        if any(mask):
            # Desempate escolhendo a primeira artificial
            pivot_line = ocorrences[mask][0]
        else:
            pivot_line = ocorrences[0]

        return pivot_line, pivot_column

    def get_X(self):

        # Funciona pro bigM
        X = np.zeros(self.tableau.shape[1])
        for bi, VBi in zip(self.b, self.VB):  # TODO
            X[int(VBi)] = bi

        self.X = X

    def set_tableau(self, novo_tableau):
        self.tableau = novo_tableau
        self.set_var()

    def set_var(self, NEW_VB=True):
        self.A = self.tableau[1:, :-1]
        self.b = self.tableau[self.n_phases:,  -1]  # TODO
        self.c = self.tableau[0, :-1]

        self.Z = self.tableau[0,  -1]
        self.n_VB = self.tableau.shape[1] - self.tableau.shape[0]

        # Salvando condicao inicial
        self.A0 = deepcopy(self.A)
        self.b0 = deepcopy(self.b)

        if NEW_VB:

            self.b = self.tableau[self.n_phases:,  -1]  # TODO TESTE
            self.tableau0 = deepcopy(self.tableau)
            # TODO: Review This can be optmized
            n_VB = self.tableau.shape[0] - self.n_phases

            self.VB = np.arange(
                self.tableau.shape[1] - n_VB, self.tableau.shape[1]) - 1

    def pivot(self, pivot_line, pivot_column):

        pivot = self.tableau[pivot_line, pivot_column]

        # Dividindo a linha pivot pelo elemento pivot (normalizar)
        self.tableau[pivot_line] /= pivot

        for i in range(len(self.tableau)):
            if i == pivot_line:
                continue
            # linha = linha - a[i][pivot_column] * linha pivo
            aij = self.tableau[i][pivot_column]
            self.tableau[i] = self.tableau[i] - aij * self.tableau[pivot_line]

        self.__trocar_base(pivot_line, pivot_column)
        self.Z = self.tableau[0, -1]
