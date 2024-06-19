n=int(input())
a=list(map(float,input().split()))
from dataclasses import dataclass
@dataclass
class c:
    i:int
    t:float
    def __lt__(self,other):
        if self.t==other.t:
            return self.i<other.i
        else:  
            return self.t<other.t
b=[]
for i in range(1,n+1):
    b.append(c(i,a[i-1]))
b.sort()
sum=0
for ii in range(n):
    print(b[ii].i,end=' ')
    sum+=b[ii].t*(n-ii-1)
print()
print(f'{round(sum/n,2):.2f}')