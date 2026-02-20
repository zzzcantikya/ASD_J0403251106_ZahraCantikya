#============================================
# Nama : Zahra Cantikya Paragasthya
# NIM : J0403251106
# Kelas : A2
#============================================

#============================================
#Implementasi Dasar : Stack
#============================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#Stack ada operasi push (memasukkan head baru) dan pop(menghapus head)

class stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)
        
    def push(self,data): #memasukkan data baru pada stack
        #1 membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class node

        #2 node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        #3 geser top pindah ke node baru
        self.top = nodeBaru
    
    def is_empty(self):
         return self.top is None #stack kosong jika top = None
    
    def pop(self):
            # 1. Periksa apakah stack kosong
            if self.is_empty:
                    print("Stack kosong, tidak ada yang bisa di-pop.")
                    return None
            data_terhapus = self.top.data # simpan data yang akan dihapus
            self.top = self.top.next # geser top ke node berikutnya (node setelah top yang lama)
            return data_terhapus # kembalikan data yang dihapus
    
    def peek(self):
         #melihat data yang paling atas tanpa menghapus
         if self.is_empty():
            return None
         return self.top.data

    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print ("Top ->" , end=" " )
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

#Instantiasi Class Stack
s = stack()
s.push('A ')
s.push('B ')
s.push('C ')
s.tampilkan()
print('peek (lihat top):', s.peek())
s.pop() 
s.tampilkan()
print('peek (lihat top):', s.peek())

