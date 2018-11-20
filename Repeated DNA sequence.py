from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s):
        l = len(s)
        result = []
        d = defaultdict(int)
        for i in range(l-9):
            sub = s[i:i+10]
            d[sub] += 1
            
        for i,j in d.items():
            if j > 1:
                result.append(i)
        return result
