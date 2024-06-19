n=int(input())
a=list(map(int,input().split()))
for head in range(n):
    i0=head
    for i in range(head+1,n):
        if a[i]<a[i0]:
            i0=i
    a[head],a[i0]=a[i0],a[head]
print(a)