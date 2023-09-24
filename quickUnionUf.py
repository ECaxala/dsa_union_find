# Quick-union Algorithm
# Caution: More efficient than quick-find but still N-array accesses needed.
# - Trees can get large
# - Find opertion is too expensive
import unittest

class QuickUnionUF:

    # Set tht Id of each object to itself (N list accesses)
    def __init__(self, N):
        self.id = []       #Create an empty List
        for index in range(N): 
            self.id.append(index)

    # Chase parent pointer until reach root
    # Cost: Depth of i array accesses
    def findRoot(self, i):
        # Moving up the tree until rach root
        while i != self.id[i]: i = self.id[i]
        return i

    # Cost: Depht of p and q array accesses
    def isConnected(self, p, q):
        return self.findRoot(p) == self.findRoot(q)

    def union(self, p, q):
        pRoot = self.findRoot(p)
        qRoot = self.findRoot(q)
        self.id[pRoot] = qRoot



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