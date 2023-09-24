# Quick find algorithm
# Caution: Algorithm with qaudratic time complexity. 
#          Does not scale with computer performance and is to slow for large number of complements. 

import unittest

class QuickFindUF:

    # Set tht Id of each object to itself (N list accesses)
    def __init__(self, N):
        self.idArray = []       #Create an empty List
        for index in range(N): 
            self.idArray.append(index)

    # Check if wethr p and q in the same component 
    def isConnected(self, p, q):
        return self.idArray[p] == self.idArray[q] 

   # Change all entries with idArray[p] to idArray[q]
    def union(self, p, q):
       pid = self.idArray[p]
       qid = self.idArray[q]
       
       for i in range(len(self.idArray)):
           if self.idArray[i] == pid: self.idArray[i] = qid 



# Unit test implementation 
class QuickFindTestCases(unittest.TestCase):
    def test_initialization_shouldInitializeCorrectly(self):
        quickFind = QuickFindUF(10)
        self.assertEqual(quickFind.idArray,list(range(10)))
        
    def test_isConnected_shouldReturnFalse(self):
        quickFind = QuickFindUF(10)
        self.assertFalse(quickFind.isConnected(3,4))
   
    def test_isConnected_shouldReturnTrue(self):
        quickFind = QuickFindUF(10)
        quickFind.union(3, 4)
        self.assertTrue(quickFind.isConnected(3,4))
        
    def test_isConnected_shouldReturnTrueOnEntity(self):
        quickFind = QuickFindUF(10)    
        quickFind.union(3, 4) # connect 3 and 4
        quickFind.union(4, 6) # connect 4 and 6
        self.assertTrue(quickFind.isConnected(3, 6))

unittest.main()