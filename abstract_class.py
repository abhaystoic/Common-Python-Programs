import abc

class Shape(object):
  __metaclass__ = abc.ABCMeta

  # In Python 3 -
  # class Shape(metaclass=abc.ABCMeta):

  @abc.abstractmethod
  def __init__(self):
    pass

  @abc.abstractmethod
  def method_to_implement(self, inp):
    raise NotImplementedError #Uncomment to force Parent class to implement it.
    return 'New {}'.format(inp)

class MyClass(Shape):

  def __repr__(self):
    return "My Class's object."

  # Hidden member of MyClass
  __hiddenVariable = 0

  # A member method that changes
  # __hiddenVariable
  def add(self, increment):
    self.__hiddenVariable += increment
    print (self.__hiddenVariable, self.method_to_implement('Hello!'))

if __name__ == '__main__':
  # Driver code
  myObject = MyClass()

  # Calls __repr__.
  print (myObject)

  myObject.add(2)
  myObject.add(5)

  # We can still access private members.
  print(myObject._MyClass__hiddenVariable)

  # This line causes error
  print (myObject.__hiddenVariable)
