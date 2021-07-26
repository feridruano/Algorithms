# Binary Search

A brute-force searching algorithm for a ***sorted or unsorted array*** that compares each value against the value being searched for.

## Pseudocode

- [x] Given an array and a target to search for.
- [x] Loop through each value in the array.
  - [x] When the array value is equal to the target, return True.
- [x] After checking all values in the array, return False.

## Code Implementation

```python
def linear_search(target, array):
    for value in array:
        if value == target:
            return True
    return False
```

## Time Complexity

Time complexity is `O(N)`, linear time.  Linear search will always take N steps. Doubling the number of items in the array requires double the number of steps.

#### Worst-Case: #1

The value being searched for is the last value in the array.

#### Worst-Case: #2

The value being searched for is not in the array.

### Best-Case:

The value being searched for is the first value in the array.

## Space Complexity

Space complexity is `O(1)`, constant space.