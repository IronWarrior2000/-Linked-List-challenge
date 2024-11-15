#Bill Nguyen | 11/11/24 | Assignment 4

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList():
    # Empty constructor 
    def __init__(self):
        # Define the list's basic properties "size", "head" and "tail"
        # Default them to 0 and None respectively
        self.size = 0
        self.head = None
        self.tail = None
    
    '''
    REQUIRED METHODS TO PASS LAB
    '''
    def count(self):
        # Return the size of the list
        return self.size
    
    def add(self, value):
        # Add the given value to the end of the list
        # If the list is empty make the value first
        # Return this list
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return self
    
    def get(self, index):
        # Return the value at the given index
        # If index is out of range raise an IndexError with message "Index is out of range"
        if index < 0 or index >- self.size:
            return "Index Error"
        current = self.head
        for _ in range(index):
            current = current.next
        return current
        
    def get_node(self, index):
        # Return the node from the given index
        # If index is out of range raise an IndexError with message "Index is out of range"
        # Bonus points if optimized to be better than O(N) in worst case
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current
            
    def remove(self, index):
        # Remove the given index
        # Be sure to maintain the integrity of the list
        # If index is out of range or list is empty raise an IndexError with message "Index is out of range"
        # Return this list
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of range")
        
        if index == 0:
            removed_node = self.head
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            # Removing any node other than the head
            prev_node = self.get_node(index - 1)
            removed_node = prev_node.next
            prev_node.next = removed_node.next
            if removed_node == self.tail:
                self.tail = prev_node

        self.size -= 1
        return self
    
    def reverse(self):
        # Reverse the elements in this list
        # Be sure to maintain the integrity of the list
        # Return this list 
        prev = None
        current = current.head
        self.tail = self.head
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev
        return self
    
    def copy(self, list):
        # Copy the given list to this list
        # Return this list
        current = list.head
        while current:
            self.add(current.value)
            current = current.next
        return self
    
    def copy_range(self, list, begin, end):
        # Copy the given list to this list using the range from begin to end exclusive
        # Return this list
        if begin < 0 or end > list.count() or begin >= end:
            raise IndexError("Invalid range")
        current = list.get_node(begin)
        for _ in range(begin, end):
            self.add(current.value)
            current = current.next
        return self
    
    def empty(self):
        # Return true or false if the list is empty
        return self.size == 0

    def first(self):
        # Return the first value in the list
        # If list is empty return None
        if self.head:
            return self.head.value
        return None
    
    def last(self):
        # Return the last value in the list
        # If list is empty return None
        if self.tail:
            return self.tail.value
        return None
    

