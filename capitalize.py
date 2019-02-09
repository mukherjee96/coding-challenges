def solve(s):
    word_list = s.split(" ")
    for i in range(len(word_list)):
        if len(word_list[i])>0 and word_list[i][0].isalpha() and word_list[i][0].islower():
            word_list[i] = word_list[i].capitalize()
    s = " ".join(word_list)
    return s

if __name__ == "__main__":
    s = input()
    print(solve(s))
