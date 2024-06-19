import sys
s0=input().strip()
se=set()
for ch in s0:se.add(ch)
l=len(s0)
def judge(s):
    i=0;j=0
    stack=[]
    while True:
        while j<l and stack and stack[-1]==s[j]:stack.pop();j+=1
        while i<l and j<l and s0[i]!=s[j]:stack.append(s0[i]);i+=1
        if i>=l and stack:print('NO');return
        i+=1;j+=1
        if j>=l:print('YES');return
while True:
    try:
        s=input().strip()
        se1=set()
        for ch in s:
            if ch not in se or ch in se1:
                print('NO')
                break
            else:
                se1.add(ch)
        else:
            if len(s)!=len(s0):print('NO');continue
            judge(s)
    except EOFError:
        break