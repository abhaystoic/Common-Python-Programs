"""
There is a list of sorted integers from 1 to n. Starting from left to right,
remove the first number and every other number afterward until you reach the
end of the list.
Repeat the previous step again, but this time from right to left, remove the
right most number and every other number from the remaining numbers.
We keep repeating the steps again, alternating left to right and right to left,
until a single number remains.
Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
"""

class Solution:

  def lastRemaining(self, n: int) -> int:
    if n <= 0:
      raise ValueError('The input is invalid')

    left = True
    remaining = n
    head = 1
    step = 1

    while remaining > 1:
      if left or remaining % 2 == 1:
        head += step

      remaining //= 2
      step *= 2
      left = not left

    return head

# def __name__ == '__main__':
n = 24
for i in range(1, 50):
  print (i , ":  ", Solution().lastRemaining(i))