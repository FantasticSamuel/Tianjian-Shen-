from heapq import heapify,heappop,heappush

class treenode:
    def __init__(self,value=None,freq=0,left=None,right=None,minalpha=None):
        self.value=value
        self.freq=freq
        self.minalpha=minalpha
        self.left:treenode=left
        self.right:treenode=right
        self.code={}
        if value is not None:self.code[value]=''
    def __lt__(self,other):
        if self.freq==other.freq:return self.minalpha<other.minalpha
        else:return self.freq<other.freq
    def decode(self,s,i=0):
        if i==0 and self.value is not None:return len(s)*self.value,len(s)
        if self.value:return self.value,i
        dic={'0':self.left,'1':self.right}
        return dic[s[i]].decode(s,i=i+1)
    def encode(self):
        for char,code in self.left.code.items():
            self.code[char]='0'+code
        for char,code in self.right.code.items():
            self.code[char]='1'+code    
    def external_path_length(self,depth=0):
        if self.value is not None and depth==0:return self.freq
        if self.left is None and self.right is None:return depth*self.freq
        else:return self.left.external_path_length(depth=depth+1)+self.right.external_path_length(depth=depth+1)

def test(char_freq = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 8, 'f': 9, 'g': 11, 'h': 12}):
    huffman_tree = huffman_encoding(char_freq)
    external_length = huffman_tree.external_path_length()
    print("The weighted external path length of the Huffman tree is:", external_length)

def huffman_encoding(char_freq):
    q=[treenode(value=char,freq=freq,minalpha=char) for char,freq in char_freq.items()]
    heapify(q)
    if len(q)==1:q[0].code[q[0].value]='0'
    while len(q)>1:
        node_l=heappop(q)
        node_r=heappop(q)
        node=treenode(freq=node_l.freq+node_r.freq,minalpha=min(node_l.minalpha,node_r.minalpha))
        node.left=node_l
        node.right=node_r
        node.encode()
        heappush(q,node)
    return q[0]

def decode(s,huffman_tree):
    i=0
    ans=''
    while i<len(s):
        val,i_=huffman_tree.decode(s,i=i)
        ans+=val
        i=i_
    return ans

def main():
    n=int(input())
    char_freq={}
    for _ in range(n):
        char,freq=input().split()
        char_freq[char]=int(freq)
    huffman_tree = huffman_encoding(char_freq)
    while True:
        try:
            s=input()
            if s[0] in '01':print(decode(s,huffman_tree))
            else:
                for ch in s:print(huffman_tree.code[ch],end='')
                print()
        except EOFError:
            break

if __name__ == "__main__":
    main()
