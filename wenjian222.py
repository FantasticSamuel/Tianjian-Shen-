import random
#a=open('10.in','w')
#b=open('10.out','w')
for i in range(3,4):
    a=open(str(i)+'.in','w')
  #  b=open(str(i)+'.out','w')
  #  m,n,h=[int(x) for x in input().split()]
    while:
        
    with open(str(i)+'.in','w') as fo:
     print('\n',file=fo,line=1)
     print(m,n,file=fo)
  #   for i in range (m):
  #      for j in range(n):
            print(random.randint(1,h),file=fo,end=' ')
        print('',file=fo)
