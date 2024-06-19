class treenode:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None
    def postorder(self):
        if self.left:self.left.postorder()
        if self.right:self.right.postorder()
        print(self.value,end=' ')

def buildtree(n,a):
    if n==0:return None
    if n==1:return treenode(value=a[0])
    idx=n
    for i in range(n):
        if a[i]>a[0]:
            idx=i
            break
    node=treenode(value=a[0])
    node.left=buildtree(idx-1,a[1:idx])
    node.right=buildtree(n-idx,a[idx:])
    return node

n=int(input())
a=list(map(int,input().split()))
tree=buildtree(n,a)
tree.postorder()