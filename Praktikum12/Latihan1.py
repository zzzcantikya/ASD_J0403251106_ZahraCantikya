# Nama  : Zahra Cantikya Paragasthya
# NIM   : j0403251106
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ========================================================== 
# Latihan 1: Weighted Graph dan Perhitungan Jalur 
# ========================================================== 
# Representasi weighted graph menggunakan dictionary bersarang 
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
} 

jalur_1 = graph['A']['B'] + graph['B']['D']   # A -> B -> D 
jalur_2 = graph['A']['C'] + graph['C']['D']   # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2) 

if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D")

# Jawaban Analisis: 
# 1. Berapa total bobot jalur A -> B -> D? 
# total bobot jalur A -> B -> D adalah 9, dengan A ke B itu 4 dan B ke D itu 5
# 2. Berapa total bobot jalur A -> C -> D?
# total bobot jalur A -> C -> D adalah 3, dengan A ke C itu 2 dan C ke D itu 1
# 3. Jalur mana yang dipilih sebagai jalur terpendek? 
# Jalur terpendek adalah A -> C -> D yaitu 3 
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
# Karena dalam weighted graph, yang menentukan “terpendek” itu bukan jumlah edgenya, tapi
# total bobot (cost) dari jalur tersebut. Jalur dengan edge lebih sedikit bisa memiliki 
# bobot besar sehingga totalnya lebih tinggi, sedangkan jalur dengan lebih banyak edge bisa 
# lebih pendek jika bobot tiap edge kecil.