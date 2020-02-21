"""
Queue implementation using a Linked List.

Output:

1  -> 2  ->
1  -> 2  -> 3  ->
1  -> 2  -> 3  -> 4  ->
1  -> 2  -> 3  -> 4  -> 5  ->
1  -> 2  -> 3  -> 4  -> 5  -> 6  ->
1  -> 2  -> 3  -> 4  -> 5  -> 6  -> 7  ->
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self, head_val):
    self.head = Node(head_val)
    self.current = self.head
  
  def insert(self, val):
    new_node = Node(val)
    self.current.next = new_node
    self.current = new_node
    self.traverse()
  
  def traverse(self):
    current = self.head
    while current is not None:
      print(current.val, ' -> ', end="")
      current = current.next
    print('\n')


if __name__ == '__main__':
  vals = [1,2,3,4,5,6,7]
  
  ll = LinkedList(vals[0])

  for v in vals[1:]:
    ll.insert(v)
  # ll.traverse()

