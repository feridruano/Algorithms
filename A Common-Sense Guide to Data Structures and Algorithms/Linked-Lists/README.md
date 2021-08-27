# Linked-Lists

A list **data structure** based on Nodes that hold information. Nodes are blocks of data spread throughout memory with a pointer to the next node. Linked-Lists are similar to arrays as both data structures hold a list of data, but how each data structure is stored in memory differs with pros and cons.

**TODO:** Clean this mess up.

## Reading

The first node in the list is O(1) while all other nodes are O(N).

### Pseudocode

- [ ] Given an index to read.
- [ ] Use a temporary variable that starts at the first node.
- [ ] Loop through the linked-list until the index.
  - [ ] Return the data of the node.
- [ ] Otherwise, the index does not exist.

## Searching

The first node in the list is O(1) while all other nodes are O(N).

### Pseudocode

- [ ] Given a value.
- [ ] Use a temporary variable that starts at the first node.
- [ ] Loop through the linked-list until the value is found.
  - [ ] Return the node itself.
- [ ] Otherwise, the value was not found in the linked-list.

## Insertion

It is O(1) for an insertion at the front.

### Pseudocode

- [ ] Given a value.
- [ ] Create a node with the value.
- [ ] Assign the new node to point to the first node.
- [ ] Reset the first node to the new node.

It is O(N) for an insertion elsewhere.

### Pseudocode

- [ ] Given a value.
- [ ] Create a new node with the value.
- [ ] Loop through the linked-list with a temporary variable until the last node.
  - [ ] Point the last node to new node.

## Deletion

### Pseudocode

- [ ] Given a value.
- [ ] Track a previous and current node.
- [ ] Search for the node using the previous and current node.
  - [ ] When the current node is the value being searched for, point the previous node to the current nodes next node.
  - [ ] Unlink the current node.
- [ ] Otherwise, no deletion.