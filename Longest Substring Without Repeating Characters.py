class Solution:
    def lengthOfLongestSubstring(self, s):
        s2 = []
        l = 0
        for i in range(len(s)):
            if s[i] not in s2:
                s2.append(s[i])
                if len(s2) > l:
                    l = len(s2)
            else:
                #l = len(s2)
                s2 = s2[s2.index(s[i])+1:]
                s2.append(s[i])
        return l
