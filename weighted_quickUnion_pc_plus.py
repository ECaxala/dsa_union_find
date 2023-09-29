# Weighted Quick-union Algorithm with path compression
# ! "Two pass" implementation: Adds second loop to findRoot() to set the id[] of each examined node to the root. 

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
        # We store the node were we looking for the root to keep it for the 2nd pass of id[] 
        root = i
        # Moving up the tree until rach root
        while root != self.id[root]:
            root = self.id[root]

        # Now we know root we set any node it along the path pointing to root to flaten the tree. 
        while i != root:
            nextNode = self.id[i]
            self.id[i] = root
            i = nextNode
        
    
        return root


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

    def test_root_shouldReturnIdOfLookedUpNodeEqualTwoRoot(self):
        quickUnion = QuickUnionUF(10)
        quickUnion.union(3, 4) # connects 3 and 4: 3-->4
        quickUnion.union(7, 5) # connects 7 and 5: 7-->5
        quickUnion.union(7, 4) # connects 7 and 4: 5-->4
        self.assertTrue(quickUnion.isConnected(7, 3))
        # Look up root of a given node
        root = quickUnion.findRoot(7)
        # Since we looked up root for given item, tree should be flatened and items id should point to root
        self.assertEqual(quickUnion.findRoot(7), root )

unittest.main()