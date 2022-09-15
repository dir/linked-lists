from dataclasses import dataclass

# Doubly Linked List Implementation
# by Luke Davis


@dataclass
class Node:
    data: object
    next: 'Node' = None  # Forward reference to Node class
    prev: 'Node' = None

    # Get node data
    def value(self) -> object:
        return self.data

    def __repr__(self) -> object:
        return str(self.data)


@dataclass
class DoublyLinkedList:
    head: Node = None
    tail: Node = None

    # Add an item to the list
    def add(self, data: object) -> None:
        newData = Node(data)

        # If there is no head, we can infer that this is the first node being inserted.
        if not self.head:
            # Set head and tail to first node.
            newData.prev = None
            self.head = newData
            self.tail = self.head
            return

        newData.prev = self.tail
        self.tail.next = newData
        self.tail = self.tail.next

    # Delete an item from the list
    def delete(self, node: Node) -> None:
        if not self.head:
            return

        current_node = self.head

        # Traverse the list until we find a match.
        while current_node != node:
            if not current_node.next:
                return

            current_node = current_node.next

        if current_node.prev:
            current_node.prev.next = current_node.next
        else:
            self.head = current_node.next

        if current_node.next:
            current_node.next.prev = current_node.prev

    # Find an item in the list.
    def find(self, data: object) -> Node:
        if not self.head:
            return None

        current_node = self.head

        while current_node.data != data:
            if current_node == self.tail:
                return None

            current_node = current_node.next

        return current_node

    # Return all values in the list, as a Python list type.
    def values(self) -> list:
        data = []

        if not self.head:
            return data

        node = self.head

        while node.next:
            data.append(node.data)
            node = node.next

        data.append(node.data)

        return data
