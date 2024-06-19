#2300011417 沈天健
from math import isqrt
is_prime=[True for _ in range(1100000)]
is_prime[0]=False
is_prime[1]=False
prime_list=[]
def shai():
    for i in range(2,1100000):
        if is_prime[i]:
            prime_list.append(i)
        for prime in prime_list:
            if i*prime>1000000:
                break
            is_prime[i*prime]=False
            if i%prime==0:
                break
shai()
n=int(input())
aas=list(map(int,input().split()))
for aa in aas:
    t=isqrt(aa)
    if t*t==aa and is_prime[t]:
        print('YES')
    else:
        print('NO')

