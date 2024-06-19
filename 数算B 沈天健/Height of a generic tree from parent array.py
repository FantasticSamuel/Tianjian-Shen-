#2300011417 沈天健
from heapq import heapify,heappop,heappush
from collections import defaultdict
Maxx=1010
adj=[[] for i in range(Maxx)]
def build_tree(parent,n):
    root_index=None
    for i in range(n):
        if parent[i]==-1:
            root_index=i
        else:
            adj[i].append(parent[i])
            adj[parent[i]].append(i)
    return root_index
def BFS(root):
    q=[]
    dist={}
    heappush(q,(0,root))
    dist[root]=0
    depth_ans=0
    while q:
        depth,node=heappop(q)
        depth+=1
        for leaf in adj[node]:
            if leaf not in dist:
                dist[leaf]=depth
                depth_ans=max(depth_ans,depth)
                heappush(q,(depth,leaf))
    return depth_ans
# Driver code
if __name__ == '__main__':
    parent = [-1, 0, 0, 0, 3, 1, 1, 2] # node 0 to node n-1
    n = len(parent) # Number of nodes in tree

    root_index = build_tree(parent, n)
    ma = BFS(root_index)
    print("Height of N-ary Tree =", ma)

# output: Height of N-ary Tree = 4