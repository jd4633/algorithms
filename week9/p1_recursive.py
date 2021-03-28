def get_rod_cuts(n, k=-1, depth=0):
    if (k==-1):
        k=n
    t = " " * depth
    print(f'{t}Getting list of cuts. Rod length: {n} Max cut: {k}')
    if (n==1):
        print(f'{t}Rod length is 1, returning [[1]]')
        return [[1]]
    if (n==0):
        print(f'{t}Rod length is 0, returning [[]]')
        return [[]]
    if (k>n):
        print(f'{t}Max cut is longer than rod length, setting max cut down to {n}')
        k=n
    cut_list = []
    for i in range (k, 0, -1):
        print(f'{t}Making first cut of size {i}')
        if (i == n):
            print(f'{t}Cut uses whole rod. Adding item: {[k]}')
            cut_list.append([i])
            continue
        # Make a first cut of size k. Remaining length is n-k. All cuts must be smaller or equal to k.
        print(f'{t}Making recursive call to get sub list')
        sub_list = get_rod_cuts(n-i, min(i, n-1), depth+1)            
        print(f'{t}Sub list: {sub_list}')
        for j in sub_list:
            j.insert(0, i)
            cut_list.append(j)
            print(f'{t}Adding: {j}')
    print(f'{t}Cut list: {cut_list}')
    print(f'{t}Size of cut list: {len(cut_list)}')
    return cut_list

get_rod_cuts(10)