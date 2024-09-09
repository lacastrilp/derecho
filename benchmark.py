import pandas as pd
from measure import measure_sorting
import U_Bubble
import U_Bucket


class SortingBenchmark:
    sorting_methods = [
        ("Bubble Sort", U_Bubble.bubble_sort),
        ("Bucket Sort", U_Bucket.bucket_sort)
    ]

    @staticmethod
    def run_benchmarks(arr):
        results = {"Size del arreglo": [len(arr)]}

        for method_name, method in SortingBenchmark.sorting_methods:
            benchmark_func = measure_sorting(method, method_name)
            execution_time, memory_use, operations, space_complexity = benchmark_func(arr)
            results[method_name + "_time"] = [execution_time]
            results[method_name + "_operations"] = [operations]
            results[method_name + "_space_complexity"] = [space_complexity]

        return pd.DataFrame(results)
