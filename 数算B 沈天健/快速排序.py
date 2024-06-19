def partition(a,l,r):
    pavot=a[l]
    i=l+1;j=r
    while i<=j:
        while i<=r and a[i]<=pavot:i+=1
        while j>=l+1 and a[j]>=pavot:j-=1
        if i>j:break
        a[i],a[j]=a[j],a[i]
    a[l],a[j]=a[j],a[l]
    return j
def qsort(a,l=0,r=None,inplace=True):
    if inplace is False:
        a=a[:]
    if r is None:
        r=len(a)-1
    if l>=r:return
    mid=partition(a,l,r)
    qsort(a,l=l,r=mid-1)
    qsort(a,l=mid+1,r=r)
    if inplace is False:
        return a
a=list(map(int,input().split()))
qsort(a)
print(a)
