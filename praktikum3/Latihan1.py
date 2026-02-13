class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete_node(self, key):
        temp = self.head

        # jika node yang dihapus adalah head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # jika data tidak ditemukan
        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# ===== Contoh Penggunaan =====
ll = LinkedList()
ll.insert_at_end(7)
ll.insert_at_end(14)
ll.insert_at_end(21)
ll.insert_at_end(28)

print("Sebelum dihapus:")
ll.display()

ll.delete_node(21)

print("Setelah dihapus:")
ll.display()
