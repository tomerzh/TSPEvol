import random

import numpy as np
from random import uniform
from eckity.genetic_operators.genetic_operator import GeneticOperator
from city_vector import CityVector


# fix when number of individuals is odd
class PermutationCrossover(GeneticOperator):
    # check if probability is needed
    def __init__(self, probability=0.8):
        self.applied_individuals = None
        self.probability = probability
        super().__init__(arity=2)

    def apply(self, individuals):
        for i in range(0, len(individuals) - 1, 2):
            if i + 1 < len(individuals) and uniform(0, 1) <= self.probability:
                temp_individual = individuals[i]
                individuals[i] = self.single_point_cross(individuals[i], individuals[i + 1])
                individuals[i + 1] = self.single_point_cross(individuals[i + 1], temp_individual)
        self.applied_individuals = individuals
        return individuals

    # this is ordered crossover with only one parent and different points
    # ordered crossover, randomly select a subset of the first parent and fill the rest with the second parent
    def cross(self, individual1: CityVector, individual2: CityVector):
        size = individual1.size()
        # randomly select a subset of the first parent
        start = np.random.randint(0, size)
        end = np.random.randint(0, size)
        if start > end:
            start, end = end, start
        subset = individual1.vector[start:end]
        # fill the rest with the second parent
        for i in range(size):
            if individual2.vector[i] not in subset:
                subset.append(individual2.vector[i])
        individual1.set_vector(subset)
        return individual1

    def single_point_cross(self, individual1: CityVector, individual2: CityVector):
        size = individual1.size()
        k = random.randint(0,size)
        print("crossover point: ", k)
        start = 0
        end = k
        subset = individual1.vector[start:end]
        for i in range(size):
            if individual2.vector[i] not in subset:
                subset.append(individual2.vector[i])
        individual1.set_vector(subset)
        return individual1

# if __name__ == "__main__":
#     individuals = perm_creator.PermutationCreator(5).create_individuals(4, True)
#     for i in individuals:
#         i.show()
#     perm = PermutationCrossover()
#     print("AFTER CROSSOVER")
#     individuals = perm.apply(individuals)
#     for i in individuals:
#         i.show()
