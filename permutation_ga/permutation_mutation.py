import numpy as np

from eckity.genetic_operators.genetic_operator import GeneticOperator
import permutation_creator as perm_creator

class PermutationMutation(GeneticOperator):
    def __init__(self, swap_probability):
        super().__init__( arity=1, probability=swap_probability)
        self.applied_individuals = None

    def apply(self, individuals):
        for ind in individuals:
            range = ind.size()
            #print("before swapping " + ind.show())
            swapping_indices = np.random.choice(range, 2, replace=False)
            first_city = ind.cell_value(swapping_indices[0])
            second_city = ind.cell_value(swapping_indices[1])
            ind.set_cell_value(swapping_indices[0], second_city)
            ind.set_cell_value(swapping_indices[1], first_city)
            #print("after swapping " + individuals)

        return individuals


individuals = perm_creator.PermutationCreator(5).create_individuals(3, True)
for i in individuals:
     i.show()

perm = PermutationMutation(1)
print("AFTER MUTATION")
individuals = perm.apply(individuals)
for i in individuals:
     i.show()






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