n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
if k==0:
    if a[0]>1:print(1)
    else:print(-1)
else:
    i=0
    while True:
        while i<n-1 and a[i]==a[i+1]:i+=1
        if k-1==i:print(a[i]);break
        if i==n-1:print(-1);break
        if i>k-1:print(-1);break
        i+=1