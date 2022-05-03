class Node(object):
    def __init__(self, data, next_node = None,
                 prev_node = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def append(self, data):
        '''add element at last'''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def insert(self, data):
        '''add element at first'''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self):
        current_node = self.head
        output = []
        while current_node:
            output.append(current_node.data)
            current_node = current_node.next
        print(*output)

    def remove(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            if current_node.next is None:
                current_node = None
                self.head = None
                return
            else:
                next_node = current_node.next
                next_node.prev = None
                current_node = None
                self.head = next_node
                return

        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None:
            return

        if current_node.next is None:
            prev = current_node.prev
            prev.next = None
            current_node = None
            return
        else:
            next_node = current_node.next
            prev_node = current_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None
            return

    def delete_first(self):
        current_node = self.head
        if current_node is None:
            return
        if current_node.next is None:
            self.head = None
            return
        self.head = current_node.next
        self.head.prev = None

        
    def delete_last(self):
        current_node = self.head
        if current_node is None:
            return
        if current_node.next is None:
            self.head = None
            return
        while current_node.next:
            current_node = current_node.next
        current_node.prev.next = None

n = int(input())
l = DoublyLinkedList()

for i in range(n):
    command = list(input().split())
    if command[0] == 'insert':
        l.insert(int(command[1]))
    elif command[0] == 'delete':
        l.remove(int(command[1]))
    elif command[0] == 'deleteFirst':
        l.delete_first()
    elif command[0] == 'deleteLast':
        l.delete_last()
        
l.print()

