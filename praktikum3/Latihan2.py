class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None #head : titik awal pada circular linked list

    def append(self, data):
        new_node = Node(data) 

        if self.head is None:  
            self.head = new_node
            new_node.next = self.head
            return
        
        #Mencari node terakhir
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        #Menyambung node terakhir dengan node baru
        temp.next = new_node
        new_node.next = self.head

    def search(self, key):
        if self.head is None: #Mengecek apakah list kosong
            print("Circular Linked List kosong. tidak ada elemen yang bisa dicari.")
            return
        
        temp = self.head
        #melakukan traversal hingga kembali ke head
        while True: 
            if temp.data == key: #jika elemen ditemukan
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return
            temp = temp.next
            if temp == self.head:
                break
        #jika elemen tidak ditemukan
        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.") 

if __name__ == "__main__":
    cll = CircularLinkedList()

    data_input = input("Masukkan elemen ke dalam Circular Linked List (pisahkan dengan koma): ")

    #Memasukkan elemen ke dalam list jika input kosong
    if data_input.strip() != "":
        data_list = data_input.split(",")
        for item in data_list:
            cll.append(int(item.strip()))

key = int(input("Masukkan elemen yang ingin dicari: "))

cll.search(key) #menjalankan fungsi pencarian





