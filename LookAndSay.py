class LookAndSay(object):

  def __init__(self):
    print ('1')
    self.seq = '1'

  def look_and_say(self, n):
    count = 1
    res = []
    for j in range(1, len(self.seq)):
      if self.seq[j-1] == self.seq[j]:
        count += 1
      else:
        res.append(str(count) + self.seq[j-1])
        count = 1
    res.append(str(count) + self.seq[-1])
    self.seq = ''.join(res)
    print (self.seq)


if __name__ == "__main__":
  n = 10
  lns = LookAndSay()
  for i in range(n-1):
    lns.look_and_say(i)