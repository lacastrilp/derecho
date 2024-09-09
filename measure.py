import time
import psutil
from functools import wraps


def measure_sorting(func, method_name, *func_args):
    @wraps(func)
    def wrapper(arr, *wrapper_args):
        process = psutil.Process()

        # Convertir cada palabra a su valor ASCII total
        ascii_values = [sum(ord(char) for char in word) for word in arr]

        # Print the array before sorting if its length is 50
        if len(arr) == 50:
            print("Array before sorting:", arr)

        # Measuring memory before execution
        before_memory = process.memory_info().rss

        # Measuring execution time
        start_time = time.time()
        sorted_arr, operations = func(arr, *func_args)
        end_time = time.time()

        # Measuring memory after execution
        after_memory = process.memory_info().rss

        execution_time = max(end_time - start_time, 1e-9)  # Ensure positive value
        memory_used = max((after_memory - before_memory) / 1024, 1e-9)  # Ensure positive value in KB
        space_complexity = max((after_memory - before_memory) / 1024, 1e-9)  # Ensure positive value in KB

        # Print the array after sorting if its length is 50
        if len(arr) == 50:
            print("Array after sorting:", sorted_arr)

        print(f"Sorting Method: {method_name}")
        print(f"Array Size: {len(arr)}")
        print(f"Tiempo de ejecución: {execution_time:.9f} segundos")
        print(f"Número de operaciones: {operations}")
        print(f"Complejidad Espacial: {space_complexity:.9f} KB")
        print("--------------------------------------------------")

        return execution_time, memory_used, operations, space_complexity

    return wrapper
