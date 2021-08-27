# Hash Tables

A **data structure** for storing or retrieving a value using a key. The process involves encoding a key, usually a string, to store or retrieve a value in a specific memory location. Hash Tables are also known as Dictionaries, Maps, Hashes, Hash Maps, and Associative Arrays.

**Note:** Hash Tables are commonly implemented using arrays.

## Hash Function

The process of converting characters into numbers, usually an array index which is used to store or retrieve the value associated with the characters, the key. 

**Note:** Most popular programming languages offer hash tables with hash functions already implemented.

## Collisions

During the process of converting a key into a number, the hash function can reproduce the same number for different keys. Ultimately, leading to a collision where two keys need to store their respective values in the same memory location or index in an array.

## Collision Resolution

To resolve a collision, one method is to add a sub-array inside the array index where a collision occurred. The sub-array contains all the keys and values that the hash function produced the same array index. 

## Efficient Hash Tables

A hash table's efficiency depends on three factors.

- How much data we're storing in the hash table.
- How many cells are available in the hash table.
- Which hash function we're using.

A good hash table strikes a balance of avoiding collisions while not consuming lots of memory. To accomplish this, computer scientists have developed the following rule of thumb: for every 7 data elements stored in a hash table, it should have 10 cells.

So, if you’re planning on storing 14 elements, you’d want to have 20 available cells, and so on.

This ratio of data to cells is called the **load factor**. Using this terminology, we’d say that the ideal load factor is 0.7 (7 elements / 10 cells)

When you begin to add more data, though, the computer will expand the hash table by adding more cells and changing the hash function so that the new data will be distributed evenly across the new cells.

## Time Complexity

For reading and writing the average time complexity is considered to be `O(1)`, constant time. However, this is misleading as not all keys are encoded with the same number of steps. It depends on the key length and the implementation of the hash function.