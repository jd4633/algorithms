import numpy

def createSolutionSet (A, i, k, n):
    if (k==0):
        return [[]]
    if (i==n):
        return ([[A[i]]])
    if (n-i-k+1<=0):
        # just add all the remaining options
        soln_set = []
        sub_soln_set = createSolutionSet(A, i+1, k-1, n)
        for sub_soln in sub_soln_set:
            sub_soln.insert(0, A[i])
            soln_set.append(sub_soln)
        return soln_set
    else:
        soln_set = []
        # First add solutions where i is used
        sub_soln_set = createSolutionSet(A, i+1, k-1, n)
        for sub_soln in sub_soln_set:
            sub_soln.insert(0, A[i])
            soln_set.append(sub_soln)
        # Then add all solutions where i is not used
        soln_set = soln_set + createSolutionSet(A, i+1, k, n)
        return soln_set       

def calculateTotal(A,solution):
    total = 0
    for i in range (0, len(A)):
        # find closest well
        closestWell = -1
        for j in range (0, len(solution)):
            if (solution[j] >= A[i]):
                if ((closestWell == -1) or (solution[j] < closestWell)):
                    closestWell = solution[j]
        if (closestWell == -1):
            return -1
        distance = closestWell - A[i]
        total = total + distance
    return total

def findMinWells(A,k):
    solutionSet = createSolutionSet (A, 0, k, len(A)-1)
    bestTotal = -1
    bestSolution = None
    for solution in solutionSet:
        total = calculateTotal(A, solution)
        #print(f'{total}: {solution}')
        if ((total >= 0) and ((bestTotal == -1) or (total < bestTotal))):
            bestTotal = total
            bestSolution = solution
    #print("best solution: ", bestSolution)
    #print("best total: ", bestTotal)
    return bestTotal

def findMinDynamic(A,n,k):
    maxIndex = len(A)-1 
    wellTableList = []
    for numWells in range(0,k):
        wellTable = numpy.zeros((maxIndex+1, maxIndex+1), numpy.int8)
        for j in range(maxIndex, -1, -1):
            for i in range(j, -1, -1):
                if j == maxIndex:
                    wellTable[i][j]=0
                elif (numWells == 0):
                    wellTable[i][j]=((A[j+1]-A[j])*(i+1) + wellTable[i+1][j+1])
                else:
                    dontAddWell = ((A[j+1]-A[j])*(i+1) + wellTable[i+1][j+1])
                    addWell = wellTableList[numWells-1][0][j+1]
                    wellTable[i][j]=min(dontAddWell, addWell)
        print(f'table for numWells = {numWells}')
        print(wellTable)
        wellTableList.append(wellTable)
    return wellTableList[k-1][0][0]

#A = [2, 6, 7, 10, 13, 16]
A = [2, 6, 7, 10, 13]
k = 3
answer = findMinDynamic(A,100,k)
print (f'answer: {answer}')
print (f'alternate calculation: {findMinWells(A,k)}')
