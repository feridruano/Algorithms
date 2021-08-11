# Quicksort

A **divide and conquer** sorting algorithm that recursively partitions an array into sub-arrays. Each partition choose a pivot and orders elements less than the pivot to the left and elements greater than the pivot to the right.

## Pseudocode

### Partition

- [x] Given an array with a start and end parameter, indexes.
- [x] Assign the pivot to be the last element in the array using the end parameter.
- [x] Assign the left pointer to be the index of the start parameter.
- [x] Assign the right pointer to be the index before the end parameter.
- [x] Create an infinite loop that will be stopped based on a condition inside its scope.
  - [x] Loop through the array starting at the left pointer.
    - [x] When the value of the element at the left pointer is less than the value of the pivot, increment the left pointer. Otherwise, stop the loop.
  - [x] Loop through the array backwards from the right pointer.
    - [x] When the value of the element at the right pointer is greater than the value of the pivot, increment the right pointer. Otherwise, stop the loop.
  - [x] When the left pointer is at the same position or passed the right pointer, stop out of the infinite loop. Otherwise, swap the values of the left and right pointers and continue onto the next loop.
- [x] Swap the value at the left pointer with that of the pivot. All values less than the pivot will be to the left and all values greater than the pivot will be to the right.
- [x] Return the index of the left pointer where the pivot is now at.

### Quicksort

- [x] Given an array with a start and end parameter, indexes.

- [x] When the array has zero or one elements return the array.

- [x] Assign the pivot index to be the result of calling the partition function on the array and its parameters

- [x] Recursively call quicksort on the sub-array to the left of the pivot by decrementing pivot index as a parameter.

- [x] Recursively call quicksort on the sub-array to the right of the pivot by incrementing pivot index as a parameter.

  

## Time Complexity

The time complexity of the partition function is at least `O(N)` and at most `O(N) ` comparisons plus `O(N/2)` swaps which is still `O(N)`.

The time complexity of the quicksort recursion is at least `O(N * log N)` and at most `O(N^2 / 2)` which is `O(N^2)`.



# Quickselect

A **divide and conquer** selection algorithm that recursively partitions an array into sub-arrays and ignores half of each sub-array to find the correct value at the `nth` selected position in the array. Basically, combining quicksort with binary search to find the correct value at any index.

**Note:** This is a selection of the correct value at any index. Not a search for a value!

## Pseudocode

### Partition

- [x] Given an array with a start and end parameter, indexes.
- [x] Assign the pivot to be the last element in the array using the end parameter.
- [x] Assign the left pointer to be the index of the start parameter.
- [x] Assign the right pointer to be the index before the end parameter.
- [x] Create an infinite loop that will be stopped based on a condition inside its scope.
  - [x] Loop through the array starting at the left pointer.
    - [x] When the value of the element at the left pointer is less than the value of the pivot, increment the left pointer. Otherwise, stop the loop.
  - [x] Loop through the array backwards from the right pointer.
    - [x] When the value of the element at the right pointer is greater than the value of the pivot, increment the right pointer. Otherwise, stop the loop.
  - [x] When the left pointer is at the same position or passed the right pointer, stop out of the infinite loop. Otherwise, swap the values of the left and right pointers and continue onto the next loop.
- [x] Swap the value at the left pointer with that of the pivot. All values less than the pivot will be to the left and all values greater than the pivot will be to the right.
- [x] Return the index of the left pointer where the pivot is now at.

### Quickselect

- [x] Given an array with an `nth` position, start, and end parameter, indexes.
- [x] When the array has zero or one elements return the first element in the array.
- [x] Assign the pivot index as the result of a partition call.
- [x] When the `nth` position is less than the pivot index, recursively call the quickselect algorithm with the boundaries of the left sub-array.
- [x] When the `nth` position is greater than the pivot index, recursively call the quickselect algorithm with the boundaries of the right sub-array.
- [x] When the `nth` position is equal to the pivot index, return the value at the index.

## Time Complexity

The time complexity is `O(N * log N)`.
