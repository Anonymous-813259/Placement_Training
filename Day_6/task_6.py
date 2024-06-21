"""
ip:-
    take string from user, that string will have only parenthesis
op:-
    check whether it is balanced or not and in double linked list concept
    if balance return -1
    else return the position of the index
"""
def rec_fun(stack,node,ind):
    if not node and not stack:
        return -1
    elif not node and stack:
        return ind
    elif node.val=='[':
        stack.append(']')
        return rec_fun(stack,node.next,ind+1)
    elif node.val=="{":
        stack.append('}')
        return rec_fun(stack,node.next,ind+1)
    elif node.val=="(":
        stack.append(")")
        return rec_fun(stack,node.next,ind+1)
    elif stack:
        if stack[-1]==node.val:
            stack.pop()
            return rec_fun(stack,node.next,ind+1)
        else:
            return ind
    else:
        return ind
    
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

s=input()
head=Node(s[0])
temp=head
pre=None
for i in range(1,len(s)):
    pre=temp
    temp.next=Node(s[i])
    temp=temp.next
    temp.prev=pre
print(rec_fun([],head,1))
