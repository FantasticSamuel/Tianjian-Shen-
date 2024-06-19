class minheap:
    def __init__(self):
        self.heap=[0]
        self.n=0
    def cmp(self,i,f):
        if self.heap[f]>self.heap[i]:self.heap[f],self.heap[i]=self.heap[i],self.heap[f];return True
        else:return False
    def up(self,i):
        while True:
            if i==1:break
            f=i//2
            if self.cmp(i,f) is False:break
            i=f
    def minchild(self,f):
        ans=None
        r=f*2+1
        l=f*2
        if l<=self.n:ans=l
        if r<=self.n and self.heap[r]<self.heap[l]:ans=r
        return ans
    def down(self,f):
        while True:
            minchi=self.minchild(f)
            if minchi is None:break
            if self.cmp(minchi,f) is False:break
            f=minchi
    def insert(self,x):
        self.n+=1
        self.heap.append(x)
        self.up(self.n)
    def pop(self):
        head=self.heap[1]
        self.heap[1]=self.heap[self.n]
        self.n-=1
        self.heap.pop()
        self.down(1)
        return head
    def buildfromarr(self,arr):
        self.n=len(arr)
        self.heap=[0]+arr[:]
        f0=self.n//2
        for f in range(f0,0,-1):self.down(f)

n=int(input())
a=minheap()
for i in range(n):
    s=input()
    if s[0]=='1':typ,u=map(int,s.split());a.insert(u)
    else:print(a.pop())
