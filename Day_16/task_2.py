"""
Implementing Tries Data Structures
"""
class Trie:
    def __init__(self,end=False,level=0):
        self.d={}
        self.end=end
        self.level=level

def insert(trie,word,i,level):
    if i==len(word):
        trie.end=True
        return
    trie.level=level
    if word[i] not in trie.d:
        trie.d[word[i]]=Trie(level=level)
    insert(trie.d[word[i]],word,i+1,level+1)
l=["",0]
def display(trie):
    for i in trie.d:
        display(trie.d[i])
    print(trie.d,trie.level)
def search(trie,pre,i):
    if i==len(pre):
        fill(trie,pre)
        return
    if pre[i] in trie.d:
        search(trie.d[pre[i]],pre,i+1)
    else:
        return
def fill(head,s):
    if head.end==1 and l[1]<=head.level and (l[0]>s or l[0]==""):
        l[0]=s
        l[1]=head.level
    for i in head.d:
        fill(head.d[i],s+i)

#word="word"
head=Trie()
#insert(head,word,0)
#display(head)
#word="words"
#insert(head,word,0)
#print()
#display(head)
#print()
#word="world"
#insert(head,word,0)
#display(head)
"""insert(head,"words",0,0)
insert(head,"world",0,0)
insert(head,"worlds",0,0)
insert(head,"word",0,0)
insert(head,"wrong",0,0)
insert(head,"wong",0,0)
insert(head,"praneeth",0,0)
insert(head,"nithin",0,0)
insert(head,"poorna",0,0)"""
insert(head,"words",0,0)
insert(head,"world",0,0)
insert(head,"woods",0,0)
insert(head,"words",0,0)
insert(head,"apple",0,0)
insert(head,"apricote",0,0)
#display(head)
pre_l=["b","ba","wo","ap"]
for i in pre_l:
    search(head,i,0)
print(l[0])