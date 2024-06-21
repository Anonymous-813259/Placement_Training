"""
dll use recursion add all even numbers and odd numbers separately
return the difference of those two
"""
def even_odd_diff(head,es,os):
    if not head:
        return abs(es-os)
    if head.val%2==0:
        return even_odd_diff(head.next,es+head.val,os)
    return even_odd_diff(head.next,es,os+head.val)


class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

l=list(map(int,input().split()))
head=Node(l[0])
temp=head
pre=None
for i in range(1,len(l)):
    pre=temp
    temp.next=Node(l[i])
    temp=temp.next
    temp.prev=pre
print(even_odd_diff(head,0,0))