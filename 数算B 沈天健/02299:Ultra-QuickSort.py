#2300011417 沈天健
def merge(a,l,r,temp):
    if r==l:
        return 0
    if r-l==1:
        ans=0
        if a[l]>a[r]:ans+=1;a[l],a[r]=a[r],a[l]
        return ans
    ans=0
    mid=(l+r)//2
    ans+=merge(a,l,mid,temp)
    ans+=merge(a,mid+1,r,temp)
    i=l;j=mid+1;k=l
    while i<=mid and j<=r and k<=r:
        if a[i]>a[j]:
            temp[k]=a[j]
            j+=1
            k+=1
            ans+=mid-i+1
        else:
            temp[k]=a[i]
            i+=1
            k+=1
    while i<=mid and k<=r:
        temp[k]=a[i]
        i+=1
        k+=1
    while j<=r and k<=r:
        temp[k]=a[j]
        j+=1
        k+=1
    if i!=mid+1:
        print('i error')
        print(a[l:(r+1)])
        print(a[l:(r+1)])
        print(i)
    if j!=r+1:
        print('j error')
        print(a[l:(r+1)])
        print(a[l:(r+1)])
        print(j)   
    if k!=r+1:
        print('k error')
        print(a[l:(r+1)])
        print(a[l:(r+1)])
        print(k) 
    for i in range(l,r+1):
        a[i]=temp[i] 
    return ans
while True:
    n=int(input())
    if n==0:
        break
    a=[]
    temp=[0 for _ in range(n)]
    for i in range(n):
        a.append(int(input()))
    print(merge(a,0,n-1,temp))