import statistics
import random
import math

class Node:
    def __init__(self, key_in):
        self.key = key_in
        self.left = None
        self.right = None
    
    def inorder(self):
        if (self.left != None):
            self.left.inorder()
        print(self.key, end=" ")
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


def MagicMedian(A, s, f):
    cut = A[s:f+1]
    medianValue = statistics.median_low(cut)
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

def BuildTree(tree, A, s, f, depth=0):
    t = " " * depth
    if (s > f):
        #print(f'{t}s: {s} > f: {f}, so returning')
        return None
    m = MagicMedian(A, s, f)
    #print(f'{t}Median index: {m} Median value: {A[m]}')
    #print(f'{t}Array before partition: {A}')
    swap(A, m, f)
    #print(f'{t}Array after moving median: {A}')
    mid = InPlacePartition(A, s, f)
    #print(f'{t}Array after partition: {A}')
    n = Node(A[mid])
    if (tree == None):
        tree = n
    else:
        tree.insert(n)
    #print(f'{t}Making recursive call with s: {s} f: {mid-1}')
    BuildTree(tree, A, s, mid-1, depth+1)
    #print(f'{t}Making recursive call with s: {mid+1} f: {f}')
    BuildTree(tree, A, mid+1, f, depth+1)
    return tree

n = 255
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
