class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.height=1
    def update(self):
        height=0
        if self.right:height=max(height,self.right.height)
        if self.left:height=max(height,self.left.height)
        self.height=height+1
    def balance(self):
        hr=0;hl=0
        if self.right:hr=self.right.height
        if self.left:hl=self.left.height
        return hl-hr
    def rotate_left(self):
        r=self.right
        rl=self.right.left
        r.left=self
        self.right=rl
        self.update()
        r.update()
        return r
    def rotate_right(self):
        l=self.left
        lr=self.left.right
        l.right=self
        self.left=lr
        self.update()
        l.update()
        return l
    def insert(self,x):
        if x<self.value:
            if self.left:self.left=self.left.insert(x)
            else:self.left=node(x)
        elif x>self.value:
            if self.right:self.right=self.right.insert(x)
            else:self.right=node(x)
        self.update()
        balance=self.balance()
        if balance>1:
            if x<self.left.value:
                return self.rotate_right()
            elif x>self.left.value:
                self.left=self.left.rotate_left()
                return self.rotate_right()
        if balance<-1:
            if x>self.right.value:
                return self.rotate_left()
            elif x<self.right.value:
                self.right=self.right.rotate_right()
                return self.rotate_left() 
        return self    
    def preorder(self,ans):
        ans.append(str(self.value))
        if self.left:self.left.preorder(ans)
        if self.right:self.right.preorder(ans)

n=int(input())
a=list(map(int,input().split()))
tree=node(a[0])
for i in range(1,n):
    tree=tree.insert(a[i])
ans=[]
tree.preorder(ans)
print(' '.join(ans))


        
