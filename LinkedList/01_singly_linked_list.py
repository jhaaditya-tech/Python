class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0


    #Insertion to Linked List in Memeory, At the begining, at the middle after the node, or at the end of the linked list
        
    #Append method, singly linked list, i.e. at the begining of linkedlist
    #First create a new node, update the last node next pointer to update to a new node, and update the tail to point to a new node
    #If linked list empty, new node, head to point newe node and also tail to point the new node
    #Time COmplexity (O(1))
    
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    #Prepend, inserting element at the begining of the linked list
    #Constant time complexity
    def prepend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    #Inserting at specific location at singly linked list, loop untl index-1, stop and update new node next reference, with all edge cases
    #Linear time Complexity
    def insert(self, index, data):
        new_node=Node(data)
        temp_node=self.head
        if index<0 or index>self.length:
            return False
        elif self.head is None:
            self.head=new_node
            self.tail=new_node
        elif index==0: #Edge case for the first element insertion
            new_node.next=self.head
            self.head=new_node
        else:
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length+=1
        return True   

    #Search for node in singly linked list
    #Linear time complexity
    def search(self,target):
        current=self.head
        index=0
        while current:
            if current.data==target:
                print(f"Found at index {index}")
                return
            current=current.next
            index+=1
           
        print("Search Failed")

    #Traversal of Singly Linked List
    #Linear time complexity
    def traverse(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next

    #Get method, passing index as a parameter and getting the value of that index
    #Linear time complexity
    def get(self, index):
        current=self.head
        if index<0 or index>=self.length:
            return -1
        for _ in range(index):
            current=current.next
        print(current.data)

    #Set method, update the value at particulat index
    #Linear time comlexity
    def set(self,index,data):
        current=self.head
        if current:
            for _ in range(index):
                current=current.next
            current.data=data
            return True
        else:
            return False


    #Pop first, remove first node from the singly linked list, consider case where you have only one node, or no node
    #Constant Time Complexity
    def pop_first(self):
        if self.length==0:
            return None
        pop_first_node=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            pop_first_node.next=None
        self.length-=1
        return pop_first_node.data
  
    #Pop, remove the last node from the end
    #Linear time complexity
    def pop(self):
        popped_node=self.tail
        if self.length==0:
            return None
        if self.length==1:
            self.head=None
            self.tail=None
        pop_node=self.head
        while pop_node.next is not self.tail:
            pop_node=pop_node.next
        self.tail=pop_node
        self.tail.next=None
        self.length-=1
        return popped_node.data

    #Remove method in Singly Linked List
    #Linear time complexity
    def remove(self, index):
        if index<0 or index>=self.length:
            return -1
        elif self.length==1:
            self.head=None
            self.tail=None
        if index==0:
            return self.pop_first()
        if index==self.legth-1:
            return self.pop()
        prev_node=self.head
        for _ in range(index-1):
            prev_node=prev_node.next
        removed_node=prev_node.next
        prev_node.next=removed_node.next
        removed_node.next=None
        self.length-=1
        return removed_node.data

    #Delete all nodes in Singly Linked List
    #Constant time complexity
    def delete(self):
        self.head=None
        self.tail=None
        self.length=0


    #Printing out the Linked List
    #Str method to overwrite to print the linked list
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.data)
            if temp_node.next is not None:
                result+=' -> '
            temp_node=temp_node.next
        return result



new_linked_list=LinkedList()

new_linked_list.append(10)
new_linked_list.append(11)
new_linked_list.append(44)
new_linked_list.prepend(1)
new_linked_list.prepend(0)
new_linked_list.insert(0,56)

new_linked_list.set(4,12)

print(new_linked_list)

print(new_linked_list.pop_first())
print(new_linked_list.pop())

print(new_linked_list)

print(new_linked_list.remove(0))
print(new_linked_list)

#new_linked_list.traverse()






