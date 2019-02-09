import string

def print_rangoli(size):
    width = 4*size - 3
    counter = int(0)
    letters = list(reversed(string.ascii_lowercase[:size]))
    pattern = []

    for i in range(1, (2*size)):
        if(int(i) <= size):
            counter = counter + 1
            pattern = list("".join(letter + '-' for letter in letters[:counter]))
            pattern = pattern[:(counter*2)-1] + list(reversed(pattern[:(counter*2)-2]))
            line = "".join(pattern)
            print(line.center(width, "-"))
            pattern.clear()
        else:
            counter = counter - 1
            pattern = list("".join(letter + '-' for letter in letters[:counter]))
            pattern = pattern[:(counter*2)-1] + list(reversed(pattern[:(counter*2)-2]))
            line = "".join(pattern)
            print(line.center(width, "-"))
            pattern.clear()

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
