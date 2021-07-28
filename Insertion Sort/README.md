# Insertion Sort

A brute-force sorting algorithm for an array that will have two partitions, an unsorted and sorted partition. The first value of the unsorted partition is positioned inside the sorted partition by shifting sorted values and inserted the first value in the correct slot, each pass-through. At the end of each pass-through, the unsorted partition will decrease in size by one and the sorted partition will increase in size by one. 

## Pseudocode

- [x] Given an array.
- [x] Loop through each value of the array.
  - [x] Loop through the sorted partition backwards, until the second value of the sorted partition.
    - [x] When the value before is greater than the value to be positioned and inserted, on the left, then swap both values.
    - [x] Otherwise continue to the next pass-through.

## Code Implementation

```python
def insertion_sort(array):
    for index in range(1, len(array)):
        for position in reversed(range(1, index + 1)):
            if(array[position - 1] > array[position]):
              array[position], array[position - 1] = array[position - 1], array[position]
            else:
                continue
```

## Time Complexity

Time complexity is `O(N^2)`, linear time. Each time the data is doubled, the number of steps increase dramatically.  

#### Worst-Case:

The values to be sorted are already sorted, but in reverse order.

#### Best-Case:

The values to be sorted are already sorted.

## Space Complexity

Space complexity is `O(1)`, constant space.

