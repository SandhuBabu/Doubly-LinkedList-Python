import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly:
    head = None
    tail = None

    @staticmethod
    def error_meassage():
        print("List is empty....")

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node = self.head
            self.tail = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, pos, data):
        if self.head is None:
            print("Can't insert " + str(data) + " after " + str(pos) + ", ", end='')
            self.error_meassage()
            return
        temp = self.head
        while temp is not None and temp.data is not pos:
            temp = temp.next
        new_node = Node(data)
        if temp is self.tail and temp.data is self.tail.data:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return
        if temp is not None and temp.data is pos:
            new_node.next = temp.next
            temp.next.prev = new_node
            new_node.prev = temp
            temp.next = new_node
        else:
            print(str(pos) + " must be in list...")

    def delete_front(self):
        if self.head is None:
            print("Can't Perform Delete, ", end='')
            self.error_meassage()
            return
        print(str(self.head.data) + " deleted...")
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("Can't Perform Delete, ", end='')
            self.error_meassage()
            return
        if self.tail == self.head:
            print(str(self.head.data) + " deleted...")
            self.head = None
            self.tail = None
            return
        print(str(self.tail.data) + " deleted...")
        self.tail = self.tail.prev
        self.tail.next = None

    def delete_data(self, data):
        if self.head is None:
            print("Can't Delete " + str(data) + ", ", end='')
            self.error_meassage()
            return
        if self.head.data == data:
            print(str(self.head.data) + " deleted...")
            self.head = self.head.next
            return
        if self.tail.data == data:
            print(str(self.tail.data) + " deleted...")
            self.tail = self.tail.prev
            self.tail.next = None
            return
        temp = self.head
        while temp is not None and temp.data is not data:
            temp = temp.next
        if temp is None:
            print(str(data) + " must be in list...")
            return
        if temp.data == data:
            print(str(temp.data) + " deleted...")
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

    def display(self):
        if self.head is None:
            self.error_meassage()
            return
        temp = self.head
        print("List : ", end='')
        while temp is not None:
            print(str(temp.data) + " ", end='')
            temp = temp.next
        print()

    def reverse_display(self):
        if self.head is None:
            self.error_meassage()
            return
        temp = self.tail
        print("Reversed List : ", end='')
        while temp is not None:
            print(str(temp.data) + " ", end='')
            temp = temp.prev
        print()


doubly = Doubly()

q = """
1. Insert End
2. Insert Begin
3. Insert After A Data
4. Delete From Front
5. Delete From End
6. Delete Known Data
7. Display
8. Display In Reverse Order
9. Quit
"""

while True:
    print(q)
    ans = int(input("Enter Choice : "))
    if ans == 1:
        data = int(input("Enter Data : "))
        doubly.insert_end(data)
    elif ans == 2:
        data = int(input("Enter Data : "))
        doubly.insert_begin(data)
    elif ans == 3:
        pos = int(input("Insert After Which Data : "))
        data = int(input("Enter Data : "))
        doubly.insert_after(pos, data)
    elif ans == 4:
        doubly.delete_front()
    elif ans == 5:
        doubly.delete_end()
    elif ans == 6:
        doubly.delete_data(int(input("Enter Data To Delete : ")))
    elif ans == 7:
        doubly.display()
    elif ans == 8:
        doubly.reverse_display()
    elif ans == 9:
        sys.exit()
    else:
        print("Invalid Option, Please Choose A Right Option")
