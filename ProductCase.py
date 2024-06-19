import random
import sys
import os

# if len(sys.argv) != 2:
#     print("Usage: produceCase.py caseNum\n无输入程序将使用使用默认case数量20")
#     caseNum = 20
# else:
#     caseNum = int(sys.argc[1])

caseNum = 18

for i in range(5,14):

    with open(str(i+1) + ".in", "w") as fout:
        m= random.randint(3, 50)
        n= random.randint(3, 50)
        p= random.randint(0, 100)
        h= random.randint(3,50)
        tp=int(input())
        print(m,n,p,file=fout)
        for hang in range(m):
            for lie in range(n):
                t=random.randint(0,h)
                tt=random.randint(1,100)
                if tt<tp:
                    print('#',file=fout,end=' ')
                else:
                    print(t,file=fout,end=' ')
            print('',file=fout)
        for cishu in range(p):
            x1= random.randint(0,m-1)
            y1= random.randint(0,n-1)
            x2= random.randint(0,m-1)
            y2= random.randint(0,n-1)
            print(x1,y1,x2,y2,file=fout)


    os.system("python sampleCode.py < %d.in > %d.out" %(i+1, i+1))

