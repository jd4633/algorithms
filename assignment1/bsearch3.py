import random

def bsearch3(A,s,f,k):
    print("*********")
    print(f's: {s} f: {f}') 
    print(f'A[s]: {A[s]} A[f]: {A[f]}')
    if (s<f):
        d = (f-s) // 3
        q1=s+d
        q2=s+2*d
        print(f'q1: {q1} q2: {q2}')
        print(f'A[q1]: {A[q1]} A[q2]: {A[q2]}')
        if A[q1] == k or A[q2] == k:
            return True
        elif A[q1] > k:
            return bsearch3(A,s,q1-1,k)
        elif A[q2] > k:
            return bsearch3(A,q1+1,q2-1,k)
        else:
            return bsearch3(A,q2+1,f,k)
    elif A[s] == k:
        return True
    else:
        return False

max=100
A = []
for i in range(1,max,2):
    A.append(i)
#print("A: ",A)
k=random.randint(1, max)
#k=91
print(f'k: {k}')
found = bsearch3(A,0,len(A)-1,k)
print(f'was found: {found}')


