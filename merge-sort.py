def merge(values, left, middle, right):
    right_start = middle + 1
    if values[middle] <= values[right_start]:
        return
    while left <= middle and right_start <= right:
        if values[left] <= values[right_start]:
            left += 1
        else:
            value = values[right_start]
            index = right_start
            while index != left:
                values[index] = values[index - 1]
                index -= 1
            values[left] = value
            left += 1
            middle += 1
            right_start += 1

## YOUR CODE IN THIS FUNCTION
# left and right will never be None
def merge_sort(values, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort(values, middle, left)
        merge_sort(values, middle + 1, right)
        merge(values, left, middle, right)
