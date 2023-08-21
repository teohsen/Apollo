def cancontruct(word, wordlist, memo={}):
    if word in memo:
        return memo[word]
    if word == '':
        return True

    for i in wordlist:
        if word.startswith(i):
            wordleft = "".join(word.split(i, 1))
            if cancontruct(wordleft, wordlist, memo) is True:
                memo[word] = True
                return True

    memo[word] = False
    return False


# m = target length
# n = wordbank length

print(cancontruct("abcdef", ["ab", "abc", "cd",
                             "def", "abcd"]))

print(cancontruct("skateboard",
                  ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))

print(cancontruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eeee"]))