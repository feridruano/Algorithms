# Binary Search

**Type:** Divide and Conquer

**Input:** Sorted Array of Elements

Binary Search divides a sorted array into two sub-arrays by determining the middle index. Then, the target element is compared against the middle index's value. If the target element is equal to : : return found, less than : : ignore the right sub-array, greater than : : ignore the left sub-array. On the remaining sub-array, repeat the entire process of divide and conquer (comparisons) until the target element is potentially found. Otherwise, the target element does not exist.

### Middle Index

The middle index is constantly changing with each division and calculating a middle index is as easy as `(low + high) / 2 `. However, this is not necessarily correct due to the potential of a buffer overflow.

### Buffer Overflow

Image an `int` data type were the range of possible values is between `-7 and 8`. We have a sorted array of elements with a length of 8. In the first division, if the target value is greater than the middle element, then `(Any Value > 1 + 7) / 2` produces a buffer overflow. The reason is because `(Any Value > 1 + 7)` have the data type of `int` and thereby must produce an a value of data type `int`, however, the value produced is greater than the maximum possible value of `8` resulting in a buffer overflow, negative middle element.

Note: 

- Yes, obviously `8` is not the maximum value an `int` can hold in reality. Totally depends on the language.
- Yes, this a buffer overflow from calculating the middle index does not happen often, but it's possible!

### Better Middle Index

The better method of calculating the middle index is `low + (High - Low) / 2`. This works because `(High - Low)` and `Low + (High - Low)` can never produce a buffer overflow, a value greater than what an `int` can hold.

### Pseudocode

Set the `Low`and `High` of the sorted array.

<u>*Divide Step: Two Sorted Sub-Arrays Based on Middle Index*</u>

Calculate the middle index using `low + (High - Low) / 2`.

<u>*Conquer Step: Compare the Target Element to the Middle Value*</u>

If the target item is equal to the middle value, then return item found.

If the target item is less than the middle value, then return the left sub-array.

​	Repeat entire process from the beginning using the left sub-array.

If the target item is greater than the middle value, then return the right sub-array.

​	Repeat entire process from the beginning using the right sub-array.

If the entire sorted array is searched, then return item not found (i.e `Low > High`).

### Time Complexity

Binary Search is `O(log n)` as for each operation half of the sorted array (or sub-array) is ignored and not used to search for the target item. The array can be divided 2<sup>x</sup> times until the target element is found or there is one remaining array element to compare.

1 = Smallest possible array (one element) before target is not found

n = Length of sorted array (or sub-arrays)

2<sup>x</sup>  = Number of division by 2 needed

1 = n / 2<sup>x</sup> 

2<sup>x</sup>  * (1) = (n / 2<sup>x</sup>) * 2<sup>x</sup> 

2<sup>x</sup>  = n

log<sub>2</sub> * 2<sup>x</sup>  = n * log<sub>2</sub>

x log<sub>2</sub> 2= log<sub>2</sub> n

x * (1) = log<sub>2</sub> n 

x = log<sub>2</sub> n

O(log n)

### Space Complexity

Binary Search space complexity is `O(1)` or constant space for the function call and constant space for variable allocations (i.e an array with elements). This applies to both the iterative and tail-recursive implementations. Recursive implementation use call stack to temporarily store each recursive call.