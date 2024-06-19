def yibu(x,y):
    bianhua=[]
    h0=dd[x][y]
    for r in [(0,-1),(0,1),(1,0),(-1,0)]:
        xx,yy=x+r[0],y+r[1]
        if -1<xx<m and -1<yy<n:
         if d[xx][yy]!='#':
            hh=h0+abs(d[xx][yy]-d[x][y])
            if dd[xx][yy]=='0':
                dd[xx][yy]=hh
                bianhua.append((xx,yy))
            else:
                if hh<dd[xx][yy]:
                    dd[xx][yy]=hh
                    bianhua.append((xx,yy))
    return bianhua

d=[]
dd0=[]

m,n,p=[int(x) for x in input().split()]
for i in range(m):
    hang=[x for x in input().split()]
    dhang=[]
    ddhang=[]
    for j in hang:
        if j!='#':
            dhang.append(int(j))
            ddhang.append('0')
        else:
            dhang.append('#')
            ddhang.append('#')
    d.append(dhang+[])
    dd0.append(ddhang+[])
for cishu in range(p):
  dd=[]
  for i in range(m):
    dd.append(dd0[i]+[])
  x1,y1,x2,y2=[int(x) for x in input().split()]
  dd[x1][y1]=0
  if d[x1][y1]=='#':
      print('NO')
      continue
  else:
      bianhua=yibu(x1,y1)
  jixu=1
  while jixu==1:
    xinbianhua=[]
    for wz in bianhua:
        xbh=yibu(wz[0],wz[1])
        xinbianhua=list(set(xinbianhua+xbh))
    bianhua=xinbianhua+[]
    if bianhua==[]:
        jixu=0
  dd[x1][y1]=0
  if type(dd[x2][y2])==type(1):
     print(dd[x2][y2])
  else:
     print('NO')
