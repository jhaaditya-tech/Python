class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class CDLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    #Append Method
    def append(self, data):
        new_node=Node(data)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            new_node.prev=self.tail
            new_node.next=self.head
            self.head.prev=new_node
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        
    #Prepend method
    def prepend(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            new_node.next=self.head
            new_node.prev=self.tail
            self.tail.next=new_node
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        
    #Traverse CDLL
    def traverse(self):
        temp_node=self.head
        while temp_node:
            print(temp_node.data)
            temp_node=temp_node.next
            if temp_node==self.head:
                break
            
    #Reverse traverse method
    def rev_traverse(self):
        temp_node=self.tail
        while temp_node:
            print(temp_node.data)
            temp_node=temp_node.prev
            if temp_node==self.tail:
                break
            
    #Search method
    def search(self,key_value):
        current_node=self.head
        while current_node:
            if (current_node.data==key_value):
                return True
            current_node=current_node.next
            if current_node==self.head:
                break
        return False
                
    #Get method, optimized method
    def get(self, index):
        if index<0 or index>=self.length:
            return None
        if (index<self.length//2):
            temp_node=self.head
            for _ in range(index):
                temp_node=temp_node.next
        else:
            temp_node=self.tail
            for _ in range(self.length-1,index,-1):
                temp_node=temp_node.prev
        return temp_node
    
    #Set Method
    def set(self,index,data):
        temp_node=self.get(index)
        if temp_node:
            temp_node.data=data
            return True
        return False
    
    
    #Insert Method,
    def insert(self,index,data):
        if index<0 or index>self.length:
            return None
        if index==0:
            return self.prepend(data)
        elif index==self.length:
            return self.append(data)
        
        new_node=Node(data)
        temp_node=self.get(index-1)
        new_node.prev=temp_node
        new_node.next=temp_node.next
        temp_node.next.prev=new_node
        temp_node.next=new_node
        self.length+=1
        return new_node
    
    #Pop FirstMethod
    def pop_first(self):
        if self.length==0:
            return None
        popped_node=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            popped_node.prev=None
            popped_node.next=None
            self.tail.next=self.head
            self.head.prev=self.tail
        self.length-=1
        return popped_node
    
    #Pop Method
    def pop(self):
        if self.length==0:
            return None
        popped_node=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=self.head
            self.head.prev=self.tail
            popped_node.next=None
            popped_node.prev=None
        self.length-=1
        return popped_node
    
    #Remove method
    def remove(self, index):
        if index < 0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        elif index==self.length-1:
            return self.pop()
        removed_node=self.get(index)
        removed_node.prev.next=removed_node.next
        removed_node.next.prev=removed_node.prev
        removed_node.next=None
        removed_node.prev=None
        self.length-=1
        return removed_node
    
    #Delete method
    def delete(self):
        self.head=None
        self.tail=None
        self.length=0

    #__str__method
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node:
            result+=str(temp_node.data)
            temp_node=temp_node.next
            if temp_node==self.head:
                break
            result+=' <-> '
        return result
            
        
    
    

cdll=CDLinkedList()
cdll.append(5)
cdll.append(10)
cdll.append(15)
cdll.append(20)
cdll.append(25)
cdll.prepend(1)
print(cdll)
#cdll.traverse()
#cdll.rev_traverse()

cdll.set(2,60)
print(cdll)

print(cdll.insert(6,66))
print(cdll)

cdll.remove(0)
print(cdll)