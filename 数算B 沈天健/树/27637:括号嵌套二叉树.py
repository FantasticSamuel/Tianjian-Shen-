from typing import List

class treenode:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None
    def preorder(self):
        print(self.value,end='')
        if self.left and self.left.value!='*':self.left.preorder()
        if self.right and self.right.value!='*':self.right.preorder()
    def midorder(self):
        if self.left and self.left.value!='*':self.left.midorder()
        print(self.value,end='')
        if self.right and self.right.value!='*':self.right.midorder()

def buildtree(s):
    stack:List[treenode]=[]
    for ch in s:
        if ch.isalpha() or ch=='*':
            node=treenode(value=ch)
            if stack:
                if stack[-1].left:
                    stack[-1].right=node
                else:stack[-1].left=node
        elif ch=='(':stack.append(node)
        elif ch==')':node=stack.pop()
    rootnode=node
    return rootnode

n=int(input())
for _ in range(n):
    s=input()
    if s=='*':print();print()
    elif len(s)==1:print(s);print(s)
    else:
        root=buildtree(s)
        root.preorder()
        print()
        root.midorder()
        print()