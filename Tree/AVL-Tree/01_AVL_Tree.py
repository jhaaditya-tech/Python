import QueueHelper as queue

class AVLNode:
    def __init__(self, data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        #To check if tree is balanced or not
        self.height=1

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
    
#Insert Node
#Helper function to calculate the height of left and right subtree
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalncedNode):
    newRoot=disbalncedNode.leftChild
    disbalncedNode.leftChild=disbalncedNode.leftChild.rightChild
    newRoot.rightChild=disbalncedNode
    disbalncedNode.height=1+max(getHeight(disbalncedNode.leftChild),getHeight(disbalncedNode.rightChild))
    newRoot.height=1+max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalancedNode):
    newRoot=disbalancedNode.rightChild
    disbalancedNode.rightChild=disbalancedNode.rightChild.leftChild
    newRoot.leftChild=disbalancedNode
    disbalancedNode.height=1+max(getHeight(disbalancedNode.leftChild),getHeight(disbalancedNode.rightChild))
    newRoot.height=1+max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot
    

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild)-getHeight(rootNode.rightChild)

def insertNode(rootNode,nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue<rootNode.data:
        rootNode.leftChild=insertNode(rootNode.leftChild,nodeValue)
    else:
        rootNode.rightChild=insertNode(rootNode.rightChild,nodeValue)
    rootNode.height=1+max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
    balance=getBalance(rootNode)
    if balance>1 and nodeValue <rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance>1 and nodeValue>rootNode.leftChild.data:
        rootNode.leftChild=leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance<-1 and nodeValue>rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance<-1 and nodeValue<rootNode.rightChild.data:
        rootNode.rightChild=rightRotate(rootNode.rightChild)
        leftRotate(rootNode)
    return rootNode

#Deleting a node from AVL
def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)
        
    
def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue<rootNode.data:
        rootNode.leftChild=deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue>rootNode.data:
        rootNode.rightChild=deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp=rootNode.rightChild
            rootNode=None
            return temp
        elif rootNode.rightChild is None:
            temp=rootNode.leftChild
            rootNode=None
            return temp
        temp=getMinValueNode(rootNode.rightChild)
        rootNode.data=temp.data
        rootNode.rightChild=deleteNode(rootNode.rightChild,temp.data)
        #Case2 Rotation required
    rootNode.height=1+max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
    balance=getBalance(rootNode)
    if balance>1 and getBalance(rootNode.leftChild)>=0:
        return rightRotate(rootNode)
    if balance<-1 and getBalance(rootNode.rightChild)<=0:
        return leftRotate(rootNode)
    if balance>1 and getBalance(rootNode.leftChild)<0:
        rootNode.leftChild=leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance<-1 and getBalance(rootNode.rightChild)>0:
        rootNode.rightChild=rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
        
    return rootNode
        
        
#Delete entire AVL tree
def deleteAVL(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None
    rootNode.height=0
        
    


    



newAVL=AVLNode(5)
newAVL=insertNode(newAVL,10)
newAVL=insertNode(newAVL,15)
newAVL=insertNode(newAVL,20)
newAVL=deleteNode(newAVL,15)
levelOrderTraversal(newAVL)
