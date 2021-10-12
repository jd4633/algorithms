def findMinWaterStops(w):
    n = len(w)-1
    H = [0] * (n+1)
    H[n] = 0
    for i in range(n-1, -1, -1):
        if (i + w[i] >= n):
            H[i] = 0
        else:
            minAdditionalWaterStops = H[i+1]
            for j in range (2, min(w[i], n)+1):          
                if H[i+j] < minAdditionalWaterStops:
                    minAdditionalWaterStops = H[i+j]
            H[i] = minAdditionalWaterStops + 1
    return H[0]
    
w = [2, 2, 2, 2, 2, 2]
m = findMinWaterStops(w)
print(f'answer: {m}')
