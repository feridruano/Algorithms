### Problems and Exercises

**1.1-1** 

Give a real-world example that requires sorting or a real-world example that requires computing a convex hull. 

A real-world example that requires sorting is sorting a randomized deck of cards.

**1.1-2** 

Other than speed, what other measures of efficiency might one use in a real-world setting? 

Another measure of efficiency is space complexity.

**1.1-3** 

Select a data structure that you have seen previously, and discuss its strengths and limitations. 

An array is a data structure that holds items in a list. These items are stored in a contiguous block of memory. A contiguous block of memory as strengths and limitations.

**Strengths**

- Constant time lookup/modification within the bounds of the array by knowing the index (position) of the item in the array.
- Take up less space in memory compared to other list data structures.

**Limitation**

- Static contiguous block of memory that must be resized when adding an item to a full array.
- Items must be shifted either left or right when a deletion or insertion happens, respectfully.

**1.1-4** 

How are the shortest-path and traveling-salesman problems given above similar? How are they different? 

The shortest-path and traveling-salesman both walk a graph to find a path in them, but differ in the number of connections per point.

**1.1-5** 

Come up with a real-world problem in which only the best solution will do. Then come up with one in which a solution that is “approximately” the best is good enough.

N/A, but traveling-salesman works for the approximation question.

**1.2-1** 

Give an example of an application that requires algorithmic content at the application level, and discuss the function of the algorithms involved. 

Google Maps require algorithmic content at the application level. The algorithms provide solutions to understanding where in the world a user is and a possible shortest path to a destination. 

**1.2-2** 

Suppose we are comparing implementations of insertion sort and merge sort on the same machine. For inputs of size n, insertion sort runs in `8n^2` steps, while merge sort runs in `64n * lg n` steps. For which values of n does insertion sort beat merge sort? 

We must find the maximum value of n, crossover point, where insertion sort becomes slower than merge sort using the same machine. 

- My problem solving skills were help and lead to the correct idea, but I stumbled at the end due to the lack of mathematical knowledge. I'm just glad that I was able to think about the problem conceptually which lead me to the beginning of the solution. Eventually I'll be able to solve this problem without looking at the final step.

**1.2-3** 

What is the smallest value of n such that an algorithm whose running time is `100n^2` runs faster than an algorithm whose running time is `2^n` on the same machine?

The time complexity between both algorithms changes drastically with each increase in n. Therefore, we can easily check the smallest numbers starting from 1 using brute force or binary search. `100n^2` will always be faster than `2^n`  until n is greater than 15.

**1-1** 

Comparison of running times 

For each function f(n) and time t in the following table, determine the largest size n of a problem that can be solved in time t, assuming that the algorithm to solve the problem takes f(n) microseconds.

 

|        | 1 second | 1 minute | 1 hour | 1 day | 1 month | 1 year | 1 century |
| ------ | -------- | -------- | ------ | ----- | ------- | ------ | --------- |
| lg n   |          |          |        |       |         |        |           |
| sqrt n |          |          |        |       |         |        |           |
| n      |          |          |        |       |         |        |           |
| n lg n |          |          |        |       |         |        |           |
| n^2    |          |          |        |       |         |        |           |
| n^3    |          |          |        |       |         |        |           |
| 2^n    |          |          |        |       |         |        |           |
| n!     |          |          |        |       |         |        |           |

