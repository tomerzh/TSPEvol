from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator


class TSPFitnessEvaluator(SimpleIndividualEvaluator):
    def __init__(self):
        super().__init__()

    def _evaluate_individual(self, individual):
        fitness = 0
        for i in range(individual.size() - 1):
            fitness += individual.cell_value(i).distance(individual.cell_value(i + 1))
        fitness += individual.cell_value(individual.size() - 1).distance(individual.cell_value(0))
        return fitness

