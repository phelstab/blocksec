class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


import hashlib

class HashNode:
    def __init__(self, data, prev_hash=''):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.compute_hash()
        self.next = None

    def compute_hash(self):
        return hashlib.sha256((self.data + self.prev_hash).encode()).hexdigest()

class HashLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = HashNode(data)
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            new_node = HashNode(data, last_node.hash)
            last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(f"Data: {current_node.data}, Hash: {current_node.hash}, Prev Hash: {current_node.prev_hash}")
            current_node = current_node.next