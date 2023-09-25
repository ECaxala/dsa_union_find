# Weighted Quick-union Algorithm with path compression
# ! Simpler "One pass" implementation: Make every other node in path point to its grandparent !

# + Modify quick-union to avoid tall trees. 
# + Keep track of size of each tree (number of objects)
# + Balance by linking root of smaller tree to root of larger tree
import unittest

class QuickUnionUF:

    # Set tht Id of each object to itself (N list accesses)
    def __init__(self, N):
        self.id = []       #Create an empty List
        for index in range(N): 
            self.id.append(index)
        self.treeSize = [1] * N     # Keeps track of the size of every tree

    # Chase parent pointer until reach root
    # Cost: Depth of i array accesses
    def findRoot(self, i):
        # Moving up the tree until rach root
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]] 
            i = self.id[i]
        return i

    # Cost: Depht of p and q array accesses
    def isConnected(self, p, q):
        return self.findRoot(p) == self.findRoot(q)

    def union(self, p, q):
        pRoot = self.findRoot(p)
        qRoot = self.findRoot(q)
        # Link root of smaller tree to root of larger tree
        if self.treeSize[pRoot] < self.treeSize[qRoot]: 
            self.id[pRoot] = qRoot
            self.treeSize[qRoot] += self.treeSize[pRoot]
        else: 
            self.id[qRoot] = pRoot
            self.treeSize[pRoot] += self.treeSize[qRoot]



# Unit test implementation 
class QuickFindTestCases(unittest.TestCase):
    def test_initialization_shouldInitializeCorrectly(self):
        quickUnion = QuickUnionUF(10)
        self.assertEqual(quickUnion.id,list(range(10)))
        
    def test_root_shouldReturnRoot(self):
        quickUnion = QuickUnionUF(10)
        self.assertEqual(quickUnion.findRoot(3), 3)

    def test_isConnected_shouldReturnFalse(self):
        quickUnion = QuickUnionUF(10)
        self.assertFalse(quickUnion.isConnected(3, 4))
        
    def test_idConnected_shouldReturnTrue(self):
        quickUnion = QuickUnionUF(10)
        quickUnion.union(3, 4) # connects 3 and 4
        self.assertTrue(quickUnion.isConnected(3, 4))

    def test_idConnected_shouldReturnTrueInComplement(self):
        quickUnion = QuickUnionUF(10)
        quickUnion.union(3, 4) # connects 3 and 4: 3-->4
        quickUnion.union(7, 5) # connects 7 and 5: 7-->5
        quickUnion.union(7, 4) # connects 7 and 4: 5-->4
        self.assertTrue(quickUnion.isConnected(7, 3))

unittest.main()