def LongestWord(sen):
    refined_sen = [i for i in sen if i.isalpha() or i == ' ']
    sen = ''.join(refined_sen).split()
    longest = sen[0]
    for word in sen:
        if len(word) > len(longest):
            longest = word
    return longest
print (LongestWord(input()))