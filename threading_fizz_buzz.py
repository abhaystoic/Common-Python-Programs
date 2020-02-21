"""
Write a program that outputs the string representation of numbers
from 1 to n, however:

If the number is divisible by 3, output "fizz".
If the number is divisible by 5, output "buzz".
If the number is divisible by both 3 and 5, output "fizzbuzz".
For example, for n = 15,
we output:
1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz.

Suppose you are given the following code:

class FizzBuzz {
  public FizzBuzz(int n) { ... }               // constructor
  public void fizz(printFizz) { ... }          // only output "fizz"
  public void buzz(printBuzz) { ... }          // only output "buzz"
  public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
  public void number(printNumber) { ... }      // only output the numbers
}
Implement a multithreaded version of FizzBuzz with four threads.
The same instance of FizzBuzz will be passed to four different threads:

Thread A will call fizz() to check for divisibility of 3 and outputs fizz.
Thread B will call buzz() to check for divisibility of 5 and outputs buzz.
Thread C will call fizzbuzz() to check for divisibility of 3 and 5 and outputs
fizzbuzz.
Thread D will call number() which should only output the numbers.

"""

import threading

class FizzBuzz(object):
  def __init__(self, n):
    self.n = n
    self.done = False
    self.fz = threading.Lock()
    self.bz = threading.Lock()
    self.fzbz = threading.Lock()
    self.num = threading.Lock()
    self.fz.acquire()
    self.bz.acquire()
    self.fzbz.acquire()

  # printFizz() outputs "fizz"
  def fizz(self, printFizz):
    """
    :type printFizz: method
    :rtype: void
    """
    while True:
      self.fz.acquire()
      if self.done: break
      printFizz()
      self.num.release()

  # printBuzz() outputs "buzz"
  def buzz(self, printBuzz):
    """
    :type printBuzz: method
    :rtype: void
    """
    while True:
      self.bz.acquire()
      if self.done: break
      printBuzz()
      self.num.release()

  # printFizzBuzz() outputs "fizzbuzz"
  def fizzbuzz(self, printFizzBuzz):
    """
    :type printFizzBuzz: method
    :rtype: void
    """
    while True:
      self.fzbz.acquire()
      if self.done: break
      printFizzBuzz()
      self.num.release()

  # printNumber(x) outputs "x", where x is an integer.
  def number(self, printNumber):
    """
    :type printNumber: method
    :rtype: void
    """
    for x in range(1, self.n + 1):
      self.num.acquire()
      if x % 15 == 0:
        self.fzbz.release()
      elif x % 3 == 0:
        self.fz.release()
      elif x % 5 == 0:
        self.bz.release()
      else:
        printNumber(x)
        self.num.release()
    self.num.acquire()
    self.done = True
    self.fz.release()
    self.bz.release()
    self.fzbz.release()

if __name__ == '__main__':
  # n = 15
  # fb_obj = FizzBuzz()
