# Recursion

A method of solving a computational problem by solving smaller instances of the same problem. Literally, a function calling itself on smaller instances until all of those smaller instances have been solved, thereby, solving the problem.

Recursion is extremely useful for problems with an unknown number of loops or layers or levels deep.



## Base Case

All recursive functions require **at least** **one** base case to stop the recursion at the desired solution. It's common to have multiple base cases.



## Reading Recursive Code

A good method of reading recursive code is as follows:

1. Identify the base case.
2. Walk through the function for the base case.
3. Identify the "next-to-last" case. This is the case just before the base case.
4. Walk through the function for the "next-to-last" case.
5. Repeat "next-to-last" case process.



## The Call Stack

Stacks provide a useful method of data processing, notably, Last-in First-Out (LIFO) operations. For this reason, recursive function calls use a stack (The Call Stack) to store the most recent instance of the call. This instance must run and complete before any previous instance.

### Stack Overflow

The Call Stack uses at most as much memory as there is available on the computer. A significant number of recursions will eventually exceed the available memory and present errors. Infinite recursion requires infinite memory, but infinite memory is not possible.



## Extra Parameters

Recursive functions can have additional parameters to keep track of variables which constantly change each recursive call. An example is passing the index as a extra parameter or a low and high parameter.



## Recursive Patterns

### Repeatedly Execute

The simplest form of recursive patterns. The recursion repeatedly executes a task. The last line of code in the function is usually a simple, single call to the recursive function. An example is a recursive implementation of a countdown from 10 to 0.

### Calculations

Performing a calculation based on a subproblem. The subproblem is a version of the very same problem applied to a smaller input. An example is the recursive implementation of factorial where the recursive call is the subproblem of the calculation.

```python
return number * factorial(number - 1)
```

#### Bottom-Up

To approach a calculation by starting at the beginning and recursing to the end, equivalent to using a loop. However, you must know the ordering in which the final solution has to be built to go from one state to next recursively correctly. How many steps do we increase by each recursive call (loop) and what is the limit at which the calculation stops. For complex calculations, knowing these two properties of a calculation may not be obvious or challenging to discover as we have to think about the entire problem as a whole.

**Note:** The bottom-up approach is the same strategy for making a calculation whether using a loop or recursion.

#### Top-Down

A new mental strategy to approach a problem through its subproblems. Top-down often starts from the end and works backwards to try to figure out the ways of getting to the end (final solution).

Mentally, the problem is kicked down the road as shown in the Array Sum example.

##### Thought Process

The thought process is vague, but more understandable with more experience of top-down recursion. A goal of understanding to reach.

1. Imagine the function you're writing has already been implemented by someone else.
2. Identify the subproblem of the problem. Try the next-to-smallest version of the problem at hand.
3. See what happens when you call the function on the subproblem and go from there.

**Note:** Recursion is the only way to achieve a top-down strategy.

#### Top-Down Examples

##### Array Sum

A top-down approach to the sum of `[1, 2, 3, 4, 5]`. We know the sum is 15 by adding each value together, left to right.

1. Imagine the recursive function is implemented.
2. Focus on the subproblem. In this case, `1` plus the **sum of everything to the right** (subproblem).
   1. So, `1 + SUM([2, 3, 4, 5])`
   2. How can continue to "kick the subproblem down the road" in actual code?
      1. The idea of `1 + 2 + SUM([3, 4, 5])` in the next recursive call.
      2.  `array[0] + SUM([1, array.length -1 ])`
   3. We now have identified the subproblem and found how to implement "kicking of the subproblem down the road".
3. What happens when the recursive function is called on the last subproblem, an array of length 1? Base case.
   1.  E.g `1 + 2 + 3 + 4 + SUM([5])`
   2. It returns the one element.

##### Count Xs

A top-down approach to counting the number of Xs in string. This is a perfect example to demonstrate that we can have slightly different recursive calls and nested checks for a base case.

1. Imagine the recursive function is implemented.

2. Focus on the subproblem. In this case, counting the number of Xs in `xbx` by check the first character of each substring.

   1. Add 1 if our first character is an X, then recursively check the remaining substring to the right and count the Xs.

      1. ```python
         if string[0] == "x":
         	return 1 + count(string[1, len(string)])
         ```

   2. Otherwise, do not add 1 and recursively check the remaining characters to the right to count the remaining Xs.

      1. ```python
         else:
         	return count(string[1, len(string)])
         ```

3. What happens when one of the recursive functions is called on the last subproblem, a string of length 1? Base case.

   1. Add one if the character is a X, otherwise add zero. Either value stops the recursion while maintaining the correct count.

      1. ```python
         if len(string) = 1:
         	if string[0] == "x":
         		return 1
         	else:
         		return 0 # As there are no more Xs or substings(subproblems) to check.
         ```

##### Staircase Problem

A top-down approach to solving a famous and complex problem. 

> How many different paths are there to the top of N steps when a person can climb one, two, or three steps at a time?

Without a recursive mindset, we would count the number of paths one by one for each N, which can be difficult to wrap our minds around the algorithm to determine the total paths for any N steps.

So, let's focus on the subproblem.

1. For an N-step staircase, there are at least `N-1` paths to the top when a person climbs one step at a time before the last step.
   1. `paths(N-1)` before taking the last step to the top. We're kicking the problem down the road by calculating the number of paths up to the previous step when a person always climbs one step at a time.
2. However, for an N-step staircase, a person can also climb two or three steps at a time. This means a person can reach the top step from two or three steps before. Therefore, the number of paths to each of those steps must be known as well.
   1. `paths(N-2) + paths(N-3)`
3. Therefore, the number of paths to reach the top of an N-step staircase is `paths(N-1) + paths(N-2) + paths(N-3)`.

Now, let's focus on the base case.

1. When the recursive subproblem reaches either 1, 2, or 3, the base case must return the correct number of steps for each value. However, the base case is tricky because`paths(N-1) + paths(N-2) + paths(N-3)` can reach negative steps `paths(1) + paths(0) + paths(-1)` which cannot possible. Therefore, we must return 0 steps for any subproblem that returns a negative number

   1. ```python
      if N <= 0:
      	return 0
      if N == 1 || N == 2:
      	return N
      if N == 3:
      	return 4 # Total steps for an 4-step staircase
      ```



## Dynamic Programming

Recursion is an elegant technique to solve complex and tricky problems, but recursion often introduces the worst time complexity when compared to other iterative approaches. In most cases, the time complexity ends up being `O(2^N)`.

Dynamic Programming is the optimization of recursive algorithms to reduce redundant recursive calls. This optimization is fairly easy to make and drastically improves the time complexity back to `O(N)`, `O(N * Log N)`, etc. Below are three simple techniques for optimizing recursive algorithms.

### Save the Recursive Call Result to a Variable

Quick implementations of recursive algorithms often lead to redundant recursive calls to retrieve the result of the same input. Optimize the call by only calling it once and storing the result in a variable to be reused as illustrated by the code below.

```python
# Unoptimized
def max(array):
	if len(array) == 1:
		return array[0]
	if array[0] > max([1, len(array)]): # 1 Recursive Call
		return array[0]
	else:
		return max([1, len(array)]) # 2 Recursive Call - Same Input, Same Result

# Optimized
def max(array):
	if len(array) == 1:
		return array[0]
   	max_result = max([1, len(array)]) # Only 1 Recursive Call, Result Stored to Variable for Reuse
	if array[0] > max_result:
		return array[0]
	else:
		return max_result
```

### Memoization - Overlapping Subproblems (Redundant Calls)

Memoization is the programming process of storing ("**memo**rizing") previous recursive calls and their result in a hash table to reduce redundant recursive calls. The hash table are passed as an extra parameter making the hash table available to all recursive call instances. In doing so, we remove the unnecessary calls to overlapping subproblems.

For instance, the unoptimized recursive Fibonacci algorithm makes redundant calls to each `nth` term due to `fib(n-2)+fib(n-1)` . Therefore, for each `nth` term it is recommended to store the result in a hash table to eliminate future redundant calls.

```python
def fibonacci(n, memo):
	if n == 0 or n == 1:
		return 1
	if not memo.get(n): # Check if fib(n) was called previously
		memo[n] = fib(n-2, memo) + fib(n-1, memo) # Save the call, to reuse the result later
	return memo[n]
```

### Bottom-Up or Iterative Approach

The last technique is to use the bottom-up approach to recursion which reduces the number of redundant recursive calls. Bottom-up is the same as reimplementing the iterative approach recursively. It's recommended to use the iterative approach whenever possible and only use recursion for complex or tricky problems.

```python
def fib(n):
	if n == 0:
		return 1
	a = 0
	b = 1
	for i in range(1, n):
		temp = a
		a = b
		b = temp + a
	return b
```





