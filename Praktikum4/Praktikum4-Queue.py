#============================================
# Nama : Zahra Cantikya Paragasthya
# NIM : J0403251106
# Kelas : A2
#============================================

#============================================
#Implementasi Dasar : Queue
#============================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

class queue: 
    # konstruktor untuk inisialisasi queue dengan front dan rear
    def __init__ (self):
        self.front = None # node paling depan 
        self.rear = None #Node paling belakang

    def is_empty(self):
        return self.front is None
    
    #membuat fungsi untuk menambahkan data baru pada bagian paling belakang
    def enqueue(self,data):
        nodeBaru= Node(data)

        #jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #jika queue tidak kosong, maka letakkan data baru ke setelah rear, dan jadikan data baru  sebagai rear
        self.rear.next = nodeBaru #Letakkan data baru pada setelahnya rear
        self.rear = nodeBaru #jadikan data baru sebagai rear

    def dequeue(self):
        #menghapus data dari depan
        data_terhapus = self.front.data #lihat data paling depan

        #geser front ke node berikutnya
        self.front = self.front.next

        #Jika setelah geser front menjadi none, maka queue kosong
        #rear juga harus jadi None
        if self.front is None:
            self.rear = None

        return data_terhapus

    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end="-> ")
            current = current.next
        print("Rear")


q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()