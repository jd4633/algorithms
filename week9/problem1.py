n = 10
r = []
s = []
for i in range(0, n+1):
    r.append([]) # create a new row in the count table
    s.append([]) # create a new row in the solution table
    for j in range (0, n+1):
        #print(f'calculating r[{i}][{j}]')
        r[i].append(0)
        s[i].append([])
        if (i == 0 or j==0):
            r[i][j] = 1
            s[i][j] = [ [] ]
        elif (j>i):
            # Max cut is bigger than the rod, so solutions are the same for a smaller max cut
            r[i][j] = r[i][j-1]
            s[i][j] = s[i][j-1].copy()
        else:
            for k in range(j, 0, -1):
                # Make first cut of size k.
                #print(f'Making a cut of size {k}')
                #print(f'Remaining rod size: {i-k}')
                #print(f'Solutions for rod size {i-k} with max cut {k} : {s[i-k][k]}')
                # Determine ways of cutting the rest of the rod, using cuts of size k or smaller
                r[i][j] = r[i][j] + r[i-k][k]
                for l in s[i-k][k]:
                    print (f'inserting {k} into {l}')
                    new_cut = l.copy()
                    new_cut.insert(0, k)
                    print (f'new cut: {new_cut}')
                    s[i][j].append(new_cut)
        print(f'r[{i}][{j}]: {r[i][j]}')
        print(f's[{i}][{j}]: {s[i][j]}')

