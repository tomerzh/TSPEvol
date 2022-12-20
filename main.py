import csv

from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation

from city import City
from city_vector import CityVector
from permutation_ga.permutation_creator import PermutationCreator
from permutation_ga.permutation_mutation import PermutationMutation
from permutation_ga.permutation_crossover import PermutationCrossover
from tsp_fitness_evaluator import TSPFitnessEvaluator


def main():
    vector = [City(30, 17), City(22, 1), City(300, 45), City(423, 54), City(51, 26),
              City(6, 7), City(7, 8), City(81, 19), City(94, 10), City(10, 111)]
    if vector is not None:
        number_of_cities = len(vector)
    else:
        number_of_cities = 10

    population_size = 10
    max_generation = 50

    algo = SimpleEvolution(
        Subpopulation(creators=PermutationCreator(length=number_of_cities, city_vector=vector),
                      population_size=population_size,
                      evaluator=TSPFitnessEvaluator(),
                      higher_is_better=False,
                      elitism_rate=0.0,
                      operators_sequence=[PermutationCrossover(),
                                          PermutationMutation(0.1)],
                      selection_methods=[(TournamentSelection(tournament_size=4, higher_is_better=False), 1)]),
        breeder=SimpleBreeder(),
        max_workers=1,
        max_generation=max_generation,
        statistics=BestAverageWorstStatistics()
    )
    print("EA Process Presented Bellow:")

    # evolve the generated initial population
    algo.evolve()
    print("#####################################")

    print("The Ultimate solution found by our solver is:")
    # for printing writing csv | NEED TO UNCOMMENT algo.finish #######################################################
    # algo.finish()
    with open('data.csv', mode='a') as data_file:
        data_writer = csv.writer(data_file, delimiter=',')
        data_writer.writerow([algo.best_of_run_.get_pure_fitness()])
    print(algo.best_of_run_.get_pure_fitness())
    # algo.finish()



if __name__ == '__main__':
    main()
