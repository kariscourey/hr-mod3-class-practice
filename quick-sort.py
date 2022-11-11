# left and right will never be None

def partition(values, left, right):
    # pivot = values[right]
    pivot_index = right
    # swap index = left - 1
    swap_index = left - 1
    # for each index from left to right - 1
    for i in range(left:right-1):
        # if the value at index is less than or equal to pivot value
        if values[i] <=  values[pivot_index]:
            # increment the swap index
            swap_index += 1
            # swap the values at swap index & loop index
            values[swap_index], values[i] = values[i], values[swap_index]
    # increment the swap index
    swap_index += 1
    # swap value at the swap index with value at right index
    values[swap_index], values[pivot_index] = values[pivot_index], values[swap_index]
    # return the swap index
    return swap_index


def quicksort(values, left, right):
    # If left >= right or left < 0, just return
    if left >= right or left < 0:
        return

    # p = Call the partition function for values, left, and right
    partition_index = partition(values, left, right)

    # Quicksort the values from left to p - 1
    quicksort(values, left, partition_index - 1)

    # Quicksort the values from p + 1 to right
    quicksort(values, partition_index + 1, right)
