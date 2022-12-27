import csv

from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation

from city import City
from permutation_ga.permutation_creator import PermutationCreator
from permutation_ga.permutation_mutation import PermutationMutation
from permutation_ga.permutation_crossover import PermutationCrossover
from tsp_fitness_evaluator import TSPFitnessEvaluator


def main():
    vector = [City(30, 17), City(22, 1), City(300, 45), City(423, 54), City(51, 26),
              City(6, 7), City(7, 8), City(81, 19), City(94, 10), City(3, 250), City(1, 666), City(244, 1234),
              City(522, 2145), City(0, 21), City(222, 1113)]
    if vector is not None:
        number_of_cities = len(vector)
    else:
        number_of_cities = 10

    population_size = 10
    max_generation = 100
    number_of_iterations = 80

    for i in range(number_of_iterations):
        algo = SimpleEvolution(
            Subpopulation(creators=PermutationCreator(length=number_of_cities, city_vector=vector),
                          population_size=population_size,
                          evaluator=TSPFitnessEvaluator(),
                          higher_is_better=False,
                          elitism_rate=0.1,
                          operators_sequence=[PermutationCrossover(0.8),
                                              PermutationMutation(0.1)],
                          selection_methods=[(TournamentSelection(tournament_size=4, higher_is_better=False), 1)]),
            breeder=SimpleBreeder(),
            max_workers=1,
            max_generation=max_generation,
            statistics=BestAverageWorstStatistics()
        )
        print("EA Process Presented Bellow:")

        # for j in range(max_generation):
        #     algo.generation_iteration()
        #     print("Generation: ", j, " Best: ", algo.best_of_gen.fitness)

        # evolve the generated initial population
        algo.evolve()
        print("#####################################")

        print("The Ultimate solution found by our solver is:")
        algo.finish()
        with open('data.csv', mode='a' ,newline="") as data_file:
            data_writer = csv.writer(data_file)
            data_writer.writerow([algo.best_of_run_.get_pure_fitness()])
            # x_vector = [algo.best_of_run_.get_vector()[i].get_x() for i in range(len(algo.best_of_run_.get_vector()))]
            # y_vector = [algo.best_of_run_.get_vector()[i].get_y() for i in range(len(algo.best_of_run_.get_vector()))]
            # data_writer.writerow(x_vector)
            # data_writer.writerow(y_vector)


if __name__ == '__main__':
    main()
