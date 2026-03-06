#=============================
# Shell Sort Descending
#=============================

def shellSort(data):
    sublistcount = len(data)//2
    
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(data, startposition, sublistcount)
        
        print("After increments of size", sublistcount, "The list is", data)
        sublistcount = sublistcount // 2


def gapInsertionSort(data, start, gap):
    for i in range(start+gap, len(data), gap):
        currentvalue = data[i]
        position = i

        while position >= gap and data[position-gap] < currentvalue:
            data[position] = data[position-gap]
            position = position-gap

        data[position] = currentvalue


data = [68, 23, 45, 12, 89, 34, 67, 10]
shellSort(data)
print(data)