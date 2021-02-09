def quicksort(l, indent=0):
    if (len(l) == 1):
        return l
    print(indent*"  ", end="")
    print("list: ", l)
    start = 0
    end = len(l)-1
    mid = (start + end) // 2
    #print("start, mid, end: ", start, mid, end)
    left = l[start:mid+1]
    right = l[mid+1:end+1]
    print(indent*"  ", end="")
    print("split: ", left, right)
    if (len(left) > 1):
        print(indent*"  ", end="")
        print("sorting left: ", left)
        quicksort(left, indent+1)
    if (len(right) > 1):
        print(indent*"  ", end="")
        print("sorting right: ", right)
        quicksort(right, indent+1)

    print(indent*"  ", end="")
    print("merging: ", left, right)
    lefti = righti = li = 0
    while (lefti < len(left) and righti < len(right)):
        if (left[lefti] <= right[righti]):
            l[li] = left[lefti]
            li = li + 1
            lefti = lefti + 1
        else: 
            l[li] = right[righti]
            li = li + 1
            righti = righti + 1
    
    while (lefti < len(left)):
        l[li] = left[lefti]
        li = li + 1
        lefti = lefti + 1
    while (righti < len(right)):
        l[li] = right[righti]
        li = li + 1
        righti = righti + 1
    print(indent*"  ", end="")
    print("sorted: ", l)

l = [5,8,1,6,4,9,2,7,3]
quicksort(l)
print(l)