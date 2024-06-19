#沈天健
#oj27312 拍照
n=int(input())
s=input()
i=0
ans=0
is_end=True
while True:
    flag=False
    while i<n-1 and (s[i+1]==s[i] or (s[i+1]=='H' and s[i]=='G')):
        if s[i+1]=='H' and s[i]=='G':
            flag=True
        i+=2
    if flag:
        if is_end:
            ans+=1
        else:
            ans+=2
    if i>=n:
        break
    is_end=False
    while i<n-1 and (s[i+1]=='G' and s[i]=='H'):i+=2
    if i>=n:
        break
print(ans)