class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp and temp.next != None:
                temp = temp.next
            temp.next = node


list = LinkedList()
list.printList()
list.append(10)
list.append(20)
list.append(30)
list.append(40)
list.printList()
