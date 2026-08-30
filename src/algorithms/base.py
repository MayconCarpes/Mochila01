from abc import ABC, abstractmethod
from src.models import KnapsackInstance, ExecutionResult


class BaseAlgorithm(ABC):
    def __init__(self, name: str, params: dict):
        self.name = name
        self.params = params

    @abstractmethod
    def solve(self, instance: KnapsackInstance) -> ExecutionResult:
        pass

    def calculate_profit(self, solution, profits):
        return sum(p * s for p, s in zip(profits, solution))

    def calculate_weight(self, solution, weights):
        return sum(w * s for w, s in zip(weights, solution))
