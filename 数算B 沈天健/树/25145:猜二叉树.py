from collections import deque
from typing import Deque

class treenode:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None
    def preorder(self):
        print(self.value,end='->')
        if self.left:self.left.preorder()
        if self.right:self.right.preorder()

def buildtree(mid,post):
    if len(mid)==0 and len(post)==0:return None
    root=post[-1]
    root_index=mid.index(root)
    mid_l=mid[:root_index]
    mid_r=mid[root_index+1:]
    post_l=post[:root_index]
    post_r=post[root_index:-1]
    rootnode=treenode(value=root)
    node_l=buildtree(mid_l,post_l)
    node_r=buildtree(mid_r,post_r)
    rootnode.left=node_l
    rootnode.right=node_r
    return rootnode

def bfs(root):
    q:Deque[treenode]=deque()
    q.append(root)
    while q:
        node=q.popleft()
        print(node.value,end='')
        if node.left:q.append(node.left)
        if node.right:q.append(node.right)
    print()

n=int(input())
for _ in range(n):
    smid=input()
    spost=input()
    if len(smid)==1 and len(spost)==1:
        print(smid)
    elif len(smid)==0 and len(spost)==0:
        print('')
    else:
        root=buildtree(smid,spost)
        bfs(root)