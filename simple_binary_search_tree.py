"""Simple Binary Search Tree"""

class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

class Tree:
  def __init__(self, val):
    self.root = Node(val)
    self.tree_list = []
  
  def insert(self, node, val):

    if val <= node.data:
      if node.left is None:
        node.left = Node(val)
      else:
        self.insert(node.left, val)
    else:
      if node.right is None:
        node.right = Node(val)
      else:
        self.insert(node.right, val)
  
  def printInorder(self, node):
    if(node is not None):
      self.printInorder(node.left)
      print(node.data)
      self.tree_list.append(node.data)
      self.printInorder(node.right)

if __name__ == '__main__':
  tree = Tree(1)
  tree.insert(tree.root, 2)
  tree.insert(tree.root, 3)
  tree.insert(tree.root, 4)
  tree.insert(tree.root, 5)
  tree.printInorder(tree.root)
  print (tree.tree_list)
