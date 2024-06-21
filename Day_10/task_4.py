"""
Printing Tree top view
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
"""def left_view(temp):
    if not temp:
        return 0
    if not temp.left:
        left_view(temp.right)
    left_view(temp.left)
    print(temp.val,end='->')
def right_view(temp):
    if not temp:
        return 0
    print(temp.val,end='->')
    if not temp.right:
        right_view(temp.left)
    right_view(temp.right)
def top_view(temp):
    left_view(temp.left)
    print(temp.val,end='->')
    right_view(temp.right)
def bottom_view(temp):
    if not temp:
        return
    if not temp.left and not temp.right:
        print(temp.val,end=' ')
    bottom_view(temp.left)
    bottom_view(temp.right)"""
left_dict=dict()
def left_view(temp,level):
    if temp==None:
        return
    if level not in left_dict:
        left_dict[level]=temp.val
    left_view(temp.left,level+1)
    left_view(temp.right,level+1)
right_dict=dict()
def right_view(temp,level):
    if temp==None:
        return
    right_dict[level]=temp.val
    right_view(temp.left,level+1)
    right_view(temp.right,level+1)
top_dict=dict()
def top_view(temp,level):
    if temp==None:
        return
    """if level not in top_dict or (level<0 and temp.val>top_dict[level]):
        top_dict[level]=temp.val"""
    if level not in top_dict:
        top_dict[level]=temp.val
    if level>=0:
        top_view(temp.left,level+1)
        top_view(temp.right,level-1)
    else:
        top_view(temp.right,level-1)
        top_view(temp.left,level+1)
bottom_dict=dict()
def bottom_view(temp,level):
    if temp==None:
        return
    """if level not in bottom_dict or (level<0 and temp.val<top_dict[level]):
        bottom_dict[level]=temp.val"""
    bottom_dict[level]=temp.val
    if level>=0:
        bottom_view(temp.left,level+1)
        bottom_view(temp.right,level-1)
    else:
        bottom_view(temp.right,level-1)
        bottom_view(temp.left,level+1)


l=list(map(int,input().split()))
root=None
for i in l:
    if not root:
        root=add_node(root,i)
    else:
        add_node(root,i)
left_view(root,0)
print("Left View:- ",list(left_dict.values()))
right_view(root,0)
print("Right View:-",list(right_dict.values()))
top_view(root,0)
print("Top View:- ",list(top_dict.values()))
bottom_view(root,0)
print("Bottom View:-",list(bottom_dict.values()))
print(bottom_dict,top_dict)
