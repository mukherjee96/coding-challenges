# Given an array of integers, return a new array 
# such that each element at index i of the new 
# array is the product of all the numbers in 
# the original array except the one at i.

# Input => [1, 2, 3, 4, 5] | output => [120, 60, 40, 30, 24]
# input => [3, 2, 1] | output => [2, 3, 6]

def multiply(inList):
 outList = []
 for i in range(len(inList)):
  counter = int(1)
  product = int(1)
  j = i + 1
  while(counter<len(inList)):
   if j > len(inList)-1:
    j = 0
   product *= inList[j]
   j += 1
   counter += 1
  outList.append(product)
 print(outList)

if __name__ == '__main__':
 inList = list(map(int, input().split()))
 multiply(inList)