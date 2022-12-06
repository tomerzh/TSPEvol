from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator

class TSPFitnessEvaluator(SimpleIndividualEvaluator):
    def __init__(self):
        super().__init__()

    def _evaluate_individual(self, individual):
        fitness = 0
        for i in range(len(individual) - 1):
            fitness += individual[i].distance(individual[i + 1])
        fitness += individual[len(individual) - 1].distance(individual[0])
        return fitness