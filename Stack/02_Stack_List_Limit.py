#With size limit

class Stack:
    def __init__(self, maxSize):
        self.maxSize=maxSize
        self.list=[]
    
    #Print mehod
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)
    
    
    #isEmpty Method
    def isEmpty(self):
        if self.list==[]:
            return True
        return False
    
    #isFull Method
    def isFull(self):
        if len(self.list)==self.maxSize:
            return True
        return False
    
    #Push Method
    def push(self,data):
        if self.isFull():
            return False
        self.list.append(data)
        return True
    
    #Pop Method
    def pop(self):
        if self.list ==[]:
            return False
        return self.list.pop()
       
    
    #Peek method
    def peek(self):
        if self.list==[]:
            return False
        return self.list[len(self.list)-1]
    
    #Delete method
    def delete(self):
        self.list=None
    