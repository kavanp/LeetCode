class Solution:
    def letterCombinations(self, digits):
        self.d = {'2':'abc', '3':'def', '4':'ghi', '5': 'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(self.d[digits])
        self.ans = []
        self.ans2 = ['']
        for i in self.d[digits[0]]:
            self.ans.append(i)
        
        for i in range(1,len(digits)):
            for j in range(len(self.ans)):
                for k in range(len(self.d[digits[i]])):
                    self.ans2.append(self.ans[j] + self.d[digits[i]][k])
            self.ans = self.ans2
            self.ans2 = ['']

        self.ans = list(filter(lambda x : len(x) == len(self.ans[len(self.ans)-1]) ,self.ans))
        return self.ans
