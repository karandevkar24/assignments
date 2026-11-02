class Node:
    def __init__(self,data): #this creates a sigle node
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):  #initially the head of any list will be None
        self.head=None

    def insert(self,data): #creates a singly linked list
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node

    def insert_multiple(self,*values): #instead of calling the insert function again and again to insert one element at a time 
        for value in values:           # we can insert all elements in one call
            self.insert(value)

    def display(self):                  #this displays the linked list
        if self.head is None:
            print("the list is empty")
            return
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print(None)

    def merge(self,a,b): #this will link the two linked lists which are given 
        dummy=Node(0)
        curr=dummy
        while a and b :
            if a.data<b.data:
                curr.next=a
                a=a.next
            else:
                curr.next=b
                b=b.next
            curr=curr.next
        curr.next=a if a else b
        return dummy.next

        
    def merge_k_list(self,lists): # this will link n number of link list we just have to give a list contaning head of all the linked lists
        if not lists:
            return None
        merge_head=lists[0]
        for i in range(1,len(lists)):
            merge_head=self.merge(merge_head,lists[i])
        return merge_head
        
l1=linkedlist()
l2=linkedlist()
l3=linkedlist()
merged=linkedlist()
l1.insert_multiple(10,20,30,40,50)
l2.insert_multiple(11,22,33,44,55)
l3.insert_multiple(15,25,35,45,60)
l1.display()
l2.display()
l3.display()
lists=[l1.head,l2.head,l3.head]
merged.head=merged.merge_k_list(lists)
merged.display()
