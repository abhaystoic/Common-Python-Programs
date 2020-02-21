# Python program to demonstrate error if we
# forget to invoke __init__() of parent.

class A:
  def __init__(self, n = 'Rahul'):
      self.name = n
class B(A):
  def __init__(self, roll):
      self.roll = roll

object = B(23)
print (object.name)
