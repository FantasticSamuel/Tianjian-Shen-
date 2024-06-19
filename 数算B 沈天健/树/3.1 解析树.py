def val(value):
    if type(value)==treenode:
        return value
    else:
        return treenode(value)

class treenode:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
    def leftin(self,value=None):
        if self.left==None:
            self.left=val(value)
        else:
            t=val(value)
            t.left=self.left
            self.left=t
    def rightin(self,value=None):
        if self.right==None:
            self.right=val(value)
        else:
            t=val(value)
            t.right=self.right
            self.right=t
    def valuein(self,value=None):
        if self.left==None:
            self.left=val(value)
        elif self.value==None:
            self.value=value
        elif self.right==None:
            self.right=val(value)   
        else:
            print('valuein error:the treenode is already full!')
    def preorder(self,end=' '):
        print(self.value,end=end)
        if self.left!=None:self.left.preorder(end=end)
        if self.right!=None:self.right.preorder(end=end)
    def cal(self,precision=None):
        try:
            float(self.value)
            if precision is None:return self.value
            else:return f"{float(self.value):.{precision}f}"
        except:
            if precision is None:
                            return str(eval(self.left.cal()+self.value+self.right.cal()))
            return f"{eval(self.left.cal(precision=precision)+self.value+self.right.cal(precision=precision)):.{precision}f}"
    def prebuild(self,s,i):
        self.value=s[i]
        try:
            float(s[i])
            return i+1
        except:
            self.left=treenode()
            i_1=self.left.prebuild(s,i+1)
            self.right=treenode()
            i_2=self.right.prebuild(s,i_1)
            return i_2
class stackclass:
    def __init__(self):
        self.sta=[]
    def push(self,value=None):
        self.sta.append(val(value))
    def pop(self):
        return self.sta.pop()
    def notempty(self):
        return self.sta
    def pushtree(self,ch):
        self.sta[-1].valuein(ch)
    def size(self):
        return len(self.sta)
        
def inp():
    s=input().strip()
    import re
    s=re.split(r'(\s+|[\+\-\*\/\(\)])',s)
    s=[item for item in s if item.strip()]
    return s

def build_tree_from_middle(s):
    if len(s)==1:
        return treenode(value=s[0])
    else:
        stack=stackclass()
        node_root=treenode()
        for ch in s:
            if ch=='(':
                if stack.notempty():
                    stack.push()
                else:
                    stack.push(node_root)
            elif ch==')':
                if stack.size()>1:
                    stack.pushtree(stack.pop())
                else:
                    stack.pop()
            else:stack.pushtree(ch)
        return node_root
def build_tree_from_pre(s):
    if len(s)==1:
        return treenode(value=s[0])
    else:
        root_node=treenode()
        root_node.prebuild(s,0)
        return root_node
    
if __name__=='__main__':
    s=inp()
    root=build_tree_from_pre(s)
    print(f'{float(root.cal()):.6f}')
