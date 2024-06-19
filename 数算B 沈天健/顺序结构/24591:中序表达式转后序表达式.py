def middleturnpost(s):
    dic={'(':1,')':1,'*':3,'/':3,'+':2,'-':2}
    stack=[]
    for ch in s:
        if ch=='(':
            stack.append(ch)
        elif ch==')':
            while True:
                cha=stack.pop()
                if cha=='(':
                    break
                print(cha,end=' ')
        elif ch in '+-*/':
            while True:
                if not stack or dic[stack[-1]]<dic[ch]:
                    break
                cha=stack.pop()
                print(cha,end=' ')
            stack.append(ch)
        else:print(ch,end=' ')
    while stack:
        print(stack.pop(),end=' ')
def inp():
    s=input().strip()
    import re
    s=re.split(r'([\(\)\+\-\*\/])',s)
    s=[item for item in s if item.strip()]
    return s
n=int(input())
for _ in range(n):
    s=inp()
    middleturnpost(s)
    print()
