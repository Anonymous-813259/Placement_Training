class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def add_node(temp,val):
    if temp is None:
        node=Node(val)
        print(val,"added")
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
def inoder(temp):
    if temp:
        inoder(temp.left)
        print(temp.val,end='->')
        inoder(temp.right)
def preoder(temp):
    if temp:
        print(temp.val,end='->')
        preoder(temp.left)
        preoder(temp.right)
def postorder(temp):
    if temp:
        postorder(temp.left)
        postorder(temp.right)
        print(temp.val,end="->")
def all_node_sum(temp):
    if not temp:
        return 0
    return all_node_sum(temp.left)+all_node_sum(temp.right)+temp.val
def all_even_sum(temp):
    if not temp:
        return 0
    if temp.val%2==0:
        return all_even_sum(temp.left)+all_even_sum(temp.right)+temp.val
    return all_even_sum(temp.left)+all_even_sum(temp.right)
def all_odd_sum(temp):
    if not temp:
        return 0
    if temp.val%2!=0:
        return all_odd_sum(temp.left)+all_odd_sum(temp.right)+temp.val
    return all_odd_sum(temp.left)+all_odd_sum(temp.right)
def abs_even_odd(temp):
    if not temp:
        return 0
    if temp.val%2==0:
        return abs_even_odd(temp.left)+abs_even_odd(temp.right)+temp.val
    return abs_even_odd(temp.left)+abs_even_odd(temp.right)-temp.val
def find_height(temp,height):
    if not temp:
        return height-1
    return max(find_height(temp.left,height+1),find_height(temp.right,height+1))
def height(temp):#sir code
    if not temp:
        return -1
    return max(height(temp.left)+1,height(temp.right)+1)
def check_balance(temp):
    return abs(find_height(temp.left,0)-find_height(temp.right,0))<=1
def count_leaf_nodes(temp):
    if not temp:
        return 0
    if not temp.left and not temp.right:
        return 1
    return count_leaf_nodes(temp.left)+count_leaf_nodes(temp.right)
def add_all_leaf_nodes(temp):
    if not temp:
        return 0
    if not temp.left and not temp.right:
        return temp.val
    return add_all_leaf_nodes(temp.left)+add_all_leaf_nodes(temp.right)
def search(temp,val):
    if temp is None:
        return False
    elif temp.val==val:
        return True
    elif val<temp.val:
        return search(temp.left,val)
    elif val>temp.val:
        return search(temp.right,val)
def node_depth(temp,val,depth):
    if temp is None:
        return False
    elif temp.val==val:
        return depth
    elif val<temp.val:
        return node_depth(temp.left,val,depth+1)
    else:
        return node_depth(temp.right,val,depth+1)

l=list(map(int,input().split()))
root=None
for i in l:
    if not root:
        root=add_node(root,i)
    else:
        add_node(root,i)
print("Inorder Traversal:- ",end=" ")
inoder(root)
print("\b\b ",end=' ')
print("\nPreorder Traversal:- ",end='')
preoder(root)
print("\b\b ",end=' ')
print("\nPostorder Traversal:- ",end='')
postorder(root)
print('\b\b ',end=' ')
print()

print("Sum of all the nodes:-",all_node_sum(root))
print("Sum of all the even nodes:-",all_even_sum(root))
print("Sum of all the odd nodes:-",all_odd_sum(root))
print("Absolute difference:-",abs(abs_even_odd(root)))
print("Height:-",find_height(root,0))
print("Balanced:-",check_balance(root))
print("Leaf Nodes:-",count_leaf_nodes(root))
print("All Leaf Nodes Addition:-",add_all_leaf_nodes(root))
n=int(input("Enter Search Element:-"))
print("Search of "+str(n)+":-",search(root,n))
print("Depth of "+str(n)+":-",node_depth(root,n,0))