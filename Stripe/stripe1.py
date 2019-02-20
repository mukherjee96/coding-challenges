# Find the lowest positive integer that does 
# not exist in the array. 
# The array can contain duplicates and negative 
# numbers as well.

# input [3, 4, -1, 1] should give 2. 
# The input [1, 2, 0] should give 3.


def find(numSet):
    for i in range(1, int(max(numSet))+2):
        if i not in numSet:
            print(i)
            return

if __name__ == '__main__':
    find(set(map(int, input().split())))
