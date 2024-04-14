class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CSLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    #Append method, adding element at the end of the linked list
    #Constant time complexity
    def append(self, data):
        new_node=Node(data)
        if self.length==0:
            self.head=self.tail=new_node
            new_node.next=new_node
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        self.length+=1

    #Prepend method, adding element at begining of linked list
    #Constant time complexity
    def prepend(self, data):
        new_node=Node(data)
        if self.length==0:
            self.head=self.tail=new_node
            self.head.next=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=new_node
        self.length+=1

    #Insert method, insert at particular index, with edge cases
    #Linear time complexity
    def insert(self, index, data):
        new_node=Node(data)
        if index<0 or index >=self.length:
            raise Exception("Index out of range")
        if index==0:
            if self.length==0:
                self.head=new_node
                self.tail=new_node
                new_node.next=new_node
            else:
                new_node.next=self.head
                self.head=new_node
                self.tail.next=new_node
        elif index==self.length-1:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
        self.length+=1
        return new_node.data
    
    #Traversal of Circular Singly Linked List
    def traversal(self):
        current_node=self.head
        while current_node is not None:
            print(current_node.data)
            current_node=current_node.next
            if current_node.next==self.head:
                break

    #Search method, serach for particular value
    def search(self, key_value):
        current=self.head
        index=0
        while current is not None:
            if (current.data==key_value):
                return True
            current=current.next
            if (current==self.head):
                break
            index+=1
        return False
        

    #Get method, get the value if the index is provided
    #Linear time complexity
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        current_node=self.head
        for _ in range(index):
            current_node=current_node.next
        return current_node.data


    #Set method
    def set(self, index,data):
        new_node=Node(data)
        current_node=self.head
        if index<0 or index>=self.length:
            return False
        if index==0:
            return self.prepend(data)
        elif index==self.length-1:
            return self.append(data)
        for _ in range(index-1):
            current_node=current_node.next
        new_node.next=current_node.next
        current_node.next=new_node
        self.length+=1
        return True

    #Pop first method, remove first element from the linked list
    def pop_first(self):
        if self.length==0:
            return False
        elif self.length==1:
            self.head=self.tail=None
        else:
            popped_node=self.head
            self.head=self.head.next
            self.tail.next=self.head
            popped_node.next=None
        self.length-=1
        return popped_node.data


    #Pop Method, remove last element from linked list
    #Linear time complexity
    def pop(self):
        popped_node=self.tail
        if self.length==0:
            return False
        if self.length==1:
            self.head=self.tail=None
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            temp.next=self.head
            self.tail=temp
            popped_node.next=None
        self.length-=1
        return popped_node

    #Remove method
    #Linear time complexity
    def remove(self,index):
        if index<0 or index>=self.length:
            return False
        if self.length==1:
            self.head=self.tail=None
        if index==0:
            return self.pop_first()
        elif index==self.length-1:
            return self.pop()
        else:
            temp_node=self.head
            for _ in range(index-1):
                temp_node=temp_node.next
            popped_node=temp_node.next
            temp_node.next=popped_node.next
            popped_node.next=None
        self.length-=1   
        return popped_node.data




    #Delete all nodes
    def delete_all(self):
        if self.length==0:
            return
        self.tail.next=None
        self.head=self.tail=None
        self.length=0


    #Printing out the Linked List
    #Str method to overwrite to print the linked list
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.data)
            temp_node=temp_node.next
            if temp_node==self.head :
                break
            result+=' -> '
        return result


new_linked_list=CSLinkedList()
new_linked_list.append(5)
new_linked_list.append(10)
new_linked_list.append(15)
new_linked_list.append(20)
new_linked_list.append(25)
print(new_linked_list.length)
print(new_linked_list)

new_linked_list.prepend(2)
print(new_linked_list.length)
print(new_linked_list)

new_linked_list.insert(0,51)
print(new_linked_list.length)
print(new_linked_list)


print(new_linked_list.search(10))

new_linked_list.set(2,101)
new_linked_list.set(7,505)
print(new_linked_list)
print(new_linked_list.tail.data)

new_linked_list.pop()
print(new_linked_list)

new_linked_list.remove(4)
print(new_linked_list)