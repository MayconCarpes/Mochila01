from dataclasses import dataclass


@dataclass
class KnapsackInstance:
    name: str
    n: int
    capacity: int
    weights: list
    profits: list
    optimal_profit: int
