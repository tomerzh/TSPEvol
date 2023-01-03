import numpy as np

from eckity.genetic_operators.genetic_operator import GeneticOperator


class PermutationMutation(GeneticOperator):
    def __init__(self, swap_probability):
        super().__init__(arity=1, probability=swap_probability)
        self.applied_individuals = None

    def apply(self, individuals):
        for ind in individuals:
            size = ind.size()
            swapping_indices = np.random.choice(size, 2, replace=False)
            first_city = ind.cell_value(swapping_indices[0])
            second_city = ind.cell_value(swapping_indices[1])
            ind.set_cell_value(swapping_indices[0], second_city)
            ind.set_cell_value(swapping_indices[1], first_city)
        self.applied_individuals = individuals
        return individuals

