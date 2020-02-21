class Base:
  __slots__ = ('foo', 'bar')

class Right(Base):
  __slots__ = ('baz',)

class Wrong(Right):
  __slots__ = ('test')

  def __init__(self):
    # Even if we declare a member variable,
    # it will throw error and it is not mentioned in __slots__
    self.temp = 'test'

if __name__ == '__main__':
  print(Wrong().temp)
