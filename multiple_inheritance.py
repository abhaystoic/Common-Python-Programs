# Python code to demonstrate multiple inheritance

class Humans(object):
  def __init__(self):
    pass

  def call_me(self):
    print ('Called in Humans')

# first parent class
class Person(Humans):
  def __init__(self, name, idnumber):
    self.name = name
    self.idnumber = idnumber

  # def call_me(self):
  #   print ('Called in Person')

# second parent class
class Employee(object):
  def __init__(self, salary, post):
    self.salary = salary
    self.post = post

  def call_me(self):
    print ('Called in Employee')

# inheritance from both the parent classes
class Leader(Person, Employee):
  # While creating an instance of a class,
  # make sure that the sequence in which you
  # give the parameters to a function is
  # relevant to that within the block of the class.
  def __init__(self, name, idnumber, salary, post, points):
    self.points = points
    Person.__init__(self, name, idnumber)
    Employee.__init__(self, salary, post)
    self.call_me()

  # def call_me(self):
  #   print ('Called in Leader')

if __name__ == '__main__':
  obj = Leader('Abhay', 1, 2, 123, 'Engineer')
  obj.call_me()
