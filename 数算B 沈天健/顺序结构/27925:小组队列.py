from collections import deque
t=int(input())
group_id={}
for i in range(t):
    group=list(map(int,input().split()))
    for j in group:group_id[j]=i
q=deque()
pos={}
while True:
    command=input()
    if command[0]=='S':break
    elif command[0]=='D':
        head,g_id=q.popleft()
        print(head.popleft())
        if not head:pos[g_id]=None
        else:q.appendleft((head,g_id))
    else:
        _,x=command.split()
        x=int(x)
        g_id=group_id[x]
        if g_id not in pos or pos[g_id] is None:
            q_new=deque()
            q_new.append(x)
            q.append((q_new,g_id))
            pos[g_id]=q_new
        else:
            pos[g_id].append(x)
    x=int(x)
