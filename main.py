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

    def pop(self):
        if self.head == None:
            return print("List is Empty")
        else:
            if self.head.next == None:
                self.head = None
            else:
                temp = self.head
                while temp and temp.next.next != None:
                    temp = temp.next
                temp.next = None

    def deleteElement(self, data):
        if self.head == None:
            return print("List is Empty")
        else:
            if self.head.val == data:
                self.head = self.head.next
            else:
                temp = self.head
                while temp and temp.next and temp.next.val != data:
                    temp = temp.next
                if temp.next and temp.next.val != data:
                    temp.next = temp.next.next
                else:
                    print("Element Not Found")

    def size(self):
        if self.head == None:
            print(0)
        else:
            total = 0
            temp = self.head
            while temp:
                total += 1
                temp = temp.next
            print(total)


list = LinkedList()
list.printList()
list.append(10)
list.append(20)
list.append(30)
list.append(40)

list.deleteElement(50)

list.printList()
list.append(40)
list.pop()
list.size()
