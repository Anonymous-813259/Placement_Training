"""
ip:-
    always double linked list is even
    5 7 8 2 1 4
op:-
    7 5 2 8 4 1
"""
def swap_interbetween_link(self):
    temp1=self.head
    temp2=self.head.next
    pre=None
    nxt=temp2.next
    self.head=temp2
    while True:
        temp1.next=temp2.next
        temp2.prev=temp1.prev
        if pre:
            pre.next=temp2
        if nxt:
            nxt.prev=temp1
        temp1.prev=temp2
        temp2.next=temp1
        pre=temp1
        if not nxt:
            break
        temp1=nxt
        temp2=temp1.next
        nxt=temp2.next
    self.tail=temp1
    return True
