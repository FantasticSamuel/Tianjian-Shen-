class treenode:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None
    def preorder(self):
        print(self.value,end=' ')
        if self.left:self.left.preorder()
        if self.right:self.right.preorder()
    def printExp(self):
        dic={'not':3,'or':1,'and':2}
        if self.left==None and self.right==None:
            return self.value,float('inf')
        n=dic[self.value]
        if self.value!='not':
            l,ln=self.left.printExp()
            r,rn=self.right.printExp()
            if ln<n:
                l='( '+l+' )'
                ln=4
            if rn<=n:#要求左序
                r='( '+r+' )'
                rn=4
            return l+' '+self.value+' '+r,min(rn,ln,n)
        else:
            r,rn=self.right.printExp()
            if rn<=n:#要求左序
                r='( '+r+' )'
                rn=4
            return self.value+' '+r,min(rn,n)
def BuildFromMiddle(s):
    def BuildOperatorTree(operator,stack_result):
        node=treenode(value=operator)
        if operator=='not':
            node_r=stack_result.pop()
            node.right=node_r
            stack_result.append(node)
        else:
            node_r=stack_result.pop()
            node_l=stack_result.pop()
            node.left=node_l
            node.right=node_r
            stack_result.append(node)
    stack_operator=[]
    stack_result=[]
    dic={'not':3,'or':1,'and':2,'(':0}
    for ch in s:
        if ch=='(':stack_operator.append(ch)
        elif ch==')':
            while True:
                operator=stack_operator.pop()
                if operator=='(':break
                BuildOperatorTree(operator,stack_result)
        elif ch in ['True','False']:stack_result.append(treenode(value=ch))
        else:
            while stack_operator and dic[stack_operator[-1]]>=dic[ch]:
                operator=stack_operator.pop()
                BuildOperatorTree(operator,stack_result)
            stack_operator.append(ch)
    while True:
        if not stack_operator:return stack_result[0]
        operator=stack_operator.pop()
        BuildOperatorTree(operator,stack_result)
if __name__=='__main__':
    s=input().strip().split()
    t=BuildFromMiddle(s)
    ans,_=t.printExp()
    print(ans)