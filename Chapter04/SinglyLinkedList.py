class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None

    
class SinglyLinkedList:
    def __init__ (self):
        self.head = None
        self.size = 0
        
    def append(self, data):
        # Encapsulate the data in a Node 
        node = Node(data)
        if self.head is None:
            self.head = node 
            self.size += 1
        else: 
            current = self.head 
            while current.next:
                current = current.next 
            current.next = node 
            self.size += 1
            
    def size(self):
        return self.size
            
            
words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

current = words.head
while current:
    print(current.data)
    current = current.next
    
print(f'The linked list has {words.size} items.')    
