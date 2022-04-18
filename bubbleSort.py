test = [3,4,23,16,13,19,10]

def bubbleSort(myList):
    for i in range(len(myList)):
        swapped = False
        for j in range(len(myList)-i-1):
            if myList[j] > myList[j+1]:
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1] = temp

                swapped = True

        if not swapped:
            break
    return myList
print(bubbleSort(test))