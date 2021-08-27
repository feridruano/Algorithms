# I Foundations

## Chapter 1

***Algorithm*** - A sequence of steps that transforms an input into an output.

***Instance*** - An instance of a problem is the <u>input</u> needed to transform into an output.

***Correctness*** - For every input instance of an algorithm, it returns the correct output.

An algorithm is considered a technology and as important as computer hardware, networking, and other major technologies.

For instance, let's compare two sorting algorithms and their runtime.

```
Insertion Sort
	Time Complexity of O(N^2).
	Sort 10 million numbers.
	Uses a faster computer with 10 billion instructions per second.
	Formula: N^2 Instructions / 10^10 Instructions/Second
    Result: (10^7)^2 / 10^10 = 20,000 Seconds (5.5 Hours)

Merge Sort
	Time Complexity of O(N Log N).
	Sort 10 million numbers.
	Uses a slower computer with 10 million instructions per second. A performance decrease of 1000 times.
	Formula: N * Log N Instructions / 10^10 Instructions/Second
    Result: 10^7 * Log 10^7 / 10^10 = 1163 Seconds (20 Minutes)
 
Comparison
Merge Sort is significantly much faster, by hours, than Insertion Sort. Knowing which algorithm to use and when to use them is an important concept to know. Simple using a faster computer with better hardware will not always improve the runtime performance.
```



## Chapter Two

### Analyzing Algorithms

Predicting the resources required by the algorithm. For instance, finding the Time Complexity and Space Complexity of an algorithm.

***Input Size*** - Depends, for many problems the most natural measure is the number of items or bits for the input.

***Running Time*** - The number of primitive operations or "steps" take for an algorithm before terminating.

### Time Complexity

 When the input increases how does the performance of the algorithm change?

***Rate of Growth*** - An abstraction of the runtime formula for an algorithm (worst-case) which focuses solely on the high-order term and ignores (abstracts away) the lower order terms. A list of common high order terms from low to high order is below.

​		***Order of Growth***: C<sub>1</sub> < Log<sub>2</sub> N < sqrt(N) < N < N * Log<sub>2</sub> N < N^2^ < < N<sup>3</sup> < 2<sup>n</sup> < N!

***Worst Case*** - The longest running time of any input size known as the upper bound.

***Average Case*** - The average case is roughly as bad a the worst case, but occurs more often.

***Best Case*** - The shortest running time of any input size known as the lower bound.

### Loop Invariant

A property of a loop that is true before (and after) each iteration. This property is used to prove the correctness of the algorithm using mathematical induction. *Introduction to Algorithms* seems to have a slightly less strict mathematical induction proof which makes it easier to understand.

The structure below is a great way to prove the correctness of an algorithm in a less strict manner.

***Correctness of Loop Invariant***

​	***Initialization*** - The property of a loop is true prior to first iteration.

​	***Maintenance*** - If the property is true before an iteration of the loop, it remains true before the next iteration.

​	***Termination*** - When the loop terminates, the loop invariant gives us a useful property that helps show that the algorithm is correct.

### Divide and Conquer Algorithm Design

Many algorithms are recursive, therefore, the divide and conquer algorithm design breaks the problem down into several subproblems that are similar to the original problem but smaller in size, solves the subproblems recursively, and combines these solutions to create a solution to the original problem. We're basically "kicking the problem the down the road".

The structure below is a great way to describe the divide and conquer design of an algorithm.

***Divide*** - Divide the problem into a number of subproblems that are smaller instances of the <u>same</u> problem.

***Conquer*** - Conquer the subproblems by solving them recursively. If the subproblem sizes are small enough, however, just solve the subproblems in a <u>straightforward manner</u>.

***Combine*** - Combine the solutions to the subproblems to solve for the original problem.

#### Analysis of Divide and Conquer

The analysis of a divide and conquer algorithm design uses the concept of recurrence equations or recurrence to describe the running time on a problem of input size`n` in terms of the running time on smaller inputs.

==TODO:== NEED MORE MATHEMATICAL BACKGROUND ON RECURRENCE RELATIONS

### Insertion Sort Analysis

==TODO:== Focus on the analysis as I know the concept of how the algorithm works and can implement. Also, I like how the book shows us the breakdown of the analysis, including the contants.

### Merge Sort Analysis

==TODO:== Focus on the analysis. as I know the concept to how the algorithm works and can implement.
