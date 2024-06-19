n=int(input())
from collections import defaultdict
dic1={'B':1,'M':0}
dic=defaultdict(list)
for i in range(n):
    name,size=input().split('-')
    dic[name].append(size)
for name in sorted(dic):
    dic[name].sort(key=lambda size: (dic1[size[-1]],float(size[:-1])))
    print(name+': '+', '.join(dic[name]))
                