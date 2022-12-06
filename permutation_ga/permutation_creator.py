import numpy as np

from eckity.creators.ga_creators.simple_vector_creator import GAVectorCreator
from city_vector import CityVector

class PermutationCreator(GAVectorCreator):
    def __init__(self, length = 1, events = None):
        super().__init__(length, None, (0, length), CityVector, events)

    def create_vector(self, individual):
        perm = list(np.random.permutation(individual))
        individual.set_vector(perm)