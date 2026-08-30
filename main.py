import random
from data.instances import get_all_instances
from src.algorithms import TabuSearch, GeneticAlgorithm
from src.runners.experiment import ExperimentRunner
from src.runners.report import ReportGenerator


def build_algorithms():
    algorithms = []

    for tabu_size in [5, 10, 20]:
        for max_iter in [100, 500, 1000]:
            algorithms.append(TabuSearch(tabu_size=tabu_size, max_iterations=max_iter))

    for pop_size in [50, 100]:
        for generations in [100, 500, 1000]:
            for mutation_rate in [0.01, 0.05]:
                algorithms.append(
                    GeneticAlgorithm(
                        pop_size=pop_size,
                        generations=generations,
                        mutation_rate=mutation_rate,
                    )
                )

    return algorithms


def main():
    random.seed(42)

    instances = get_all_instances()
    algorithms = build_algorithms()

    runner = ExperimentRunner(instances, algorithms, repetitions=3)
    results = runner.run()

    report = ReportGenerator(results)
    report.generate_csv("resultados.csv")
    report.generate_docx("relatorio.docx")

    print(f"\nTotal de execucoes: {len(results)}")
    print("Arquivos gerados: resultados.csv, relatorio.docx")


if __name__ == "__main__":
    main()
