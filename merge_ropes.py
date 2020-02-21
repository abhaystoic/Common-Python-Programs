# https://aonecode.com/amazon-online-assessment-oa2-connect-ropes
# Given n ropes of different lengths, you need to connect these ropes into one rope. You can connect only 2 ropes at a time. The cost required to connect 2 ropes is equal to sum of their lengths. The length of this connected rope is also equal to the sum of their lengths. This process is repeated until n ropes are connected into a single rope. Find the min possible cost required to connect all ropes.

# Input
# ropes, an int arrary representing the rope length.

# Output
# Return the min possible cost required to connect all ropes.

# Examples 1
# Input:
# ropes = [8, 4, 6, 12]

# Output:
# 58

import bisect

def connectRopes(ropes):
  if not ropes:
      return 0
  cost = 0
  ropes.sort()
  while len(ropes) > 1:
    new_rope = ropes[0] + ropes[1]
    cost += new_rope
    ropes = ropes[2:]
    bisect.insort(ropes, new_rope)
  return cost

if __name__ == '__main__':
  ropes = input()
  print (connectRopes(ropes))
