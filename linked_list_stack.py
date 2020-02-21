"""
Stack implementation using a Linked List.

Output:

2  -> 1  ->
3  -> 2  -> 1  ->
4  -> 3  -> 2  -> 1  ->
5  -> 4  -> 3  -> 2  -> 1  ->
6  -> 5  -> 4  -> 3  -> 2  -> 1  ->
7  -> 6  -> 5  -> 4  -> 3  -> 2  -> 1  ->
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self, head_val):
    self.head = Node(head_val)
  
  def insert(self, val):
    new_node = Node(val)
    new_node.next = self.head
    self.head = new_node
    self.traverse()
  
  def traverse(self):
    head = self.head
    while head is not None:
      print(head.val, ' -> ', end="")
      head = head.next
    print('\n')


if __name__ == '__main__':
  vals = [1,2,3,4,5,6,7]
  
  ll = LinkedList(vals[0])

  for v in vals[1:]:
    ll.insert(v)
  # ll.traverse()
