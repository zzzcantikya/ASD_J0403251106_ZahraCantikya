#=============================
# Bubble Sort Ascending
#=============================

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:   # kondisi ascending
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1


alist = [37,12,70,20,56,99,81,101,151,63]
shortBubbleSort(alist)
print(alist)

