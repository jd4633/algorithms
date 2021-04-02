import statistics
import random
import math

class Node:
    def __init__(self, key_in):
        self.key = key_in
        self.sum = key_in
        self.left = None
        self.right = None
    
    def inorder(self):
        if (self.left != None):
            self.left.inorder()
        print(f'{self.key}/{self.sum}', end=" ")
        if (self.right != None):
            self.right.inorder()
    
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

    def printTree(self):
        depth = self.depth()
        for i in range(0, depth+1):
            self.printLevel(i)
            print()
    
    def printLevel(self, level):
        if (level == 0):
            print(self.key, end=" ")
            return
        if (self.left == None):
            #print(f'level: {level}', end="")
            dashCount = 2 ** (level - 1)
            #print(f'dashCount: {dashCount}', end="")
            print("- " * dashCount, end="")
        else:
            self.left.printLevel(level-1)
        if (self.right == None):
            #print(f'level: {level}', end="")
            dashCount = 2 ** (level - 1)
            print("- " * dashCount, end="")
        else:
            self.right.printLevel(level-1)
        
    
    def insert(self, n):
        self.sum = self.sum + n.key
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

def TotalLess(t, x):
    if (t == None):
        return 0
    if (x.key < t.key):
        return TotalLess(t.left, x)
    total = 0
    if (t.left != None):
        total = total + t.left.sum
    total = total + t.key
    total = total + TotalLess(t.right, x)
    return total

n = 15
A = list(range(1,n+1))
random.shuffle(A)
print(f'A: {A}')
bst = BuildTree(None, A, 0, n-1)
print(f'BST: ', end="")
bst.inorder()
print()
depth = bst.depth()
print(f'depth of BST: {depth}')
bst.printTree()

# L = [9, 11, 13, 15]
# for i in L:
#     print(f'Deleting: {i}')
#     bst.deleteLeaf(i)

print(f'BST: ', end="")
bst.inorder()
print()
depth = bst.depth()
print(f'depth of BST: {depth}')
#bst.printTree()

for i in range (1, 16):
    print(f'{i}: {TotalLess(bst, Node(i))}')

