class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        self.height=1
        self.prev=None
def height(node):
    if node is None:
        return 0
    return node.height
def insert(root,data):
    if root is None:
        return Node(data)
    if data<root.data:
        root.left=insert(root.left,data)
    elif data>root.data:
        root.right=insert(root.right,data)
    else:
        return root
    root.height=1+max(height(root.left),height(root.right))

    balance=height(root.left)-height(root.right)
    if balance>1 and data<root.left.data:
        return right_rotate(root)

    if balance<-1 and data>root.right.data:
        return left_rotate(root)

    if balance >1 and data>root.left.data:
        root.left=left_rotate(root.left)
        return right_rotate(root)
    return root

def left_rotate(y):
    x=y.right
    temp=x.left
    x.left=y
    y.right=temp
    x.height=1+max(height(x.left),height(x.right))
    y.height=1+max(height(y.left),height(y.right))
    return y

def right_rotate(y):
    x=y.left
    temp=x.right
    x.right=y
    y.left=temp
    x.height=1+max(height(x.left),height(x.right))
    y.height=1+max(height(y.left),height(y.right))
    return y
    
def set_predecessors(root):
    previous=[None]
    def postorder(node):
        if node is None:
            return
        postorder(node.left)
        postorder(node.right)
        node.prev=previous[0]
        previous[0]=node
    postorder(root)

def search(root,key):
    while root is not None:
        if key==root.data:
            return root

        elif key<root.data:
            root=root.left
        else:
            root=root.right
    return None
def find_predecessor(root,key):
    node=search(root,key)
    if node is None:
        return "key not found"
    if node.prev is None:
        return "No predecessor"
    return node.prev.data

root=None
values=[50,30,70,20,40,60,80]
for value in values:
    root=insert(root,value)
set_predecessors(root)
key=int(input())
print("the postorder predecessor of", key, "is",find_predecessor(root,key))
