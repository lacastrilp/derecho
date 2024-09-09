from benchmark import SortingBenchmark
import pandas as pd
from plot_utils import plot_results
from file_utils import leer_palabras_archivo
from export_to_excel import export_results_to_excel
from datetime import datetime


def run_benchmarks_and_collect_results(file_path, sizes):
    all_results = []
    total_words = 0
    for size in sizes:
        palabras = leer_palabras_archivo(file_path, size)
        if not palabras:
            break
        total_words = len(palabras)
        df_results = SortingBenchmark.run_benchmarks(palabras)
        all_results.append(df_results)
    return all_results, total_words


def plot_all_results(df_all_results):
    sorting_methods = SortingBenchmark.sorting_methods
    plot_results(df_all_results, "Size del arreglo",
                 [method_name + "_time" for method_name, _ in sorting_methods],
                 [method_name for method_name, _ in sorting_methods],
                 "Tiempo de ejecución en función del tamaño del arreglo")
    plot_results(df_all_results, "Size del arreglo",
                 [method_name + "_operations" for method_name, _ in sorting_methods],
                 [method_name for method_name, _ in sorting_methods],
                 "Operaciones en función del tamaño del arreglo")
    plot_results(df_all_results, "Size del arreglo",
                 [method_name + "_space_complexity" for method_name, _ in sorting_methods],
                 [method_name for method_name, _ in sorting_methods],
                 "Complejidad Espacial en función del tamaño del arreglo")


def main():
    start_time = datetime.now()
    print(f"Hora de inicio: {start_time}")

    file_path = 'C:/Users/Alejandro Castrillon/PycharmProjects/AlgoritBubBuck/palabras.es'
    sizes = [50] + list(range(10000, 260000, 10000))  # Start at 50, then increment by 10000 up to 250000
    all_results, total_words = run_benchmarks_and_collect_results(file_path, sizes)

    if all_results:
        df_all_results = pd.concat(all_results, ignore_index=True)
        plot_all_results(df_all_results)
        export_results_to_excel(df_all_results)

    end_time = datetime.now()
    print(f"Hora de fin: {end_time}")


if __name__ == "__main__":
    main()
