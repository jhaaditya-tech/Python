"""
Queue

can be created using the Python list as well as Linked List

Operations includes Create Queue, Enqueue(), Dequeue(), peek(), delete(), isEmpty(), isFull

Queue is a data structure that stores items in First-In/First-Out manner. (similar to queue in store)

Uselful for utilizing first coming data first, while other waits their turns (FIFO method)

First application is POS in restaurant, Printer Queue, Call Center Application

"""

class Queue:
    def __init__(self):
        self.items=[]
        
    #Str method, printing queue
    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)
    
    #isEmpty Method
    def isEmpty(self):
        if self.items==[]:
            return True
        return False
    
    #Enqueue Method, linear timer
    def enqueue(self,data):
        self.items.append(data)
        return True

    #Dequeue method, Linear time complexity
    def dequeue(self):
        if self.isEmpty():
            return False
        else:
            return self.items.pop(0) #To remove the first element
        
    #Peek Method, constant time
    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.items[0]
        
    #Delete method, constant time
    def delete(self):
        self.items=None
    
queue=Queue()
print(queue.isEmpty())

queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
print(queue)
queue.dequeue()
print(queue)