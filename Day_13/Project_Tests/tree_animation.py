import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import networkx as nx
import random

# Binary Tree Node class
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Insert function for the Binary Tree
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Function to add edges to the graph for visualization
def add_edges(graph, root):
    if root:
        if root.left:
            graph.add_edge(root.val, root.left.val)
            add_edges(graph, root.left)
        if root.right:
            graph.add_edge(root.val, root.right.val)
            add_edges(graph, root.right)

# Create initial tree
root = Node(50)
keys = [30, 70, 20, 40, 60, 80]
for key in keys:
    insert(root, key)

# Create graph for the tree
G = nx.DiGraph()
add_edges(G, root)

# Create plot
fig, ax = plt.subplots()
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, ax=ax)

# Function to update the plot
def update(frame):
    ax.clear()
    new_key = random.randint(10, 90)
    insert(root, new_key)
    G.add_node(new_key)
    add_edges(G, root)
    nx.draw(G, pos, with_labels=True, ax=ax)

# Create animation
ani = FuncAnimation(fig, update, frames=10, repeat=False)
plt.show()
