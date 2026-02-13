class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        if not self.head:
            print("kosong")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # menggabungkan dua singly linked list
    def merge(self, other):
        merged = SinglyLinkedList()

        temp = self.head
        while temp:
            merged.append(temp.data)
            temp = temp.next

        temp = other.head
        while temp:
            merged.append(temp.data)
            temp = temp.next

        return merged


# Contoh Penggunaan
ll1 = SinglyLinkedList()
ll2 = SinglyLinkedList()

data1 = input("Masukkan elemen untuk Linked List 1: ")
if data1.strip():
    for x in data1.split(","):
        ll1.append(int(x.strip()))

data2 = input("Masukkan elemen untuk Linked List 2: ")
if data2.strip():
    for x in data2.split(","):
        ll2.append(int(x.strip()))

print("Linked List 1:")
ll1.display()

print("Linked List 2:")
ll2.display()

hasil = ll1.merge(ll2)

print("Linked List setelah digabungkan:")
hasil.display()
