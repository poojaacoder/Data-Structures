
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printAll(self):
        current = self.head
        if self.head == None:
            return 0
        else:
            while current:
                print(current.val)
                current = current.next

    def sizeAll(self):
        current = self.head
        size = 0
        if self.head == None:
            return
        while current != None:
            size+=1
            current = current.next
        print(size)
        return size
    
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head == None:
            return
        new_node.next = self.head
        self.head = new_node
        print("inserted node", data)

    def insertAtIndex(self, index, data):
        new_node = Node(data)
        current = self.head
        if self.head == None:
            return 0
        pos = 0
        if pos == index:
            self.insertAtBegin(data)
            return
        
        while current !=  None and pos+1 != index:
            pos +=1
            current= current.next

        if  current != None:
            new_node.next = current.next
            current.next = new_node
        else:
            print("Index not found")


    def insertAtEnd(self, data):
        new_node = Node(data)
        current = self.head
        if self.head == None:
            return
        while current != None:
            current = current.next
        
        current.next = new_node

    def removeFirst(self):
        if self.head == None:
            return 
        current = self.head
        self.head = current.next

        
    def removeEnd(self):
        if self.head == None:
            return 
        current = self.head
        while current.next != None :
            current = current.next
        
        current.next = None

    def removeAtIndex(self, index):
        if self.head == None:
            return
        current = self.head
        pos = 0
        if pos == index:
            self.removeFirst()
        while current != None and pos + 1== index:
            current = current.next
            pos +=1

        if current != None:
            current.next = current.next.next
        else:
            print("index not found")

    def remove_node_data(self,data):
        current = self.head
        if self.head == None:
            return 
        if current.val == data:
            self.removeFirst()
            return
        while current != None and current.next.val != data:
            current = current.next

        if current == None:
            return
        else:
            current.next = current.next.next



list1 = LinkedList()
list1.insertAtBegin('a')
list1.insertAtEnd('c')
list1.insertAtEnd('d')
list1.insertAtEnd('e')
list1.printAll()
list1.insertAtIndex(1, 'b')
list1.removeEnd()
list1.removeFirst()
list1.printAll()        







        









