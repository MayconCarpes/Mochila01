from src.models import KnapsackInstance, ExecutionResult
from src.algorithms.base import BaseAlgorithm


class ExperimentRunner:
    def __init__(self, instances, algorithms, repetitions=3):
        self.instances = instances
        self.algorithms = algorithms
        self.repetitions = repetitions

    def run(self):
        results = []
        total = len(self.instances) * len(self.algorithms) * self.repetitions
        current = 0

        for instance in self.instances:
            for algorithm in self.algorithms:
                best_result = None
                times = []

                for rep in range(self.repetitions):
                    current += 1
                    print(
                        f"[{current}/{total}] {instance.name} | "
                        f"{algorithm.name} | {algorithm.params} | Rep {rep + 1}"
                    )
                    result = algorithm.solve(instance)
                    times.append(result.time_seconds)

                    if best_result is None or result.best_profit > best_result.best_profit:
                        best_result = result

                best_result.time_seconds = round(sum(times) / len(times), 4)
                results.append(best_result)

        return results
