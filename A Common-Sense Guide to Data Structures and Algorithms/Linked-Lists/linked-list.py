class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def read(self, index):
        position = 0
        current_node = self.head

        while current_node:
            if position == index:
                return current_node.data
            else:
                position += 1
                current_node = current_node.next

        return None

    def search(self, data):
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next

        return None

    def insert(self, index, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            position = 0
            previous_node = None
            current_node = self.head

            while position < index and current_node is not None:
                previous_node = current_node
                current_node = current_node.next
                position += 1

            new_node.next = current_node
            previous_node.next = new_node

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, node, data):
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    def insert_end(self, data):
        new_node = Node(data)
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def delete(self, data):
        return None


if __name__ == '__main__':
    singly_linked_list = LinkedList()
