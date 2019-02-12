def merge_the_tools(string, k):
    char_list = list(string)
    pointer = int(0)
    res_list = []
    for _ in range(0, int(len(char_list)/k)):
        sub_list = char_list[pointer:pointer+k]
        for i in sub_list:
            if i not in res_list:
                res_list.append(i)
        print("".join(res_list))
        res_list.clear()
        pointer = pointer + k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)