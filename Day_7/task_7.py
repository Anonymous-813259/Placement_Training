"""
Trees Concept
"""
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def addNode(val,temp):
    if temp is None:
        temp=Node(val)
        return None
    if temp.val