class MinHeap:

    def __init__(self):
        self.heapArray = []
        self.nextValuePos = 0

    # insert value priority pair into list
    def insert(self, val, p):
        # use a tuple for pair
        t = (val, p)
        self.heapArray.insert(self.nextValuePos, t)
        if p < self.heapArray[self.parent(self.nextValuePos)][1]:
            self.percUp(self.nextValuePos, self.parent(self.nextValuePos))
        self.nextValuePos += 1

    # for getting parent and child indices
    def parent(self, index):
        return int((index-1)/2)

    def lChild(self, index):
        return 2*index+1

    def rChild(self, index):
        return 2*index+2

    # maintain heap structure to the root
    def percUp(self, index, pIndex):
        self.swap(index, pIndex)
        if self.heapArray[pIndex][1] < self.heapArray[self.parent(pIndex)][1]:
            self.percUp(pIndex, self.parent(pIndex))

    # swap elements at indices
    def swap(self, i, j):
        temp = self.heapArray[i]
        self.heapArray[i] = self.heapArray[j]
        self.heapArray[j] = temp

    # deletes the min and returns it
    def deleteMin(self):
        if self.nextValuePos > 0:
            min = self.heapArray[0]
            self.swap(0, self.nextValuePos-1)
            del self.heapArray[self.nextValuePos-1]
            # to maintain heap property
            self.heapify(0)
            self.nextValuePos -= 1
            return min[0]

    # to maintain heap structure
    def heapify(self, index):
        # while there is an element left to heapify
        if index < len(self.heapArray):
            parent = self.heapArray[index]
            leftChild = self.lChild(index)
            rightChild = self.rChild(index)
            # compare child indices
            # swap parent with lesser child
            if rightChild >= len(self.heapArray):
                if not leftChild >= len(self.heapArray):
                    self.swap(index,leftChild)
            elif self.heapArray[rightChild][1] < self.heapArray[leftChild][1]:
                if parent[1] > self.heapArray[rightChild][1]:
                    self.swap(index, rightChild)
                    self.heapify(rightChild)
            else:
                if parent[1] > self.heapArray[leftChild][1]:
                    self.swap(index, leftChild)
                    self.heapify(leftChild)

    # decreases the priority of an element
    def lowerPriority(self, data, newPriority):
             index = self.indexOf(data)
             if index != -1:
                 pri, val = self.heapArray[index]
                 self.heapArray[index] = (pri, newPriority)
                 if newPriority < self.heapArray[self.parent(index)][1]:
                     # percUp to maintain heap property
                     self.percUp(index, self.parent(index))

    # returns index of given value in heap array
    def indexOf(self, val):
        count = 0
        for x in self.heapArray:
            if x[0] == val:
                return count
            count += 1


    def __str__(self):
        sb = ""
        for e in self.heapArray:
            sb += str(e) + "\n"
        return sb
