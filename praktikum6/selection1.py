#=============================
# Selection Sort Ascending
#=============================

def selectionSort(data):
    for fillslot in range(len(data)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if data[location] > data[positionOfMax]:
                positionOfMax = location
        
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp


data = [45, 12, 78, 34, 23, 90, 11]
selectionSort(data)
print(data)