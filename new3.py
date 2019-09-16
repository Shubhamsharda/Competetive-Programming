from binarytree import tree
from binarytree import Node

root = Node('jchsjcbs')
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
print(root)