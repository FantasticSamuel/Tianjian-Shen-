class treenode:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None
    def postorder(self,end=' '):
        if self.left!=None:self.left.postorder(end=end)
        if self.right!=None:self.right.postorder(end=end)
        print(self.value,end=end)

def buildtree(n,s):
    dic={'0':'B','1':'I'}
    if n==0:
        node=treenode(dic[s])
        return node
    l=2**n
    node=treenode()
    node.left=buildtree(n-1,s[:l//2])
    node.right=buildtree(n-1,s[l//2:])
    vl=node.left.value
    vr=node.right.value
    if vl==vr=='B':node.value='B'
    elif vl==vr=='I':node.value='I'
    else:node.value='F'
    return node

n=int(input())
s=input()
tree=buildtree(n,s)
tree.postorder(end='')