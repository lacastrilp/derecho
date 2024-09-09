def bucket_sort(arr):
    if len(arr) == 0:
        return arr, 0

    # Convertir cada palabra a su valor ASCII total
    ascii_values = [sum(ord(char) for char in word) for word in arr]

    # Crear cubetas basadas en los valores ASCII
    min_value = min(ascii_values)
    max_value = max(ascii_values)
    bucket_size = 5  # Puedes ajustar esto
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    operations = 0

    for value, word in zip(ascii_values, arr):
        index = (value - min_value) // bucket_size
        buckets[index].append((value, word))
        operations += 1

    sorted_arr = []
    for bucket in buckets:
        sorted_bucket = sorted(bucket, key=lambda x: x[0])
        sorted_arr.extend([word for _, word in sorted_bucket])
        operations += len(bucket)

    return sorted_arr, operations