# Partition - Sorting Elements
def partition(array, left_pointer, right_pointer):
    pivot_index = right_pointer
    pivot = array[pivot_index]
    right_pointer -= 1

    while True:
        while array[left_pointer] < pivot:
            left_pointer += 1

        while array[right_pointer] > pivot:  # Negative Index Breaks the Loop
            right_pointer -= 1

        if left_pointer >= right_pointer:
            break
        else:
            array[left_pointer], array[right_pointer] = array[
                right_pointer], array[left_pointer]
            left_pointer += 1

    array[left_pointer], array[pivot_index] = array[pivot_index], array[
        left_pointer]

    return left_pointer


# Quicksort - Recursive Subproblems
def quicksort(array, left_pointer, right_pointer):
    if right_pointer - left_pointer <= 0:
        return array
    pivot_index = partition(array, left_pointer, right_pointer)
    quicksort(array, left_pointer, pivot_index - 1)
    quicksort(array, pivot_index + 1, right_pointer)
    return array


# Main Program
array = [0, 5, 2, 1, 6, 3]
print("Array: %s" % array)
print("One Partition: %s" % partition(array, 0, len(array) - 1))
array = [0, 5, 2, 1, 6, 3]
print("Resetting Array... Then Quicksorting: %s" %
      quicksort(array, 0,
                len(array) - 1))
