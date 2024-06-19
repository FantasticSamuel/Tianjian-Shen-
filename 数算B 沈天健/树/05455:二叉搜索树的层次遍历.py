from collections import deque

class treenode:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None
    def postorder(self):
        if self.left:self.left.postorder()
        if self.right:self.right.postorder()
        print(self.value,end=' ')
    def insert(self,x):
        if x>self.value:
            if self.right:self.right.insert(x)
            else:self.right=treenode(x)
        else:
            if self.left:self.left.insert(x)
            else:self.left=treenode(x)
    def bfs(self):
        q=deque()
        q.append(self)
        while q:
            node=q.popleft()
            print(node.value,end=' ')
            if node.left:q.append(node.left)
            if node.right:q.append(node.right)

a=list(map(int,input().split()))
a=list(dict.fromkeys(a))
n=len(a)
tree=treenode(value=a[0])
for i in range(1,n):
    tree.insert(a[i])
tree.bfs()