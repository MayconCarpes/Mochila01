import time
import random
from src.algorithms.base import BaseAlgorithm
from src.models import KnapsackInstance, ExecutionResult
from src.utils.greedy import greedy_solution
from src.utils.repair import repair_solution


class GeneticAlgorithm(BaseAlgorithm):
    def __init__(self, pop_size=100, generations=500, crossover_rate=0.8, mutation_rate=0.05):
        params = {
            "pop_size": pop_size,
            "generations": generations,
            "crossover_rate": crossover_rate,
            "mutation_rate": mutation_rate,
        }
        super().__init__("Algoritmo Genetico", params)
        self.pop_size = pop_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def _initialize_population(self, instance):
        population = [greedy_solution(instance.weights, instance.profits, instance.capacity)]

        for _ in range(self.pop_size - 1):
            individual = [random.randint(0, 1) for _ in range(instance.n)]
            individual = repair_solution(
                individual, instance.weights, instance.profits, instance.capacity
            )
            population.append(individual)

        return population

    def _tournament_selection(self, population, fitnesses, k=3):
        selected = random.sample(range(len(population)), k)
        winner = max(selected, key=lambda i: fitnesses[i])
        return population[winner][:]

    def _crossover(self, parent1, parent2):
        if random.random() > self.crossover_rate:
            return parent1[:], parent2[:]
        point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2

    def _mutate(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]
        return individual

    def solve(self, instance: KnapsackInstance) -> ExecutionResult:
        start = time.time()

        population = self._initialize_population(instance)
        best = None
        best_profit = -1
        convergence = []

        for _ in range(self.generations):
            fitnesses = [
                self.calculate_profit(ind, instance.profits) for ind in population
            ]

            gen_best_idx = max(range(len(population)), key=lambda i: fitnesses[i])
            if fitnesses[gen_best_idx] > best_profit:
                best = population[gen_best_idx][:]
                best_profit = fitnesses[gen_best_idx]

            convergence.append(best_profit)

            new_population = [best[:]]

            while len(new_population) < self.pop_size:
                parent1 = self._tournament_selection(population, fitnesses)
                parent2 = self._tournament_selection(population, fitnesses)
                child1, child2 = self._crossover(parent1, parent2)
                child1 = repair_solution(
                    self._mutate(child1),
                    instance.weights,
                    instance.profits,
                    instance.capacity,
                )
                child2 = repair_solution(
                    self._mutate(child2),
                    instance.weights,
                    instance.profits,
                    instance.capacity,
                )
                new_population.append(child1)
                if len(new_population) < self.pop_size:
                    new_population.append(child2)

            population = new_population

        elapsed = time.time() - start
        gap = (
            (instance.optimal_profit - best_profit) / instance.optimal_profit * 100
            if instance.optimal_profit > 0
            else 0.0
        )

        return ExecutionResult(
            instance_name=instance.name,
            algorithm_name=self.name,
            params=self.params,
            best_profit=best_profit,
            best_solution=best,
            optimal_profit=instance.optimal_profit,
            gap_percent=round(gap, 2),
            time_seconds=round(elapsed, 4),
            iterations=self.generations,
            convergence_history=convergence,
        )
