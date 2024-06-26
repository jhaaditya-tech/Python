import QueueHelper as queue

class BSTNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

#Inserting Node Method, logarithmic time complexity (O(logN))
def insertNode(rootNode, nodeValue):
    if rootNode.data ==None:
        rootNode.data=nodeValue
    elif nodeValue<=rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild=BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild=BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "Success"

#Traversing BST
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
    
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
    
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        

#Search Method
def searchNode(rootNode, keyValue):
    if rootNode is None:
        return False
    if rootNode.data==keyValue:
        return True
    if keyValue<rootNode.data:
        return searchNode(rootNode.leftChild,keyValue)
    else:
        return searchNode(rootNode.rightChild,keyValue)
    
    
#Delete Node Method

#Find minimum value node method
def minValueNode(bstNode):
    current=bstNode
    while current.leftChild is not None:
        current=current.leftChild
    return current

#Delete node method
def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue<rootNode.data:
        rootNode.leftChild=deleteNode(rootNode.leftChild,nodeValue)
    elif nodeValue>rootNode.data:
        rootNode.rightChild=deleteNode(rootNode.rightChild,nodeValue)
    else:
        #Only one Child
        if rootNode.leftChild is None:
            temp=rootNode.rightChild
            rootNode=None
            return temp
        if rootNode.rightChild is None:
            temp=rootNode.leftChild
            rootNode=None
            return temp
        #Two Children
        temp=minValueNode(rootNode.rightChild)
        rootNode.data=temp.data
        rootNode.rightChild=deleteNode(rootNode.rightChild, temp.data)
    return rootNode


#Delete entire BST Method
def deleteBST(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None
       


newBST=BSTNode(None)
print(insertNode(newBST,70))
print(insertNode(newBST,60))
print(insertNode(newBST,80))
print(insertNode(newBST,90))
deleteNode(newBST,80)
deleteBST(newBST)
levelOrderTraversal(newBST)
