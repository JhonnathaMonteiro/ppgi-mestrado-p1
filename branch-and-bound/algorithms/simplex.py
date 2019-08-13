# -*- coding: utf-8 -*-
from simplex_tableau import Tableau
import numpy as np


class Simplex(Tableau):

    '''The Simplex algorithm implementation.

    Methods
    -------
    solver()
        Simplex solver.
    run()
        Run the simplex algorithm with the spl_type spl_type
        to solve the current tableau.
    remove_artficial()
        Remove artificial variables from the current tableau.
    test_optimum()
        Check if the the solution is optimum.
    test_feasible()
        Check if the problem is feasible.
    test_min_ratio(pivot_column)
        Test the min ratio with the pivot_column.
    _big_m()
        BigM simplex method spl_type.
    _phase1()
        Phase 1 of TWO_PHASES simplex.
    _phase2()
        Phase 2 of TWO_PHASES simplex.
    '''

    def __init__(self,
                 tableau,
                 n_phases=1,
                 n_vart=0,
                 i_art=[],
                 opt_type="MAX",
                 spl_type="TWO_PHASES"):
        super().__init__(tableau, n_phases, n_vart)

        self.n_phases = n_phases
        self.n_vart = n_vart
        self.i_art = i_art
        self.spl_type = spl_type
        self.feasible = True
        self.solution = None

        '''
        Parameters
        ----------
        tableau : numpy.ndarray
            A numpy.ndarray containing the tableau for the simplex method

                                  _____________________________________
            Objective Function -> |  c1  |  c2  | ... |  cn     |   Z |
                                  |  x11 |  x12 | ... |  x1n    |  b1 |
                                  |  x21 |  x22 | ... |  x2n    |  b2 |
                                  |               ...           | ... |
                                  |  xm1 |  xm2 | ... |  xmn    |  bn |
                                  -------------------------------------
        n_phases: int
            The variable n_phases is used to determine the number of phases
            required to solve the LP problem, (TWO_PHASES: n_phases = 2
                                               BIG_M:      n_phases = 1).

        n_vart: int
            The variable n_vart is used to determine the number of
            artificial Variables in the current tableau.

        i_art: list
            The variable i_art is used to determine the number of
            artificial Variables in the current tableau.

        opt_type: str
            The variable opt_type is used to determine the type of optimization
            maximization(MAX), minimization(MIN).

        spl_type: str
            The variable method is used to determine the simplex spl_type
            used to solve the current tableau.

        '''

    def solver(self):
        while not self.optimum:
            pivot_line, pivot_column = self.get_pivot()
            self.test_min_ratio(pivot_column)
            self.test_unbounded()
            if self.unbounded:
                self.solution = "Unbounded!"
                return
            self.pivot(pivot_line, pivot_column)
            self.test_optimum()

    def run(self):

        if self.spl_type == "BIG_M":
            self._big_m()
        elif self.spl_type == "TWO_PHASES":
            # Phase 1
            if self.n_phases == 2:
                self._phase1()
                self.test_feasible()
                self.remove_artficial()
                self.optimum = False
                self.n_phases = 1
                if self.feasible:
                    self._phase2()  # <---Call phase 2
                else:
                    self.solution = "Infeasible!"
            # Phase 2
            elif self.n_phases == 1:
                self._phase2()
                self.get_X()
                self.solution = self.X

    def remove_artficial(self):
        self.tableau = np.delete(
            self.tableau, np.s_[-(self.n_vart + 1):-1], 1)

        self.tableau = np.delete(self.tableau, 0, 0)
        self.optimum = False

    def test_optimum(self):

        # To max LP
        if np.min(self.c) >= 0:
            self.optimum = True

        # TODO to min LP

    def test_feasible(self):
        if self.spl_type == "TWO_PHASES":
            # This run at the end of the first Phase
            # So Z means W here!
            if self.Z != 0:
                self.feasible = False

        elif self.spl_type == "BIG_M":
            if any(self.c[-self.n_vart:] == 0):
                self.feasible = False

        else:
            raise NotImplementedError(
                "Simplex Method spl_type not Implemented")

    def test_min_ratio(self, pivot_column):

        self.test_ratio = [b/a if a > 0 and b >= 0 else np.inf for b,
                           a in zip(self.b, self.tableau[self.n_phases:, pivot_column])]

    def test_unbounded(self):
        # If min ratio test fail > unbounded
        if all((test < 0 or test == np.inf) for test in self.test_ratio):
            self.unbounded = True

    def _big_m(self):
        # Here im setting M as 100 times the largest coeficient in A matrix
        M = 100 * self.A.max()

        # New FO, coef 0 to Artificials variable
        self.tableau[0] = self.tableau[0] - M*sum(self.tableau[self.i_art])

        # Zerando valor do coef artificial
        self.tableau[0][-(self.n_vart + 1):-1] = 0  # CORRETO -(art +1)

        self._phase2()
        self.test_feasible()
        if self.feasible:
            self.get_X()
            self.solution = self.X

    def _phase1(self):
        self.solver()

        # NEW_VB = False, block changes in self.VB
        self.set_var(NEW_VB=False)

    def _phase2(self):
        self.solver()


#TODO: Remover
if __name__ == "__main__":
    S = Simplex("entrada.txt",
                spl_type="BIG_M",
                i_art=[2, 3],
                n_vart=2
                )
    S.run()
    print(S.X)
