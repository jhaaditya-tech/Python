class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    #Append Method
    def append(self,data):
        new_node=Node(data)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
    
        
    #Prepend Method
    def prepend(self,data):
        new_node=Node(data)
        if not self.head:
           self.head=new_node
           self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        
    #Traverse Method
    def traverse(self):
        current_node=self.head
        while current_node:
            print(current_node.data)
            current_node=current_node.next
            
    #Reverse Traverse Method
    def reverse_traverse(self):
        current_node=self.tail
        while current_node:
            print(current_node.data)
            current_node=current_node.prev
            
    #Search Method
    def search(self,key_value):
        current_node=self.head
        while current_node:
            if current_node.data==key_value:
                return True
            current_node=current_node.next
        return False
        
    #Get Method, optimized way, Linear time complexity but less itteration,  reduced number of operations
    def get(self, index):
        if index<0 or index>=self.length:
            return None
        if index<self.length//2:
            current_node=self.head
            for _ in range(index):
                current_node=current_node.next
        else:
            current_node=self.tail
            for _ in range(self.length-1,index,-1):
                current_node=current_node.prev   
        return current_node
        
    
    #Set Method
    def set(self, index,data):
        if index<0 or index>=self.length:
            return None
        current_node=self.get(index)
        if current_node:
            current_node.data=data
            return True
        return False
    
    #Insert Method
    def insert(self,index,data):
        if index<0 or index>=self.length:
            return None
        if index==0:
            self.prepend(data)
            return
        elif index==self.length:
            self.append(data)
            return
        else:
            new_node=Node(data)
            temp_node=self.get(index-1)
            new_node.next=temp_node.next
            new_node.prev=temp_node
            temp_node.next.prev=new_node
            temp_node.next=new_node
        self.length+=1
        
    
    #Pop First Method
    def pop_first(self):
        if not self.head:
            return None
        popped_node=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
            popped_node.next=None
        self.length-=1
        return popped_node.data
    
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
            self.tail.next=None
            popped_node.prev=None
        self.length-=1
        return popped_node.data
    
    #Remove method
    def remove(self, index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        elif index==self.length-1:
            return self.pop()
        else:
            popped_node=self.get(index)
            popped_node.prev.next=popped_node.next
            popped_node.next.prev=popped_node.prev
            popped_node.next=None
            popped_node.prev=None
        self.length-=1
        return popped_node
    
    
    #Str method update:
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.data)
            if temp_node.next is not None:
                result+= ' <-> '
            temp_node=temp_node.next
        return result
            
        
        

dll=DLinkedList()
dll.append(5)
dll.append(10)
dll.append(15)
dll.prepend(1)

print(dll)
dll.traverse()
dll.reverse_traverse()
print(dll.search(1))
print(dll.get(2))

dll.remove(1)
print(dll)
    
        
        