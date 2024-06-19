class digset:
    def __init__(self,n):
        self.f=[i for i in range(n+1)]
        self.level=[0 for i in range(n+1)]
    def find(self,x):
        if self.f[x]==x:return x
        else:
            self.f[x]=self.find(self.f[x])
            return self.f[x]
    def merge(self,x,y):
        fx=self.find(x)
        fy=self.find(y)
        if self.level[fx]<self.level[fy]:self.f[fy]=fx
        elif self.level[fx]<self.level[fy]:self.f[fx]=fy
        else:
            self.level[fy]+=1
            self.f[fy]=fx

case=0
while True:
    case+=1
    n,m=map(int,input().split())
    if n==0 and m==0:break
    a=digset(n)
    for _ in range(m):
        x,y=map(int,input().split())
        a.merge(x,y)
    b=set()
    ans=0
    for i in range(1,n+1):
        f=a.find(i)
        if f not in b:
            ans+=1
            b.add(f)
    print(f'Case {case}: {ans}')