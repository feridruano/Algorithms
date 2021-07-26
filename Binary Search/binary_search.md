# Binary Search

A divide and conquer searching algorithm that repeatedly divides a ***sorted array*** in half to compare the value in the middle of the array against the value being searched for. When the value in the middle is smaller than the value being searched for, the first half of the sorted array is disregarded and we continue our search on the second half of the sorted array. The opposite is true when the value in middle is greater than the value being searched for. The value being searched for is found when equal to the value in the middle or not found after repeatedly dividing the sorted array until no more division are possible.

## Pseudocode

- [x] Given a sorted array and a target to search for.
- [x] Track array boundaries to repeatedly divide the sorted array in half later.
- [x] Repeatedly divide the sorted array in half using the array boundaries until no more divisions are possible.
  - [x] Calculate the new middle index using the array boundaries.
  - [x] When the value at the middle index is equal to the target, return True.
  - [x] When the value at the middle index is smaller than the target, adjust the lower bound to disregard the first half of the sorted array.
  - [x] When the value at the middle index is greater than the target, adjust the upper bound to disregard the second half of the sorted array.
- [x] After no more divisions are possible and the target has not been found, return false.

## Code Implementation

```python
def binary_search(array, target):
	lower_bound = 0
	upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        middle_index = lower_bound + (upper_bound - lower_bound) // 2
        if array[middle_index] == target:
            return True
        elif array[middle_index] < target:
            lower_bound = middle_index + 1
        else:
            upper_bound = middle_index - 1
    return False
```

## Time Complexity

Time complexity is `O(log N)`, logarithmic time. Doubling the array data only increases the binary search algorithm by one step and we can determine the worst-case number of steps the algorithm will take for any array of size N using Log<sub>2</sub> N.

#### Worst-Case: #1

The value being searched for is the last value in the array.

#### Worst-Case: #2

The value being searched for is not in the array.

#### Best-Case:

The value being searched for is the first value in the middle.

## Space Complexity

Space complexity is `O(1)`, constant space. The algorithm uses constant (same) memory to store an array of N size, upper and lower boundaries, and middle index. 