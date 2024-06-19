class treenode:
    def __init__(self):
        self.son={}
        self.cnt=0
class tree:
    def __init__(self):
        self.root=treenode()
    def walk(self,s,add=False):
        p=self.root
        for ch in s:
            if ch not in p.son:
                if add==True:p.son[ch]=treenode()
                else:return False
            p=p.son[ch]
        if add==True:p.cnt+=1;return p
        else:
            if p.cnt==0:return False
            else:return p
    def insert(self,s):
        self.walk(s,add=True)
    def search(self,s):
        p=self.walk(s)
        if p==False:return p
        else:return p.cnt
    def delete(self,s):
        p=self.walk(s)
        if p==False:return p
        else:p.cnt-=1;return True
# def main():
#     # 创建一个tree对象
#     t = tree()

#     # 插入一些单词
#     words_to_insert = ["apple", "banana", "cherry", "date", "elderberry"]
#     for word in words_to_insert:
#         t.insert(word)

#     # 搜索一些单词
#     words_to_search = ["apple", "cherry", "fig", "elderberry", "grape"]
#     for word in words_to_search:
#         result = t.search(word)
#         print(f"Search for {word}: {'Found' if result else 'Not Found'}")

#     # 删除一些单词
#     words_to_delete = ["banana", "date", "grape"]
#     for word in words_to_delete:
#         result = t.delete(word)
#         print(f"Delete {word}: {'Success' if result else 'Fail'}")

#     # 再次搜索所有单词
#     for word in words_to_search:
#         result = t.search(word)
#         print(f"Search for {word} after deletion: {'Found' if result else 'Not Found'}")

# if __name__ == "__main__":
#     main()
    