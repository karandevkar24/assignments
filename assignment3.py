class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head

            
    def display(self):
        if self.head is None:
            print("the list is empty")
            return
        temp=self.head
        hset=set()
        while temp:
            if temp in hset:
                break
            else:
                print(temp.data,end="->")
                hset.add(temp)
                temp=temp.next
        print(temp.data)

        
    def distort(self,position):
        if self.head is None:
            print("the list is empty")
            return
        last=self.head
        while last.next!=self.head:
            last=last.next
        target=self.head
        count=1
        while count<=position:
            target=target.next
            count+=1
        last.next=target

    def relink(self):
        if self.head is None:
            print("the list is empty")
            return
        temp=self.head 
        tset=set()
        while temp:
            if temp.next not in tset:
                tset.add(temp)
                temp = temp.next
            else:
                temp.next=self.head
                break
l1=linkedlist()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insert(40)
l1.insert(50)
l1.display()
l1.distort(3)
l1.display()
l1.relink()
l1.display()
