def verify(numbers, k):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == k:
                print(True)
                break

if __name__ == '__main__':
    numbers = list(map(float, input().split()))
    k = float(input())
    verify(numbers, k)