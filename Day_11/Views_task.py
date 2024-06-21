"""
Tree Views only top and bottom views
"""
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def add_node(temp,val):
    if temp is None:
        node=Node(val)
        #print(val,"added")
        return node
    if temp.val<val:
        if not temp.right:
            temp.right=add_node(temp.right,val)
        else:
            add_node(temp.right,val)
    elif temp.val>val:
        if not temp.left:
            temp.left=add_node(temp.left,val)
        else:
            add_node(temp.left,val)
top_dict=dict()
def top_view(temp,level,depth):
    if not temp:
        return
    if (level not in top_dict) or (depth<top_dict[level][1]):
        top_dict[level]=[temp.val,depth]
    top_view(temp.left,level+1,depth+1)
    top_view(temp.right,level-1,depth+1)
bottom_dict=dict()
def bottom_view(temp,level,depth):
    if not temp:
        return
    if (level not in bottom_dict) or (depth>=bottom_dict[level][1]):
        bottom_dict[level]=[temp.val,depth]
    bottom_view(temp.left,level+1,depth+1)
    bottom_view(temp.right,level-1,depth+1)
def top_view_bfs(queue,d):
    while queue:
        node=queue[0][0]
        if node.left:
            queue.append([node.left,queue[0][1]+1])
        if node.right:
            queue.append([node.right,queue[0][1]+1])
        if queue[0][1] not in d:
            d[queue[0][1]]=queue[0][0].val
        queue.pop(0)
    return d.values()
def bottom_view_bfs(queue,d):
    while queue:
        node=queue[0][0]
        if node.left:
            queue.append([node.left,queue[0][1]-1])
        if node.right:
            queue.append([node.right,queue[0][1]+1])
        d[queue[0][1]]=queue[0][0].val
        queue.pop(0)
    return d.values()

l=list(map(int,input().split()))
root=None
for i in l:
    if not root:
        root=add_node(root,i)
    else:
        add_node(root,i)
#top_view(root,0,0)
#top_values=[top_dict[i][0] for i in top_dict]
#print("Top View:-",top_values)
#bottom_view(root,0,0)
#bottom_values=[bottom_dict[i][0] for i in bottom_dict]
#print("Bottom View:-",bottom_values)
#print("Top View:-",top_view_bfs([[root,0],],{}))
print("Bottom View:-",bottom_view_bfs([[root,0],],{}))