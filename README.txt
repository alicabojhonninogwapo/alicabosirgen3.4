ASSESSMENT 3.3: NON-LINEAR DATA STRUCTURE
Last Name: ALICABO
Programming Language: Python 3

FILES
1. binary_tree/binary_tree_alicabo.py
2. graph/graph_alicabo.py

REQUIREMENTS
- Python 3 installed on your computer.
- No extra Python libraries are required.

HOW TO RUN
Open a terminal in the extracted folder.

Run the Binary Tree program:
    python binary_tree/binary_tree_alicabo.py

Run the Graph program:
    python graph/graph_alicabo.py

On some Windows computers, use:
    py binary_tree/binary_tree_alicabo.py
    py graph/graph_alicabo.py

EXPECTED OUTPUT: BINARY TREE
BINARY TREE - ALICABO
BFS (level order): A - L - I - C - A2 - B - O
DFS (preorder): A - L - C - A2 - I - B - O

EXPECTED OUTPUT: GRAPH
GRAPH - ALICABO
Vertices: A1, L, I, C, A2, B, O
Edges: A1-L, A1-I, L-C, L-A2, I-B, I-O, C-B, A2-O
BFS: A1 - L - I - C - A2 - B - O
DFS: A1 - L - C - B - I - O - A2

TRAVERSAL EXPLANATION
- BFS (Breadth-First Search) visits nodes level by level or visits
  nearby connected nodes first. It uses a queue.
- DFS (Depth-First Search) follows one path as far as possible before
  going back to explore another path.
- The binary tree DFS uses preorder: visit the current node, then the
  left subtree, then the right subtree.
- The graph is undirected. Neighbor order is the order shown in the
  graph dictionary. A1 and A2 represent the two A letters.

The two Python programs are separate. Run each file independently.
