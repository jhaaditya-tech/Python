'''Queue Creation for Level Order'''
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
    def __str__(self):
        return str(self.value)
    
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
        
    #Printing the queue
    def __str__(self):
        values=[str(x) for x in self.linkedList]
        return ' '.join(values)
    
    #Enqueue Method
    def enqueue(self,value):
        newNode=Node(value)
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
    
    
    #Dequeue Method
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
    
    #Peek Method
    def peek(self):
        if self.isEmpty():
            return False
        return self.linkedList.head
    
    #Delete method
    def delete(self):
        self.linkedList.head=None
        self.linkedList.tail=None
        
        
    
        
        
