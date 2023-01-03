import numpy as np

from eckity.creators.ga_creators.simple_vector_creator import GAVectorCreator
from eckity.fitness.simple_fitness import SimpleFitness
from city_vector import CityVector


# remember to pass on a non default gene_creator
class PermutationCreator(GAVectorCreator):
    def __init__(self, length=1, city_vector=None, gene_creator=None, bounds=(0, 100), events=None):
        super().__init__(length, gene_creator, bounds, CityVector, events)
        self.vector = city_vector

    def create_individuals(self, n_individuals, higher_is_better):
        individuals = [self.type(length=self.length,
                                 bounds=self.bounds,
                                 fitness=SimpleFitness(higher_is_better=higher_is_better))
                       for _ in range(n_individuals)]
        if self.vector is None:
            self.vector = [self.gene_creator(individuals[0], i) for i in range(self.length)]
        for ind in individuals:
            self.create_vector(ind)
        self.created_individuals = individuals
        return individuals

    def create_vector(self, individual):
        perm = list(np.random.permutation(self.vector))
        individual.set_vector(perm)




