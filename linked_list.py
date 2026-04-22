class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

   
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def recursive_sum(self):
        return self._sum_helper(self.head)

    def _sum_helper(self, node):
        if node is None:
            return 0
        return node.data + self._sum_helper(node.next)

   
    def recursive_search(self, target):
        return self._search_helper(self.head, target)

    def _search_helper(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        return self._search_helper(node.next, target)

    
    def recursive_reverse(self):
        self.head = self._reverse_helper(self.head, None)

    def _reverse_helper(self, current, prev):
        if current is None:
            return prev

        next_node = current.next
        current.next = prev

        return self._reverse_helper(next_node, current)

    def display(self):
        current = self.head
        output = []

        while current:
            output.append(str(current.data))
            current = current.next

        output.append("None")
        print(" -> ".join(output))