"""
ip:-
    3 4 5 6 2 1 8 7
op:-
    4
return number od prime numbers in the linked list not usage of while or for loop at all. Only using recursion
"""
d=dict()
d[1]=False
def count_prime(node,count):
    if not node:
        return count
    #check prime using recursion
    num=node.val
    def check_prime(num,i):
        if num in d:
            return d[num]
        if i==1:
            if num not in d:
                d[num]=True
            return True
        if num%i==0:
            if num not in d:
                d[num]=False
            return False
        return check_prime(num,i-1)
    if check_prime(num,num//2):
        count+=1
    return count_prime(node.next,count)

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
print(count_prime(head,0))