import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Node{
    int value;
    Node left;
    Node right;
    Node(int value){
        this.value=value;
        this.left=null;
        this.right=null;
    }
}

class Tree{
    Node root;
    Tree(){
        this.root=null;
    }
    Node addNode(Node temp,int value){
        if(temp!=null && value<temp.value){
            if(temp.left==null){
                temp.left=addNode(temp.left, value);
            }
            else{
                addNode(temp.left, value);
            }
        }
        else if(temp!=null && value>temp.value){
            if(temp.right==null){
                temp.right=addNode(temp.right, value);
            }
            else{
                addNode(temp.right, value);
            }
        }
        return new Node(value);
    }
    void inOrder(Node temp){
        if(temp!=null){
            inOrder(temp.left);
            System.out.print(temp.value+"->");
            inOrder(temp.right);
        }
    }
    void preOrder(Node temp){
        if(temp!=null){
            System.out.print(temp.value+"->");
            preOrder(temp.left);
            preOrder(temp.right);
        }
    }
    void postOrder(Node temp){
        if(temp!=null){
            postOrder(temp.left);
            postOrder(temp.right);
            System.out.print(temp.value+"->");
        }
    }
    int addAllNodes(Node temp){
        if(temp==null){
            return 0;
        }
        return addAllNodes(temp.left)+addAllNodes(temp.right)+temp.value;
    }
    int addAllEvenNodes(Node temp){
        if(temp==null){
            return 0;
        }
        if(temp.value%2==0){
            return addAllEvenNodes(temp.left)+addAllEvenNodes(temp.right)+temp.value;
        }
        return addAllEvenNodes(temp.left)+addAllEvenNodes(temp.right);
    }
    int addAllOddNodes(Node temp){
        if(temp==null){
            return 0;
        }
        if(temp.value%2==0){
            return addAllOddNodes(temp.left)+addAllOddNodes(temp.right);
        }
        return addAllOddNodes(temp.left)+addAllOddNodes(temp.right)+temp.value;
    }
    int absDiffEvenOdd(Node temp){
        if(temp==null){
            return 0;
        }
        if(temp.value%2==0){
            return absDiffEvenOdd(temp.left)+absDiffEvenOdd(temp.right)+temp.value;
        }
        return absDiffEvenOdd(temp.left)+absDiffEvenOdd(temp.right)-temp.value;
    }
    int nodeHeight(Node temp){
        if(temp==null){
            return -1;
        }
        return Math.max(nodeHeight(temp.left)+1, nodeHeight(temp.right)+1);
    }
    boolean checkBalance(Node temp){
        return Math.abs(nodeHeight(temp.left)-nodeHeight(temp.right))<=1;
    }
    int leafNodeCount(Node temp){
        if(temp==null){
            return 0;
        }
        else if(temp.left==null && temp.right==null){
            return 1;
        }
        return leafNodeCount(temp.left)+leafNodeCount(temp.right);
    }
    int addLeafNodes(Node temp){
        if(temp==null){
            return 0;
        }
        else if(temp.left==null && temp.right==null){
            return temp.value;
        }
        return addLeafNodes(temp.left)+addLeafNodes(temp.right);
    }
    boolean searchTree(Node temp,int value){
        if(temp==null){
            return false;
        }
        else if(value<temp.value){
            return searchTree(temp.left, value);
        }
        else if(value>temp.value){
            return searchTree(temp.right, value);
        }
        return true;
    }
    int nodeDepth(Node temp, int value,int depth){
        if(temp==null){
            return -1;
        }
        else if(value<temp.value){
            return nodeDepth(temp.left, value, depth+1);
        }
        else if(value>temp.value){
            return nodeDepth(temp.right, value, depth+1);
        }
        return depth;
    }
}

public class Practice {
    public static void main(String[] args) throws IOException {
        System.out.print("Enter numbers to add in tree:- ");
        BufferedReader read=new BufferedReader(new InputStreamReader(System.in));
        String[] integerLine=(read.readLine()).split((" "));
        int[] numbers=new int[integerLine.length];
        Tree bst=new Tree();
        for(int i=0;i<integerLine.length;i++){
            numbers[i]=Integer.parseInt(integerLine[i]);
        }
        for(int i=0;i<numbers.length;i++){
            if(bst.root==null){
                bst.root=bst.addNode(bst.root, numbers[i]);
            }
            else{
                bst.addNode(bst.root, numbers[i]);
            }
        }
        System.out.print("InOrder Traversal:- ");
        bst.inOrder(bst.root);
        System.out.print("\b\b  \n");
        System.out.print("PreOrder Traversal:- ");
        bst.preOrder(bst.root);
        System.out.print("\b\b  \n");
        System.out.print("PostOrder Traversak:- ");
        bst.postOrder(bst.root);
        System.out.print("\b\b  \n");
        System.out.println();
        System.out.println("Sum of all Nodes:- "+bst.addAllNodes(bst.root));
        System.out.println("Sum of all Even Nodes:- "+bst.addAllEvenNodes(bst.root));
        System.out.println("Sum of all Odd Nodes:- "+bst.addAllOddNodes(bst.root));
        System.out.println("Absolute Difference between Even and Odd:- "+Math.abs(bst.absDiffEvenOdd(bst.root)));
        System.out.println("Height of Tree:- "+bst.nodeHeight(bst.root));
        System.out.println("Balanced Tree:- "+bst.checkBalance(bst.root));
        System.out.println("Number of Leaf Nodes:- "+bst.leafNodeCount(bst.root));
        System.out.println("Sum of all Leaf Nodes:- "+bst.addLeafNodes(bst.root));
        System.out.print("Enter Search Element:- ");
        int n=Integer.parseInt(read.readLine());
        System.out.println("Search for "+n+":- "+bst.searchTree(bst.root, n));
        System.out.println("Depth of Node "+n+":- "+bst.nodeDepth(bst.root, n, 0));
    }
}