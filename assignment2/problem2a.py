import statistics
import math

class Node:
    def __init__(self, key_in):
        self.key = key_in
        self.left = None
        self.right = None
    
    def insert(self, n):
        if (n.key < self.key):
            if self.left == None:
                self.left = n
            else:
                self.left.insert(n)
        else:
            if self.right == None:
                self.right = n
            else:
                self.right.insert(n)

    def deleteLeaf(self, n):
        if (n < self.key):
            if (self.left.key == n):
                self.left = None
            else:
                self.left.deleteLeaf(n)
        else:
            if self.right.key == n:
                self.right = None
            else:
                self.right.deleteLeaf(n)

    def depth(self):
        depth = 0
        if (self.left == None):
            leftDepth = -1
        else:
            leftDepth = self.left.depth()
        if (self.right == None):
            rightDepth = -1
        else:
            rightDepth = self.right.depth() 
        depth = max(leftDepth, rightDepth) + 1
        return depth                

def MagicMedian(A, s, f):
    cut = A[s:f+1]
    medianValue = statistics.median_high(cut)
    return A.index(medianValue, s, f+1)

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def InPlacePartition(A, s, n):
    slide = s-1
    for j in range(s, n):
        if A[j] < A[n]:
            slide = slide + 1
            swap(A, j, slide)
    swap(A, slide+1, n)
    return slide+1

def BuildTree(tree, A, s, f):
    if (s > f):
        return tree
    m = MagicMedian(A, s, f)
    swap(A, m, f)
    mid = InPlacePartition(A, s, f)
    n = Node(A[mid])
    if (tree == None):
        tree = n
    else:
        tree.insert(n)
    BuildTree(tree, A, s, mid-1)
    BuildTree(tree, A, mid+1, f)
    return tree

def FullHeight(n):
    if (n.right == None):
        return 0
    return 1+FullHeight(n.right)

def convertToRBT(n, h):
    if (h>=0):
        print(f'Coloring {n.key} as black')
        n.color = "BLACK"
    else:
        print(f'Coloring {n.key} as red')
        n.color = "RED"
    if n.left != None:
        convertToRBT(n.left, h-1)
    else:
        # insert NIL node
        pass
    if n.right != None:    
        convertToRBT(n.right, h-1)
    else:
        # insert NIL node
        pass

n = 15
A = list(range(1,n+1))
print(f'A: {A}')
bst = BuildTree(None, A, 0, n-1)

L = [9, 11, 13, 15]
for i in L:
    print(f'Deleting: {i}')
    bst.deleteLeaf(i)

depth = bst.depth()
print(f'depth of BST: {depth}')
print(f'FullHeight of BST: {FullHeight(bst)}')

convertToRBT(bst, FullHeight(bst))