#============================================
# Nama : Zahra Cantikya Paragasthya
# NIM : J0403251106
# Kelas : A2
#============================================

#============================================
#Implementasi Dasar : Node pada Linked List
#============================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#1) Membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Mendefinisikan head dan menghubungkan Node : A-> B-> C-> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3) Traversal: Menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data) #Menampilkan data pada nose saat ini
    current = current.next #pindah ke node berikutnya 

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
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()