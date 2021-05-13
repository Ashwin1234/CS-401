import sys
 
class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap=[[1 * sys.maxsize for x in range(3)] for i in range(maxsize)]
        #self.Heap = [-1 * sys.maxsize, -1 * sys.maxsize, -1 * sys.maxsize]*(self.maxsize + 1)
        self.Heap[0] = [-1 * sys.maxsize, -1 * sys.maxsize, -1 * sys.maxsize]
        self.FRONT = 1
 
    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos//2
 
    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos
 
    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1
 
    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        if pos > (self.size//2) and pos <= self.size:
            return True
        return False
 
    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def isempty(self):
        return len(self.Heap)==0
 
    # Function to heapify the node at pos
    def minHeapify(self, pos):
 
        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos][0] > self.Heap[self.leftChild(pos)][0] and
               self.Heap[pos][0] > self.Heap[self.rightChild(pos)][0]):
                
                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.leftChild(pos)][0] < self.Heap[self.rightChild(pos)][0]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
 
                # Swap with the right child and heapify
                # the right child
                elif self.Heap[self.leftChild(pos)][0] > self.Heap[self.rightChild(pos)][0]:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
                

                else:
                    if self.Heap[self.leftChild(pos)][1] < self.Heap[self.rightChild(pos)][1]:
                        self.swap(pos, self.leftChild(pos))
                        self.minHeapify(self.leftChild(pos))
                    else:
                        self.swap(pos, self.rightChild(pos))
                        self.minHeapify(self.rightChild(pos))

            
            elif (self.Heap[pos][0] > self.Heap[self.leftChild(pos)][0] or
               self.Heap[pos][0] > self.Heap[self.rightChild(pos)][0]):

                           
 
                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.leftChild(pos)][0] < self.Heap[self.rightChild(pos)][0]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
 
                # Swap with the right child and heapify
                # the right child
                elif self.Heap[self.leftChild(pos)][0] > self.Heap[self.rightChild(pos)][0]:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
                
                
            
            elif (self.Heap[pos][0] == self.Heap[self.leftChild(pos)][0] or 
               self.Heap[pos][0] == self.Heap[self.rightChild(pos)][0]):
 
                # Swap with the left child and heapify
                # the left child
                if self.Heap[pos][1] > self.Heap[self.leftChild(pos)][1] or self.Heap[pos][1] > self.Heap[self.rightChild(pos)][1]:
                 
                    if self.Heap[self.leftChild(pos)][1] < self.Heap[self.rightChild(pos)][1]:
                        if self.Heap[0] == self.Heap[self.leftChild(pos)][0]:
                            self.swap(pos, self.leftChild(pos))
                            self.minHeapify(self.leftChild(pos))
 
                # Swap with the right child and heapify
                # the right child
                    else:
                        if self.Heap[0] == self.Heap[self.rightChild(pos)][0]:
                            self.swap(pos, self.rightChild(pos))
                            self.minHeapify(self.rightChild(pos))
            
            
 
    # Function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize :
            return
        self.size+= 1
        self.Heap[self.size] = element
 
        current = self.size
        
        

        while self.Heap[current][0] <= self.Heap[self.parent(current)][0]:
            if self.Heap[current][0] == self.Heap[self.parent(current)][0]:
                
                if self.Heap[current][1] < self.Heap[self.parent(current)][1]:
                   
                    self.swap(current,self.parent(current))
                    current=self.parent(current)
                else:
                    break
            else:
                self.swap(current, self.parent(current))
                current = self.parent(current)
        
 
    # Function to print the contents of the heap
    def Print(self):
        for i in range(1, (self.size//2)):
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1]))
 
    # Function to build the min heap using
    # the minHeapify function
    def minHeap(self):
 
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)
 
    # Function to remove and return the minimum
    # element from the heap
    def remove(self):
 
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.minHeapify(self.FRONT)
        return popped
 
# Driver Code
if __name__ == "__main__":
    minheap.insert([0,0,0])
    minheap.insert([2, 4, 1])
    minheap.insert([4, 2, 4])
    minheap.insert([5, 6, 2])
    minheap.insert([4, 5, 3])
    minheap.insert([3, 9, 4])
    minheap.insert([6, 5, 5])
    minheap.Print()
    print(minheap.Heap)
    print(minheap.remove())
    minheap.Print()
    print(minheap.Heap)
    print(minheap.remove())
    minheap.Print()
    print(minheap.Heap)
    print(minheap.remove())
    minheap.Print()
    print(minheap.Heap)
    print(minheap.remove())
    
    minheap.Print()
    print(minheap.Heap)
    print(minheap.remove())
    
    minheap.Print()

    print(minheap.Heap)
    print(minheap.remove())
    print(minheap.Heap)
    print(minheap.remove())
    print(minheap.Heap)
    print(minheap.remove())
    