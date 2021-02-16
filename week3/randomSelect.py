import random

def randomSelect(A, s, f, k):
    print(f'A[s:f+1]: {A[s:f+1]}')
    print(f's: {s} f: {f} k: {k}')
    if (s == f):
        if (k == 1):
            print(f'array size 1, return value: {A[s]}')
            return A[s]
        else:
            print("uh oh... something is wrong")
            return -1
    p = random.randrange(s, f)
    pv = A[p]
    print(f'p: {p} pv: {pv}')
    B=[0]*(f-s+2)
    i=1
    j=len(B)-1
    for ind in range(s,f+1):
        if A[ind] < pv:
            B[i] = A[ind]
            i = i + 1
        elif A[ind] > pv:
            B[j] = A[ind]
            j = j -1
    r = i
    B[r]=pv
    print(f'B: {B[1:]}')    
    if (r == k):
        print(f'found it, returning: {B[r]}')
        return(B[r])
    elif (k<r):
        print(f'recursing on left side')
        return randomSelect(B,1,r-1,k)
    else:
        print(f'recursing on right side')
        return randomSelect(B,r+1,len(B)-1,k-r)

A=list(range(21,37))
random.shuffle(A)
A.insert(0,0)
print('Unordered A: ', A)

k = random.randrange(1, 16)
print(f'k: {k}')

result = randomSelect(A,1,len(A)-1,k)
print(f'result: {result}')