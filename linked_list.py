from list_node import Node
class LinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        """
        Method that checks whether list is empty or not
        """
        return not self.head
    def clear(self):
        self.head = None
    def getSize(self):
        """
        Method to count the size of the list
        """
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next
        return size
    def append(self,data):
        """
        Method to append a new element to the end of the list
        """
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    def prepend(self,data):
        """
        Method to prepend a new element to the beginning of the list
        """
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def deleteNode(self,data):
        current = self.head
        if not self.is_empty():
            while current.next:
                if self.head.data == data:
                    self.head = self.head.next
                    break
                if current.next.data == data:
                    current.next = current.next.next
                    break
                current = current.next
    def printList(self):
        current = self.head
        while current:
            print(current.data,"--> ",end='')
            current = current.next
        print()

    def hasCycle(self, head):
        """
        Method to check whether list has a cycle or not.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    
    def removeElement(self , val):
        """
        Method to remove node with given data.
        """
        current = self.head
        if self.head.data == val:
            self.head.next = self.head.next.next
        while self.head and self.head.data == val:
            self.head = self.head.next
        while current.next:
            if current.next.data == val:
                current.next = current.next.next 
            else:
                current = current.next
        
ob=LinkedList()
ob.append(15)
ob.append(16)
ob.append(17)
print(ob.getSize())
ob.printList()
ob.prepend(123)
print(ob.getSize())
ob.printList()
ob.deleteNode(16)
ob.printList()
print(ob.getSize())
