n=int(input())
a=list(map(int,input().split()))
for i in range(n-1):
    swap=False
    for j in range(0,n-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            swap=True
    if swap==False:
        break
print(a)