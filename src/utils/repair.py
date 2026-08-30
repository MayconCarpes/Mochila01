def repair_solution(solution, weights, profits, capacity):
    total_weight = sum(w * s for w, s in zip(weights, solution))
    if total_weight <= capacity:
        return solution

    solution = solution[:]
    ratios = [
        (profits[i] / weights[i] if weights[i] > 0 else float('inf'), i)
        for i in range(len(solution)) if solution[i] == 1
    ]
    ratios.sort()

    for _, i in ratios:
        if total_weight <= capacity:
            break
        solution[i] = 0
        total_weight -= weights[i]

    return solution
