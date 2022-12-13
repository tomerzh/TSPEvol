import numpy as np

from eckity.genetic_operators.genetic_operator import GeneticOperator
import permutation_creator as perm_creator

class PermutationMutation(GeneticOperator):
    def __init__(self, swap_probability):
        super().__init__( arity=1, probability=swap_probability)
        self.applied_individuals = None

    def apply(self, individuals):
        range = individuals.size()
        print("before swaping " + individuals)
        swapping_indices = np.random.choice(range, 2, replace=False)
        first_city = individuals.cell_value(swapping_indices[0])
        second_city = individuals.cell_value(swapping_indices[1])
        individuals.set_cell_value(swapping_indices[0], second_city)
        individuals.set_cell_value(swapping_indices[1], first_city)
        # self.applied_individuals = individuals
        print("after swaping " + individuals)

        return individuals

# individual = perm_creator.PermutationCreator(5).create_individuals(1,True)
# PermutationMutation.apply(individual)





#
# class Test:
#     def __init__(self):
#         self.creator = perm_creator.PermutationCreator(5)
#         self.mutation = PermutationMutation(1)
#
#     def test(self):
#         individual = self.creator.create_individual()
#         print(individual)
#         self.mutation.apply(individual)