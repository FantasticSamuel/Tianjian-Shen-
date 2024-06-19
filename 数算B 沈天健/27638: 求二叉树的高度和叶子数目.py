class treenode:
    def __init__(self):
        self.right=None
        self.left=None
    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False
def depth(node):
    if node is None:
        return -1
    return max(depth(node.left),depth(node.right))+1
def count_leaves(node):
    if node is None:
        return 0
    if node.is_leaf():
        return 1
    return count_leaves(node.left)+count_leaves(node.right)
n=int(input())
tree=[treenode() for i in range(n)]
has_parent=[False for i in range(n)]
for i in range(n):
    l,r=map(int,input().split())
    if l!=-1:
        tree[i].left=tree[l]
        has_parent[l]=True
    if r!=-1:
        tree[i].right=tree[r]
        has_parent[r]=True
root=tree[has_parent.index(False)]
print(f'{depth(root)} {count_leaves(root)}')