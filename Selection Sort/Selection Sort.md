# Selection Sort

A brute-force sorting algorithm for an array that will have two partitions, an unsorted and sorted partition. Each pass-through finds the smallest value in the unsorted partition and inserts the value at the end of the sorted partition. At the end of each pass-through, the unsorted partition will decrease in size by one and the sorted partition will increase in size by one. 

## Pseudocode

- [x] Given an array.
- [x] Loop through each value of the array.
  - [x] Store the lowest value's index, initially the first value of the unsorted partition.
  - [x] Loop through the unsorted partition.
    - [x] When the value at the index of the unsorted partition is lower than the stored lowest value, change the stored lowest value's index.
  - [x] Swap the first value of the unsorted partition with that of the stored lowest value.

## Code Implementation

```python
def selection_sort(array):
    for index in range(0, len(array) - 1):
        lowest_value_index = index
        for position in range(index + 1, len(array)):
            if(array[lowest_value_index] > array[position]):
                lowest_value_index = position
        array[index], array[lowest_value_index] = array[lowest_value_index], array[index]
```

## Time Complexity

Time complexity is `O(N^2)`, linear time. Each time the data is doubled, the number of steps increase dramatically.  

#### Worst-Case:

The values to be sorted are already sorted, but in reverse order.

#### Best-Case:

The values to be sorted are already sorted.

## Space Complexity

Space complexity is `O(1)`, constant space.

