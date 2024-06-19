#2300011417 沈天健
class treenode:
    def __init__(self,val):
        self.val=val
        self.childs=[]
s =input().strip()
s =''.join(s.split()) 
stack=[]
root=None
if len(s)==1:
    print(s)
    print(s)
else:
    for ch in s:
        if ch.isalpha():
            node=treenode(ch)
            if stack:
                stack[-1].childs.append(node)
        if ch=='(':
            if node:
                stack.append(node)
                node=None
        if ch==')':
            if stack:
                root=stack.pop()
    def preorder(node):
        print(node.val,end='')
        for child in node.childs:
            preorder(child)
    def postorder(node):
        for child in node.childs:
            postorder(child)
        print(node.val,end='')
    if root:
        preorder(root)  # 输出前序遍历序列
        print()
        postorder(root)  # 输出后序遍历序列
    else:
        print("input tree string error!")


