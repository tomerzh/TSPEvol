from eckity.genetic_encodings.ga.vector_individual import Vector

from random import randint

from city import City

MIN_BOUND = 0
MAX_BOUND = 2 ** 31


class CityVector(Vector):
    def __init__(self,
                 fitness,
                 length,
                 bounds=(MIN_BOUND, MAX_BOUND)):
        super().__init__(fitness, length=length, bounds=bounds)
        self.city_temp = None

    def get_random_number_in_bounds(self, index):
        if type(self.bounds) == tuple:
            x = randint(self.bounds[0], self.bounds[1])
            y = randint(self.bounds[0], self.bounds[1])
            self.city_temp = City(x, y)
            return self.city_temp
        x = randint(self.bounds[index][0], self.bounds[index][1])
        y = randint(self.bounds[index][0], self.bounds[index][1])
        self.city_temp = City(x, y)
        return self.city_temp

    def get_city_vector(self):
        return self.city_temp

    def get_x(self):
        return self.city_temp.get_x()

    def get_y(self):
        return self.city_temp.get_y()


if __name__ == "__main__":
    vector1 = CityVector(None, 5)
    vector1.show()
    vector = [vector1.get_random_number_in_bounds(i) for i in range(vector1.length)]
    vector1.set_vector(vector)
    vector1.show()

