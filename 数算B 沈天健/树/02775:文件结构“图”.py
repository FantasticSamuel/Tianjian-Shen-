class treenode:
    def __init__(self,value):
        self.value=value
        self.children=[]
    def __lt__(self,other):
        if (self.value[0]=='d' and other.value[0]=='f') or (self.value[0]=='f' and other.value[0]=='f' and self.value<other.value):
            return True
        return False
n=1
def preorder(node):
    print(node.value,end=' ')
    for child in node.children:
        preorder(child)
def dfs(node_root):
    output=[]
    output.append(node_root.value)
    node_root.children.sort()
    for child in node_root.children:
        if child.value[0]=='f':
            output.append(child.value)
        else:
            outputs=dfs(child)
            for out in outputs:
                out='|     '+out
                output.append(out)
    return output
def handle(node_root,n):
    print(f'DATA SET {n}:')
    output=dfs(node_root)
    print('\n'.join(output))
    print()
node_0=treenode('ROOT')
stack=[node_0]
while True:
    s=input()
    if s=='#':
        break
    if s[0]=='d':
        node=treenode(s)
        stack[-1].children.append(node)
        stack.append(node)
    if s[0]=='f':
        node=treenode(s)
        stack[-1].children.append(node)
    if s==']':
        stack.pop()
    if s=='*':
        handle(node_0,n)
        # print()
        # preorder(node_0)
        # print()
        node_0=treenode('ROOT')
        stack.append(node_0)
        n+=1