class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,data=0):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
            return True
        self.tail.next=Node(data)
        self.tail.next.prev=self.tail
        self.tail=self.tail.next
        return True
    def addfront(self,data=0):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
            return True
        front_node=Node(data)
        front_node.next=self.head
        self.head.prev=front_node
        self.head=front_node
        return True
    def display(self):
        if self.head is None:
            return -1
        temp=self.head
        print("\nTraverse:- ",end="")
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("\b\b ",end=" ")
        print("\nReverse:- ",end="")
        temp=self.tail
        while temp:
            print(temp.data,end='->')
            temp=temp.prev
        print("\b\b ",end=' ')
        return 1
    def search(self,data=0):
        if self.head is None:
            return False
        front_temp=self.head
        back_temp=self.tail
        while front_temp.data!=data and back_temp.data!=data and front_temp!=back_temp and front_temp.next!=back_temp:
            front_temp=front_temp.next
            back_temp=back_temp.prev
        if front_temp.data==data or back_temp.data==data:
            return True
        return False
    def even_odd(self):
        if self.head is None:
            return "Zero"
        if self.head==self.tail:
            return "Odd"
        front=self.head
        back=self.tail
        while front and front.next and front!=back and front.next!=back:
            front=front.next.next
            back=back.prev.prev
        if not front or front.next==back:
            return "Even"
        return "Odd"
    def palindrome(self):
        if self.head is None:
            return False
        front=self.head
        back=self.tail
        while front.data==back.data and front!=back and front.next!=back:
            front=front.next
            back=back.prev
        if front.data==back.data:
            return True
        return False
    def rotate_middle(self):
        if self.head is None:
            return False
        fast=self.head
        slow=self.head
        pre=None
        nxt=slow.next
        while fast and fast.next:
            pre=slow
            slow=slow.next
            nxt=slow.next
            fast=fast.next.next
        #Changing Connections
        """pre.next=None
        slow.prev=None
        self.tail.next=self.head
        self.head.prev=self.tail
        self.tail=pre
        self.head=slow"""
        #Swaping data
        temp=self.head
        while slow:
            temp.data,slow.data=slow.data,temp.data
            temp=temp.next
            slow=slow.next
        return True
    
def binary_search(se,t_head,t_tail):
    if t_head==t_tail and t_head.data==se:
        return True
    elif t_head==t_tail:
        return False
    fast=t_head
    slow=t_head
    while fast!=t_tail.next and fast.next!=t_tail.next:
        slow=slow.next
        fast=fast.next.next
    if slow.data>se:
        return binary_search(se,t_head,slow.prev)
    elif slow.data<se:
        return binary_search(se,slow.next,t_tail)
    else:
        return True
    
    
dll=DLL()
l=list(map(int,input().split()))
for i in l:
    dll.addback(i)
dll.display()
print()
"""se=int(input())
print(dll.search(se))"""
#print(dll.even_odd())
#print(dll.palindrome())
dll.rotate_middle()
dll.display()
print()
"""se=int(input())
res=binary_search(se,dll.head,dll.tail)
print(res)
dll.display()"""








'''class Node:
    def __init__(self,data=0):
        self.val=data
        self.next=None
        self.prev=None
    """def asd(self):
        print("Hi",self)"""
x=Node()
#x.asd()
#Node.asd(10)'''