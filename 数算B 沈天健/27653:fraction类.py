#2300011417 沈天健
def gcd(m,n):
    m,n=max(m,n),min(m,n)
    while m%n!=0:
        m,n=n,m%n
    return n
class fraction:
    def __init__(self,u,d):
        self.u=u
        self.d=d
    def add(self,other):
        answer=fraction(None,None)
        answer.d=self.d*other.d
        answer.u=self.u*other.d+self.d*other.u
        gcdd=gcd(answer.d,answer.u)
        answer.d=int(answer.d/gcdd)
        answer.u=int(answer.u/gcdd)
        return answer
u1,d1,u2,d2=map(int,input().split())
ans=fraction(u1,d1).add(fraction(u2,d2))
if ans.d==1:
    print(f'{ans.u}')
else:
    print(f'{ans.u}/{ans.d}')
    
