from heapq import heapify,heappop,heappush

class treenode:
    def __init__(self,value=None,freq=0,left=None,right=None):
        self.value=value
        self.freq=freq
        self.left=left
        self.right=right
    def __lt__(self,other):
        return self.freq<other.freq

def huffman_encoding(char_freq):
    q=[treenode(value=char,freq=freq) for char,freq in char_freq.items()]
    heapify(q)
    while len(q)>1:
        node_l=heappop(q)
        node_r=heappop(q)
        node=treenode(freq=node_l.freq+node_r.freq)
        node.left=node_l
        node.right=node_r
        heappush(q,node)
    return q[0]

def external_path_length(huffman_tree,depth=0):
    if huffman_tree.left is None and huffman_tree.right is None:return depth*huffman_tree.freq
    else:return external_path_length(huffman_tree.left,depth=depth+1)+external_path_length(huffman_tree.right,depth=depth+1)

def main():
    char_freq = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 8, 'f': 9, 'g': 11, 'h': 12}
    huffman_tree = huffman_encoding(char_freq)
    external_length = external_path_length(huffman_tree)
    print("The weighted external path length of the Huffman tree is:", external_length)

if __name__ == "__main__":
    main()

