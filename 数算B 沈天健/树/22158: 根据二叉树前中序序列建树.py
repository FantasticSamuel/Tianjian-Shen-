def preorder(mid,pre):
    if len(mid)==0 and len(pre)==0:return
    root=pre[0]
    root_index=mid.index(root)
    mid_l=mid[:root_index]
    mid_r=mid[root_index+1:]
    post_l=pre[1:root_index+1]
    post_r=pre[root_index+1:]
    preorder(mid_l,post_l)
    preorder(mid_r,post_r)
    print(root,end='')

while True:
    try:
        s1=input()
        s2=input()
        if len(s1)==0 and len(s2)==0:
            print('')
        elif len(s1)==1 and len(s2)==1:
            print(s1)
        else:
            preorder(s2,s1)
            print()
    except EOFError:
        break