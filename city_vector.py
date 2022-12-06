from eckity.genetic_encodings.ga.vector_individual import Vector

from random import randint

from city import City

MIN_BOUND = 2 ** 31 - 1
MAX_BOUND = -2 ** 31

class CityVector(Vector):
    def __init__(self,
                 fitness,
                 length,
                 bounds=(MIN_BOUND, MAX_BOUND)):
        super().__init__(fitness, length=length, bounds=bounds)

    def get_random_city_in_bounds(self, index):
        if type(self.bounds) == tuple:
            x = randint(self.bounds[0], self.bounds[1])
            y = randint(self.bounds[0], self.bounds[1])
            return City(x, y)
        x = randint(self.bounds[index][0], self.bounds[index][1])
        y = randint(self.bounds[index][0], self.bounds[index][1])
        return City(x, y)