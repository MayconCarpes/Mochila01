def greedy_solution(weights, profits, capacity):
    n = len(weights)
    ratios = [
        (profits[i] / weights[i] if weights[i] > 0 else float('inf'), i)
        for i in range(n)
    ]
    ratios.sort(reverse=True)

    solution = [0] * n
    remaining = capacity

    for _, i in ratios:
        if weights[i] <= remaining:
            solution[i] = 1
            remaining -= weights[i]

    return solution
