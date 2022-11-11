def bubble_sort(values):
    for i in range(len(values)):
        for j in range(len(values) - i - 1):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
