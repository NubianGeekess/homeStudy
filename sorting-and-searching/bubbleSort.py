def bubble_sort(aList):
    for passnum in range(len(aList)-1, 0, -1):
        for i in range(passnum):
            if aList[i] > aList[i+1]:
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp

aList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(aList)
print aList