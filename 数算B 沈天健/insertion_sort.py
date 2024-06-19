n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    j=i
    while j>0 and a[j]<a[j-1]:
        a[j],a[j-1]=a[j-1],a[j]
        j-=1
for i in range(n):
    print(a[i])