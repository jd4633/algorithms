def MyRecurse(A,s,f):
    if s < f:
        q2 = (s + f) // 2
        q1 = (s + q2) // 2
        MyRecurse(A,s,q1)
        MyRecurse(A,q2+1,f)
        if q1 < q2:
            for i in range(q1+1, q2+1):
                #print(A[i], end=" ")
                print(f'{A[i]:05b}')
    else:
        #print(A[s], end=" ")
        print(f'{A[s]:05b}')

#A=[1,2,3,4]
# prints: 1, 3, 4, 2
#A=[1,2,3,4,5,6,7,8]
# 1, 2, 5, 7, 8, 6, 3, 4
A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# prints: 1, 3, 4, 2, 9, 10, 13, 15, 16, 14, 11, 12, 5, 6, 7, 8
MyRecurse(A,0,len(A)-1)
print()

""" 
MyRecurse(A,s,f):
    if s < f
        q2 = b(s + f )/2c
        q1 = b(s + q2)/2c
        MyRecurse(A,s,q1)
        MyRecurse(A,q2+1,f)
        if q1 < q2
            for i = q1 + 1 to q2
                Print A [i]
    else Print A [s] 
"""