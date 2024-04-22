#Creating Binary Heap:

class Heap:
    def __init__(self,size):
        self.customList=[None]*(size+1)
        self.heapSize=0
        self.maxSize=(size+1)
   
#Peek of Binary Heap, simply returns root Node, constant time and space
def peekBHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]
    

#Size of Binary Heap, constant time and space
def sizeBHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize
    
#Level order Traversal, linear time and space complexity
def levelOrderTraversalBHeap(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i])

#Inserting node in Binary Heap, index of a node you want to make adjustment, heapType is minimum or maximum, O(logN) time and space
def heapifyInsert(rootNode,index,heapType):
    parentIndex=int(index/2)
    if index<=1:
        return
    if heapType=="Min":
        if rootNode.customList[index]<rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index]=rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
        heapifyInsert(rootNode,parentIndex,heapType)
    elif heapType=="Max":
        if rootNode.customList[index]>rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index]=rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
        heapifyInsert(rootNode, parentIndex,heapType)
    
#O(logN) time and space complexity
def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize+1==rootNode.maxSize:
        return "Binary Heap is Full"
    rootNode.customList[rootNode.heapSize+1]=nodeValue
    rootNode.heapSize+=1
    heapifyInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been inserted."
        

#Extract a node in Binary Heap, O(logN) time and space complexity
def heapifyExtract(rootNode, index, heapType):
    leftIndex=index*2
    rightIndex=index*2+1
    swapChild=0
    if rootNode.heapSize<leftIndex:
        return
    elif rootNode.heapSize==leftIndex:
        if heapType=="Min":
            if rootNode.customList[index]>rootNode.customList[leftIndex]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customLits[leftIndex]=temp
            return
        else:
            if rootNode.customList[index]<rootNode.customList[leftIndex]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customLits[leftIndex]=temp
            return
    else:
        if heapType=="Min":
            if rootNode.customList[leftIndex]<rootNode.customList[rightIndex]:
               swapChild=leftIndex
            else:
               swapChild=rightIndex
            if rootNode.customList[index]>rootNode.customList[swapChild]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
        else:
            if rootNode.customList[leftIndex]>rootNode.customList[rightIndex]:
               swapChild=leftIndex
            else:
               swapChild=rightIndex
            if rootNode.customList[index]<rootNode.customList[swapChild]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
    heapifyExtract(rootNode,swapChild,heapType)
    
def extractNode(rootNode, heapType):
    if rootNode.heapSize==0:
        return
    else:
        extractNode=rootNode.customList[1]
        rootNode.customList[1]=rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize]=None
        rootNode.heapSize-=1
        heapifyExtract(rootNode,1,heapType)
        return extractNode
    
    
            
#Delete entire Binary Heap, constant time and space complexity
def deleteEntireBHeap(rootNode):
    rootNode.customList=None
    
                

newBinaryHeap=Heap(5)
insertNode(newBinaryHeap,4,"Min")
insertNode(newBinaryHeap,5,"Min")
insertNode(newBinaryHeap,2,"Min")
insertNode(newBinaryHeap,1,"Min")
levelOrderTraversalBHeap(newBinaryHeap)
extractNode(newBinaryHeap,"Min")
levelOrderTraversalBHeap(newBinaryHeap)

    