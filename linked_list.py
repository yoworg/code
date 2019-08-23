class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        
    
class LinkedList():
    def __init__(self):
        self.head = None
    
    def append(self, val):
        if not self.head:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
    
    def print(self):
        list = []
        curr = self.head
        while curr:
            list.append(curr.val)
            curr = curr.next
        print(list)
    
    
    
lst = LinkedList()

lst.append(5)
lst.append(4)
lst.append(10)

lst.print()
