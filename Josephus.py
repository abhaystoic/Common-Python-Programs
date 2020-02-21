#!/bin/python
"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
[1, 2, 3]
[1, 3]
[3]
n = 3, ans = 3

[1, 2, 3, 4]
[1, 3]
[1]
n = 4, ans = 1

[1, 2, 3, 4, 5]
[1, 3, 5]
[3]
n = 5, ans = 3

[1, 2, 3, 4, 5, 6]
[1, 3, 5]
[5]
n = 6, ans = 5

[1, 2, 3, 4, 5, 6, 7]
[1, 3, 5, 7]
[3, 7]
[7]
n = 7, ans = 7
"""

def josephus(n, kill_first=False):
  """

  :param n:
  :param kill_first:
  :return:
  """
  # print (n, kill_first)
  l = len(n)
  if kill_first:
    start = 1
    if l == 2:
      return [n[1]]
  else:
    start = 0
    if l == 2:
      return [n[0]]

  i = start
  res = []
  for i in range(start, l, 2):
    res.append(n[i])
  if i == l-1:
    kill_first_next = True
  else:
    kill_first_next = False
  if len(res) > 1:
    return josephus(res, kill_first_next)
  return res


def josephus2(n, k):
  """

  :param n: total number of prisoners.
  :param k: killing pattern (killing sequence).
  :return:
  """
  if (n == 1):
    return 1
  else:
    # The position returned by
    # josephus(n - 1, k) is adjusted
    # because the recursive call
    # josephus(n - 1, k) considers
    # the original position
    # k%n + 1 as position 1
    return (josephus2(n - 1, k) + k-1) % n + 1

def josephus3(n, k):
  """

  :param n: total number of prisoners.
  :param k: killing pattern (killing sequence).
  :return:
  """
  r = 0
  for i in range(1, n+1):
    r = (r+k)%i
  return r

if __name__ == '__main__':
  # print (tuple([x for x in map(int, input().split())]))
  # for i in range(300, 1000):
  #   try:
  #     if josephus([x for x in range(i)])[0] + 1 != josephus2(i, 2):
  #       print ('Failed for i=', i)
  #   except:
  #     print ('Timed out for i=', i)

  i = 998
  # if josephus([x for x in range(i)])[0] + 1 != josephus2(i, 2):
  #   print ('Failed for i=', i)

  # print (josephus([x for x in range(i)])[0] + 1)
  # print (josephus2(i, 2))
  print (josephus3(i, 2) + 1)

































