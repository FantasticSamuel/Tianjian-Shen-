n=int(input())
a=list(map(int,input().split()))
gap=n//2
def insert_sort(start,gap):
    j0=start+gap
    while j0<n:
        j=j0
        while j-gap>=0 and a[j-gap]>a[j]:
            a[j-gap],a[j]=a[j],a[j-gap]
            j-=gap
        j0+=gap
while gap>=1:
    for start in range(gap):
        insert_sort(start,gap)
        #print(a,gap)
    gap//=2
print(a)