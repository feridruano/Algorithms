def partition(array, start, end):
    pivot = array[end]
    left_pointer = start
    right_pointer = end - 1
    while True:
        while array[left_pointer] < pivot:
            left_pointer += 1
        while array[right_pointer] > pivot:
            right_pointer -= 1
        if left_pointer >= right_pointer:
            break
        else:
            array[left_pointer], array[right_pointer] = array[
                right_pointer], array[left_pointer]
    array[left_pointer], array[end] = array[end], array[left_pointer]
    return left_pointer


def quickselect(array, position, start, end):
    if len(array) <= 1:
        return array[0]
    pivot_index = partition(array, start, end)
    if position < pivot_index:
        return quickselect(array, position, start, pivot_index - 1)
    elif position > pivot_index:
        return quickselect(array, position, pivot_index + 1, end)
    else:
        return array[pivot_index]


# Main Program
array = [0, 5, 2, 1, 6, 3]
print("Array: %s" % array)
print("One Partition: %s" % partition(array, 0, len(array) - 1))
array = [0, 5, 2, 1, 6, 3]
print("Resetting Array... Then Quickselecting Third Lowest Value: %s" %
      quickselect(array, 2, 0,
                  len(array) - 1))
