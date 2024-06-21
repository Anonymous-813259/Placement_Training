class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,root,data):
        if root is None:
            return node(data)
        if data<root.data:
            root.left=self.insert(root.left,data)
        else:
            root.right=self.insert(root.right,data)
        return root
    def inorder_traversal(self,root):
        if root is None:
            print("Tree is empty")
            return
        print("Inorder Traversal:")
        self.inorder_traversal2(root)
    def inorder_traversal2(self,root):
        if root:
            self.inorder_traversal2(root.left)
            print(root.data,end=" ")
            self.inorder_traversal2(root.right)
    def preorder_traversal(self,root):
        if root is None:
            print("Tree is empty")
            return
        print("Preorder Traversal:")
        self.preorder_traversal2(root)
    def preorder_traversal2(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder_traversal2(root.left)
            self.preorder_traversal2(root.right)
    def postorder_traversal(self,root):
        if root is None:
            print("Tree is empty")
            return
        print("Postorder Traversal:")
        self.postorder_traversal2(root)
    def postorder_traversal2(self,root):
        if root:
            self.postorder_traversal2(root.left)
            self.postorder_traversal2(root.right)
            print(root.data,end=" ")
    def delete(self,root,data):
        if root is None:
            print(f"{data} is not present in the tree")
            return
        if data<root.data:
            root.left=self.delete(root.left,data)
        elif data>root.data:
            root.right=self.delete(root.right,data)
        else:
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                return temp
            temp=self.find_min(root.right)
            root.data=temp.data
            root.right=self.delete(root.right,temp.data)
        return root
    def find_min(self,start):
        temp=start
        while temp.left!=None:
            temp=temp.left
        return temp
    def search(self,root,se):
        if root is None:
            print("Tree is empty")
            return
        if se==root.data:
            return True
        elif se<root.data:
            return self.search(root.left,se)
        elif se>root.data:
            return self.search(root.right,se)
        else:
            return False
obj=BST()
root=None
while 1:
    print("\n1.Insert\n2.Inorder traversal\n3.Preorder traversal\n4.Postorder traversal\n5.Delete\n6.Search\n7.Exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        data=list(map(int,input("Enter the elements:").split()))
        for i in data:
            root=obj.insert(root,i)
        print("Elements inserted successfully")
    elif ch==2:
        obj.inorder_traversal(root)
    elif ch==3:
        obj.preorder_traversal(root)
    elif ch==4:
        obj.postorder_traversal(root)
    elif ch==5:
        data=int(input("Enter the element to delete:"))
        root=obj.delete(root,data)
        print("Deletion operation completed successfully")
    elif ch==6:
        se=int(input("Enter the search element:"))
        if obj.search(root,se):
            print(f"{se} is present in the tree")
        else:
            print(f"{se} is not present in the tree")
    elif ch==7:
        print("You are exited")
        break
    else:
        print("Invalid choice")