class DisgSet:
    def __init__(self,n):
        self.rank=[1]*n
        self.f=list(range(n))
    def find(self,x):
        if self.f[x]!=x:
            self.f[x]=self.find(self.f[x])
        else:
            return x
    def union(self,x,y):
        f_x=self.find(x)
        f_y=self.find(y)
        if f_x==f_y:
            return
        else:
            if self.rank[f_x]<self.rank[f_y]:self.f[f_x]=f_y
            elif self.rank[f_x]>self.rank[f_y]:self.f[f_y]=f_x
            else:self.f[f_x]=f_y;self.rank[f_y]+=1
a=DisgSet(5)
b=DisgSet(5)
a.union(0,1)
a.union(2,3)
a.union(1,4)
print(a.rank)
print(a.f)
print(b.rank)
print(b.f)

