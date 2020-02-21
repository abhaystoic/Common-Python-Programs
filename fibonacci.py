def fibonacci(num):
  if num <= 1:
    return 1
  sum = 0
  while num >= 0:
    sum += num
    num -=1
  return sum



if __name__ == '__main__':
  num = int(raw_input('Enter a number to calculate fibonacci.'))
  print (fibonacci(num))