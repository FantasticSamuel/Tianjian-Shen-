from collections import deque
while True:
    n,p,m=map(int,input().split())
    if n==0 and p==0 and m==0:break
    a=deque(range(1,n+1))
    a.rotate(1-p)
    while a:
        a.rotate(1-m)
        print(a[0],end='')
        a.popleft()
        if a:print(',',end='')
        else:print()
    