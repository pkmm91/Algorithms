def anagrams(s):
    if s == '':
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            for i in range(len(w)+1):
                ans.append(w[:i] + s[0] + w[i:])
        return ans
print anagrams('blue')
