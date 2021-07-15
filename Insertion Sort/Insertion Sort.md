# Insertion Sort

Imagine splitting an array into two partitions, a sorted and an unsorted partition. From the unsorted partition select the value at the start. Insert the value into the correct position in the sorted array 



## Pseudocode

I can't explain it concisely while explaining the bounds of each for loop.



The element at the start of the array will be considered the first sorted element. Therefore, an outer loop will iterate starting from the second element to the last element of the array, considered the unsorted partition. An inner loop will iterate from the start of the unsorted partition to second element of the array in reverse, considered as iterating over the sorted partition. Swap the element with previous element until the value is positioned correctly in the sorted partition.



## Pitfalls

- People don't understand how the index of the outer loop and the inner loop work together to create the sorted and unsorted partitions in a single array.
  - The best method of understanding this concept is to run through the algorithm on a piece of paper. The focus should placed on how the sorted and unsorted partitions increase and decrease in size, respectively, each loop.
- People confuse Selection Sort for Insertion Sort.
  - Selection Sort chooses the next smallest value to add at the end of the sorted partition.
  - Insertion Sort finds the index within the sorted partition for any value.

