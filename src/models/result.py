from dataclasses import dataclass, field


@dataclass
class ExecutionResult:
    instance_name: str
    algorithm_name: str
    params: dict
    best_profit: int
    best_solution: list
    optimal_profit: int
    gap_percent: float
    time_seconds: float
    iterations: int
    convergence_history: list = field(default_factory=list)
