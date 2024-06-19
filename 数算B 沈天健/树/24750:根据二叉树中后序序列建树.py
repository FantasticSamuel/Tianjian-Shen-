s1=input()
s2=input()
def preorder(mid,post):
    if len(mid)==0 and len(post)==0:return
    root=post[-1]
    root_index=mid.index(root)
    mid_l=mid[:root_index]
    mid_r=mid[root_index+1:]
    post_l=post[:root_index]
    post_r=post[root_index:-1]
    print(root,end='')
    preorder(mid_l,post_l)
    preorder(mid_r,post_r)
if len(s1)==0 and len(s2)==0:
    print('')
elif len(s1)==1 and len(s2)==1:
    print(s1)
else:
    preorder(s1,s2)