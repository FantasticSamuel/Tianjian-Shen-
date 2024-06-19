n=int(input())
if n==0:
    print('*')
N=3**n
a=['*' for _ in range(N)]
def dele(a,l,r):
    if l==r:return
    m1=l+(r-l+1)//3
    m2=l+(r-l+1)//3*2-1
    for i in range(m1,m2+1):
        a[i]='-'
    dele(a,l,m1-1)
    dele(a,m2+1,r)
dele(a,0,N-1)
print(''.join(a))