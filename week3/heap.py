import random

def swap(A, i, j):
    # print(f'swap A i: {i} j: {j}')
    tmp=A[j]
    A[j] = A[i]
    A[i] = tmp

def bubbleDown(A, i):
    while (i*2 < len(A)):
        if (i*2 + 1 < len(A)):
            if (A[i] >= A[i*2] and A[i] >= A[i*2+1]):
                break
            elif (A[i*2] > A[i*2+1]):
                swap(A, i, i*2)
                i=i*2
            else:
                swap(A, i, i*2+1)
                i=i*2+1
        else:
            if (A[i] >= A[i*2]):
                break
            else:
                swap(A,i,i*2)
                i=i*2

def bubbleUp(A, i):
    while (i > 1):
        j = i // 2
        if A[i] < A[j]:
            break
        swap(A,i,j)
        i=j


A=list(range(1,17))
random.shuffle(A)
A.insert(0,0)
print('Unordered A: ', A)

'''
# Heapify A using bubbleDown
i=len(A)-1
for j in range(i, 0, -1):
    bubbleDown(A,j)
    print(f'j: {j:2d} A: {A}')
print('A as heap: ', A)

i=len(A)-1
for j in range(i, 0, -1):
    swap(A, 1, j)
    j = A.pop()
    print(f'{j}', end=" ")
    bubbleDown(A,1)
'''

# Incrementally create heap B
B=[0]
for i in range(1, len(A)):
    B.append(A[i])
    bubbleUp(B,i)
    print('B: ', B)

i=len(B)-1
for j in range(i, 0, -1):
    swap(B, 1, j)
    k = B.pop()
    print(f'{k}', end=" ")
    bubbleDown(B,1)