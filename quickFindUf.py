#Quick find algorithm

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

# Creat an class instance
quickFind = QuickFindUF(10)
print(quickFind.idArray)
# Should show connected false
print(quickFind.isConnected(3, 4))

quickFind.union(3, 4)
quickFind.union(3, 9)
# Should show connected true
print(quickFind.isConnected(3, 4))
print(quickFind.idArray)
# Should show connected true
print(quickFind.isConnected(3, 9))