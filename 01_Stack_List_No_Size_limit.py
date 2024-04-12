#Stacks

"""
Stack is a data structute that stores items in Last in First Out Manner (LIFO)

Why stack?

example; back button in the browser

Operations - Create Stack, Push, Pop, Peek, isEmpty, isFull, deleteStack

"""

"""
Using List
Easy to implement
Speed problem when it grows

Using Linked List
Fast Performance
Implementation is not easy

"""

#Creating stack using List without size limit

class Stack:
    def __init__(self):
        self.list=[]
        
    
    #Printing Method    
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)
    
    #isEmpty Method
    def isEmpty(self):
        if self.list ==[]:
            return True
        return False
    
    #Push Method, Constant
    def push(self,data):
        self.list.append(data)
        return True
    
    #Pop Method, Constant
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.list.pop()
        
    
    #Peek Method, Constant time compleexity
    def peek(self):
        if self.isEmpty():
            return "Empty Stack"
        else:
            return self.list[len(self.list)-1]
        
    
    #Delete Stack
    def delete(self):
        self.list=None
        
    
    

customStack=Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.peek())

print(customStack)






