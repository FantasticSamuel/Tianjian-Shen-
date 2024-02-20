a=0
b=1
c=1
n=int(input())
i=0
while True:
    if i==n:
        print(a)
        break
    a,b,c=b,c,a+b+c
    i+=1
