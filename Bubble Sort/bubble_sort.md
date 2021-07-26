# Bubble Sort

A brute-force sorting algorithm for an array that consecutively compares two values and shifts the larger value toward the end of the array, bubbling up the largest value each pass-through. The array will have two partitions, an unsorted and sorted partition. At the end of each pass-through, the unsorted partition will decrease in size by one and the sorted partition will increase in size by one.

**Note:** The Bubble Sort listed here is the slowest version with two for loops.

## Pseudocode

- [x] Given an array.
- [x] Loop through each value of the array, except the last value for N - 1 pass-throughs.
  - [x] Loop through the unsorted partition.
    - [x] When the value at the index of the unsorted partition is greater than the value ahead, on the right, then swap both values.

## Code Implementation

```python
def bubble_sort(array):
    for index in range(len(array) - 1):
        for unsorted_index in range(len(array) - 1 - index):
            if array[unsorted_index] > array[unsorted_index + 1]:
                array[unsorted_index], array[unsorted_index + 1] = array[
                    unsorted_index + 1], array[unsorted_index]
    return array
```

## Time Complexity

Time complexity is `O(N^2)`, quadratic time. Each time the data is doubled, the number of steps increases dramatically.  

#### Worst-Case:

The values to be sorted are already sorted, but in reverse order.

#### Best-Case:

The value being searched for is the first value in the middle.

## Space Complexity

Space complexity is `O(1)`, constant space.
