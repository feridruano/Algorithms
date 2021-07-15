# Selection Sort

Imagine splitting an array into two partitions, a sorted and an unsorted partition. Search through the unsorted partition to find the smallest value. Insert the value at the end of the sorted partition which starts on the left side. Repeat until all values are sorted in ascending order.



## Pseudocode

- Loop through the array, left to right. 

- Store the smallest value's index which is equivalent to`ith` loop's value, initially.
  - Loop through the unsorted partition to potentially find a smaller value and its index.

- Swap the value at the start of the unsorted partition with that of the smallest value found.

- Repeat until all values are sorted in ascending order.



## Pitfalls

- People don't understand how the index of the outer loop and the inner loop work together to create the sorted and unsorted partitions in a single array.
  - The best method of understanding this concept is to run through the algorithm on a piece of paper. The focus should placed on how the sorted and unsorted partitions increase and decrease in size, respectively, each loop.
- People confuse Selection Sort for Insertion Sort.
  - Selection Sort chooses the next smallest value to add at the end of the sorted partition.
  - Insertion Sort finds the index within the sorted partition for any value.

