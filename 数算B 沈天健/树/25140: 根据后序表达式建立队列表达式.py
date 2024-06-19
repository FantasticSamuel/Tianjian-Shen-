class treenode:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None
    def duiliebiaodashi(self):
        from collections import deque
        q=deque()
        q.append(self)
        ans=''
        while q:
            node=q.popleft()
            ans+=node.value
            if node.left!=None:q.append(node.left)
            if node.right!=None:q.append(node.right)   
        return ans[::-1]     
def BuildFromPost(s):
    stack=[]
    for ch in s:
        if ch in 'abcdefghijklmnopqrstuvwxyz':
            stack.append(treenode(value=ch))
        else:
            node=treenode(value=ch)
            node_r=stack.pop()
            node_l=stack.pop()
            node.left=node_l
            node.right=node_r
            stack.append(node)
    return stack[0]
if __name__=='__main__':
    n=int(input())
    for i in range(n):
        s=input()
        t=BuildFromPost(s)
        print(t.duiliebiaodashi())