import time
import random
from collections import deque
from src.algorithms.base import BaseAlgorithm
from src.models import KnapsackInstance, ExecutionResult
from src.utils.greedy import greedy_solution
from src.utils.repair import repair_solution


class TabuSearch(BaseAlgorithm):
    def __init__(self, tabu_size=10, max_iterations=500):
        params = {"tabu_size": tabu_size, "max_iterations": max_iterations}
        super().__init__("Busca Tabu", params)
        self.tabu_size = tabu_size
        self.max_iterations = max_iterations

    def solve(self, instance: KnapsackInstance) -> ExecutionResult:
        start = time.time()

        current = greedy_solution(instance.weights, instance.profits, instance.capacity)
        current_profit = self.calculate_profit(current, instance.profits)

        best = current[:]
        best_profit = current_profit

        tabu_list = deque(maxlen=self.tabu_size)
        convergence = [best_profit]

        for _ in range(self.max_iterations):
            best_neighbor = None
            best_neighbor_profit = -1
            best_move = -1

            for i in range(instance.n):
                neighbor = current[:]
                neighbor[i] = 1 - neighbor[i]
                neighbor = repair_solution(
                    neighbor, instance.weights, instance.profits, instance.capacity
                )
                neighbor_profit = self.calculate_profit(neighbor, instance.profits)

                is_tabu = i in tabu_list
                aspiration = neighbor_profit > best_profit

                if (not is_tabu or aspiration) and neighbor_profit > best_neighbor_profit:
                    best_neighbor = neighbor
                    best_neighbor_profit = neighbor_profit
                    best_move = i

            if best_neighbor is None:
                break

            current = best_neighbor
            current_profit = best_neighbor_profit
            tabu_list.append(best_move)

            if current_profit > best_profit:
                best = current[:]
                best_profit = current_profit

            convergence.append(best_profit)

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
            iterations=len(convergence) - 1,
            convergence_history=convergence,
        )
