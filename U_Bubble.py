def bubble_sort(arr):
    n = len(arr)
    operations = 0

    # Convertir cada palabra a su valor ASCII total
    ascii_values = [sum(ord(char) for char in word) for word in arr]

    for i in range(n):
        for j in range(0, n-i-1):
            operations += 1
            if ascii_values[j] > ascii_values[j+1]:
                ascii_values[j], ascii_values[j+1] = ascii_values[j+1], ascii_values[j]
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr, operations