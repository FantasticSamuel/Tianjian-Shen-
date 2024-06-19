#2300011417 沈天健
n,a,b,c=input().split()
n=int(n)
def move(n,s,e,o):
    if n==1:
        print(f'1:{s}->{e}')
        return
    move(n-1,s,o,e)
    print(f'{n}:{s}->{e}')
    move(n-1,o,e,s)
move(n,a,c,b)