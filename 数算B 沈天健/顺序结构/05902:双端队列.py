#2300011417 沈天健
class block:
    def __init__(self,size=1):
        if size==1:
            self.value=None
        else:    
            self.value=[None]*size
            self.t=0
        self.l=size
        self.next=None
        self.pre=None

def val(blok,sep='->'):
    if type(blok.value)==list:
        if blok.t==0:
            return None
        else:
            return sep.join(map(str,blok.value[:blok.t]))
    else:return blok.value
def TailAddBlock(blok):
    blok.next=block(blok.l)
    blok.next.pre=blok
    return blok.next
def HeadAddBlock(blok):
    blok.pre=block(blok.l)
    blok.pre.next=blok
    return blok.pre
class CustomDeque:
    def __init__(self,size=1):
        self.head=self.tail=block(size)
        self.size=size
    def append(self,value):
        if self.size==1:
            if self.tail.value==None:
                self.tail.value=value
            else:
                self.tail=TailAddBlock(self.tail)
                self.tail.value=value
        else:
            if self.tail.t==self.tail.l:
                self.tail=TailAddBlock(self.tail)
            self.tail.value[self.tail.t]=value
            self.tail.t+=1
    def appendleft(self,value):
        if self.size==1:
            if self.head.value==None:
                self.head.value=value
            else:
                self.head=HeadAddBlock(self.head)
                self.head.value=value
        else:
            if self.head.t==self.head.l:
                self.head=HeadAddBlock(self.head)
            self.head.value=[value]+self.head.value[:-1]
            self.head.t+=1
    def pop(self):
        if self.size==1:
            if self.tail.value==None:
                raise IndexError('pop from an empty q')
            tail0=self.tail.value
            self.tail.value=None
            if self.tail!=self.head:
                self.tail=self.tail.pre
                self.tail.next=None
            return tail0
        else:
            if self.tail.t==0:
                raise IndexError('pop from an empty q')
            tail0=self.tail.value[self.tail.t-1]
            self.tail.value[self.tail.t-1]=None
            self.tail.t-=1
            if self.tail.t==0 and self.tail!=self.head:
                self.tail=self.tail.pre
                self.tail.next=None
            return tail0
    def popleft(self):
        if self.size==1:
            if self.head.value==None:
                #raise IndexError('pop from an empty q')
                return
            head0=self.head.value
            self.head.value=None
            if self.tail!=self.head:
                self.head=self.head.next
                self.head.pre=None
            return head0
        else:
            if self.head.t==0:
                #raise IndexError('popleft from an empty q')
                return 
            head0=self.head.value[0]
            self.head.value=self.head.value[1:]+[None]
            self.head.t-=1
            if self.head.t==0 and self.head!=self.tail:
                self.head=self.head.pre
                self.head.next=None
            return head0
    def test(self,sep='->',end='\n',tes=True):
        if tes==True:
            print('->',end='')
        blok=self.head
        if tes==False:
            value=val(blok,sep=sep)
            if value is None or value == '':
                value='NULL'
        else:
            value=blok.value
        while True:
            if blok==self.tail:
                if tes==True:
                    print(value,end=sep+end)
                else:
                    print(value,end=end)
                break
            else:
                print(value,end=sep)
            blok=blok.next
            if not tes:
                value=val(blok,sep=sep)
            else:
                value=blok.value
    
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        a=CustomDeque()
        n=int(input())
        for __ in range(n):
            typ,x=map(int,input().split())
            if typ==1:
                a.append(x)
            else:
                if x==0:
                    a.popleft()
                else:
                    a.pop()
        a.test(tes=False,sep=' ',end='\n')




        