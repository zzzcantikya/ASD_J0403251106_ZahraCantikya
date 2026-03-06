#=============================
# Insertion Sort Ascending
#=============================

def insertionSort(data):
    for index in range(1, len(data)):
        currentvalue = data[index]
        position = index

        while position > 0 and data[position-1] > currentvalue:
            data[position] = data[position-1]
            position = position - 1

        data[position] = currentvalue


data = [45, 12, 78, 34, 23, 90, 11]
insertionSort(data)
print(data)