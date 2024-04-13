#Circular Queue - Queue with fixed capaciy
"""
Use start and top pointer, when eqnueue move T and when dequeue you move start variable, ignoring first element, but the list will have fixed size
you will just be moving the pointer S and T in the fixed size list

Watch lecture for this

"""

class Queue:
    def __init__(self, maxSize):
        self.items=maxSize*[None]
        self.maxSize=maxSize
        self.start=-1
        self.top=-1
        
    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)
    
    #isFull Method, constant time
    def isFull(self):
        if self.top+1==self.start:
            return True
        elif self.start==0 and self.top+1==self.maxSize:
            return True
        return False
    
    #isEmpty Method, constant time
    def isEmpty(self):
        if self.top==-1:
            return True
        return False
    
    #Enqueue Method, constant time
    def enqueue(self, data):
        if self.isFull():
            return False
        else:
            if self.top+1==self.maxSize:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start=0
            self.items[self.top]=data
            return True        
                
    
    #dequeue method, constant time
    def dequeue(self):
        if self.isEmpty():
            return False
        firstElement=self.items[self.start]
        start=self.start
        if self.start==self.top:
            self.start=-1
            self.top=-1
        elif self.start+1==self.maxSize:
            self.start=0
        else:
            self.start+=1
        self.items[start]=None
        return firstElement
    
    #Peek Method, constant time
    def peek(self):
        if self.isEmpty():
            return False
        else:
            return self.items[self.start]
        
    #delete method, constant time
    def delete(self):
        self.items=self.maxSize*[None]
        self.top=-1
        self.start=-1
        
    




queue=Queue(3)
print(queue.isEmpty())
print(queue.isFull())
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
print(queue)
print(queue.isFull())



