#stack using Linked List, everything is constant time

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        
    #Print method,  This line yields the current node (curNode) to the caller. This means that the iterator will produce the current node each time it's called.
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next

#Creating stack using Linked List
class Stack:
    def __init__(self):
        self.LinkedList=LinkedList()
        
    #Printing the Stack
    def __str__(self):
        values=[str(x.data) for x in self.LinkedList]
        return '\n'.join(values)
        
    #In Stack, you are inserting node at the begining of the Linked List
    
    #isEmpty Method, constant time complexity
    def isEmpty(self):
        if not self.LinkedList.head:
            return True
        return False
    
    #Push method
    def push(self,data):
        new_stack_node=Node(data)
        if self.isEmpty():
            self.LinkedList.head=new_stack_node
        else:
            new_stack_node.next=self.LinkedList.head
            self.LinkedList.head=new_stack_node
            
    #Pop method
    def pop(self):
        if self.isEmpty():
            return False
        else:
            node_value=self.LinkedList.head.data
            self.LinkedList.head=self.LinkedList.head.next
            return node_value
        
    #Peek method
    def peek(self):
        if self.isEmpty():
            return False
        else:
            node_value=self.LinkedList.head.data
            return node_value
        
        
        
    
    #Delete method
    def delete(self):
        self.LinkedList.head=None
        

customStack=Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.pop()
customStack.pop()
print(customStack.pop())
print(customStack.pop())
print(customStack)

"""
When to use/avoid Stack?

use - LIFO functionality
The chance of data corruption is minimum

Avoid:
Random access is not possible, only last element accessible




"""