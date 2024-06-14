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
from IPython.display import display, HTML

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

    def manipulate_data(self, target_data, new_data):
        current_node = self.head
        while current_node:
            if current_node.data == target_data:
                current_node.data = new_data
                current_node.hash = current_node.compute_hash()
                self.update_hashes(current_node.next)
                break
            current_node = current_node.next

    def update_hashes(self, node):
        while node:
            node.prev_hash = node.prev_hash if node.prev_hash == '' else node.prev_hash
            node.hash = node.compute_hash()
            node = node.next

    def visualize(self):
        current_node = self.head
        html = '<div style="font-family: monospace;">'
        while current_node:
            html += f'<div style="display: inline-block; border: 1px solid black; padding: 10px; margin: 5px;">'
            html += f'<p>Data: {current_node.data}</p>'
            html += f'<p>Hash: {current_node.hash[:8]}...</p>'
            html += f'<p>Prev Hash: {current_node.prev_hash[:8]}...</p>'
            html += '</div>'
            if current_node.next:
                html += '<div style="display: inline-block; vertical-align: top; padding: 10px;">&#8594;</div>'
            current_node = current_node.next
        html += '</div>'
        display(HTML(html))