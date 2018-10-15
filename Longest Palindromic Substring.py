class Solution(object):
    def checkP(self,s):
        if s == s[::-1]:
            return True    
    
    def longestPalindrome(self, s):
        if len(s)==0:
            return ""
        if len(s)==1:
            return s
        max_length = 0
        lp =[]
        I =0
        J =0 
        for i in range(len(s)):
            for j in range(1,len(s)):
                if i > I and i < J and j > I and j < J:
                    j = j+1
                #s1 = s[i:j+1]
                #if s1==s1[::-1]:
                if self.checkP(s[i:j+1]):
                    if (j-i) > max_length:
                        max_length = j-i
                        lp = s[i:j+1]
                        I = i
                        J = j
                        if j==len(s):
                            break
        if lp == []:
            return s[0]
        return lp

