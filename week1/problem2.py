def operation1(l, startIndex, endIndex):
    min_index=startIndex
    for i in range(startIndex+1, endIndex+1):
        if l[i] > l[min_index]:
            min_index = i
    return min_index

def operation2(l, startIndex, endIndex):
    i = startIndex
    j = endIndex
    while (i < j):
        temp = l[i]
        l[i] = l[j]
        l[j] = temp
        i = i + 1
        j = j - 1

def sort(l):
    i = 0
    endIndex = len(l) - 1
    print(l)
    while (i < endIndex):
        j = operation1(l, i, endIndex)
        if (i != j):
            operation2(l, i, j)
        print(l)
        i = i + 1

l = [5,8,1,6,4,9,2,7,3]
sort(l)