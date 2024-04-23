import QueueHelper as queue

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        
newBT=TreeNode("N1")
leftChild=TreeNode("N2")
rightChild=TreeNode("N3")

newBT.leftChild=leftChild
newBT.rightChild=rightChild


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
#preOrderTraversal(newBT)

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
    
#postOrderTraversal(newBT)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        #Creating a custom queue
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            #Assuming dequeu returns the tree node directly
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)




def searchBT(rootNode,key_value):
    if not rootNode:
        return "The BT does not exit."
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            if key_value==root.value.data:
                return True
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            return False
                
            
def insertNodeBT(rootNode,newNode):
    if not rootNode:
        rootNode=newNode
        return 'Successfully Inserted'
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild=newNode
                return 'Successfully Inserted'
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild=newNode
                return 'Successfully Inserted'
                

newNode=TreeNode("N4")
insertNodeBT(newBT,newNode)
levelOrderTraversal(newBT)

#Deleting a node

#Get deepest Node
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        deepestNode=root.value
        return deepestNode

print(getDeepestNode(newBT).data)

#Deleting the deepest Node
def deleteDeepestNode(rootNode,dNode):
    if not rootNode:
        return
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            if root.value is dNode:
                root.value=None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild=None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild=None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

#Delete node BT method

def deleteNode(rootNode, node):
    if not rootNode:
        return "The BT doesn't exist"
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            if root.value.data==node:
                dNode=getDeepestNode(rootNode)
                root.value.data=dNode.data
                deleteDeepestNode(rootNode,dNode)
                return "Node Deleted"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return 'Failed Message'
                
                
            

deleteDeepestNode(newBT,getDeepestNode(newBT))
levelOrderTraversal(newBT)

#Delete entire binary tree
def deleteBT(rootNode):
    rootNode=None
    rootNode.leftChild=None
    rootNode.rightChild=None
    return 'The BT has been successfully deleted.'
    
    
