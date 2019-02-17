def verify(numbers, k):
    if(any(numbers[i]+numbers[j] == k for i in range(len(numbers)) for j in range(i+1, len(numbers)))):
        print(True)
    else:
        print(False)

if __name__ == '__main__':
    numbers = list(map(float, input().split()))
    k = float(input())
    verify(numbers, k)
