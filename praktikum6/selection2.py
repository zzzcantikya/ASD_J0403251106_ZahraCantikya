#=============================
# Selection Sort Descending
#=============================

def selectionSort(data):
    for fillslot in range(len(data)-1,0,-1):
        positionOfMin = 0
        for location in range(1,fillslot+1):
            if data[location] < data[positionOfMin]:
                positionOfMin = location
        
        temp = data[fillslot]
        data[fillslot] = data[positionOfMin]
        data[positionOfMin] = temp


data = [45, 12, 78, 34, 23, 90, 11]
selectionSort(data)
print(data)