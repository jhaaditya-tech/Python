"""
Creating Queue using Linked List

All have constant time and space complexity
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
    def __str__(self):
        return str(self.data)
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next
            

class Queue:
    def __init__(self):
        self.linkedList=LinkedList()
        
    
    #Printable queue
    def __str__(self):
        values=[str(x) for x in self.linkedList]
        return ' '.join(values)
    
    #Enqueue Method, Constant time
    def enqueue(self,data):
        newNode=Node(data)
        if self.linkedList.head is None:
            self.linkedList.head=newNode
            self.linkedList.tail=newNode
        else:
            self.linkedList.tail.next=newNode
            self.linkedList.tail=newNode
        return newNode
    
    #isEmpty Method
    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        return False
    
    #Dequeue Method, constant time
    def dequeue(self):
        if self.isEmpty():
            return False
        popped_node=self.linkedList.head
        if self.linkedList.head==self.linkedList.tail:
            self.linkedList.head=None
            self.linkedList.tail=None
            return popped_node
        self.linkedList.head=self.linkedList.head.next
        return popped_node
       
    
    #Peek method
    def peek(self):
        if self.isEmpty():
            return False
        return self.linkedList.head
    
    #Delete method
    def delete(self):
        self.linkedList.head=None
        self.linkedList.tail=None

queue=Queue()
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
queue.dequeue()
print(queue)


"""

List vs LinkedList Implementation

Using list, some operation will have linear time comlexity, but all the operation in the queue will have the constant time complexity

"""

'''
Queue Module

'''