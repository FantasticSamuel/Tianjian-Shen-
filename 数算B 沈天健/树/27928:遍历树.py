#2300011417 沈天健
def go(root,graph):
    a=[root]+graph[root][:]
    a.sort()
    for node in a:
            if node==root:print(root)
            else:go(node,graph)
n=int(input())
if n==1:
    node=int(input())
    print(node)
else:
    from collections import defaultdict
    graph=defaultdict(list)
    is_child=defaultdict(bool)
    for i in range(n):
        a=list(map(int,input().split()))
        for i in range(1,len(a)):
            graph[a[0]].append(a[i])
            is_child[a[i]]=True
    for key in graph:
        if is_child[key]==False:root=key;break
    go(root,graph)
