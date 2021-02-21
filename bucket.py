import random

def generate_item():
    a = random.randrange(1, 11)
    b = random.randrange(1, 11)
    c = a / b
    #print(f'a: {a} b: {b} c: {c}')
    #print(a)
    return c

n = 100000
A = [0]*(n+1)
B = []
for i in range (0, n+1):
    B.append([])
#print("A", A)
#print("B", B)
for i in range (1, n+1):
    c = generate_item()
    bucketindex = round((c / 10) * n)
    #print(f'bucketindex: {bucketindex}')
    A[bucketindex] = A[bucketindex] + 1
    bucket = B[bucketindex]
    #print("bucket before inserting: ", bucket)
    bucket.append(c)
    #print("bucket after inserting: ", bucket)
    #print("B: ", B)

for i in range (0, n):
    bucket = B[i]
    bucket.sort()

for i in range (0, n):
    if (A[i] > 0):
        print(f'A[{i}]: {A[i]}')

print(B[10000])

#for i in range (0, n):
    #bucket = B[i]
    #print(f'B[{i}]: {B[i]}')
    #for j in bucket:
        #print(f'{j:2.4f}')
#print()