a=list(map(int,input().split()))
b=list(map(int,input().split()))
summ=0
for i in range(5):
    summ+=a[i]**2*b[i]
print(summ)