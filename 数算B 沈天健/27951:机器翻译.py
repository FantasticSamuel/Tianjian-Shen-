from collections import deque,defaultdict
m,n=map(int,input().split())
a=list(map(int,input().split()))
d=defaultdict(int)
q=deque()
ans=0
for i in a:
    if d[i]==0:
        ans+=1
        d[i]=1
        q.append(i)
        if len(q)>m:d[q.popleft()]=0
print(ans)