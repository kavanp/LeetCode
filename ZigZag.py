class Solution:
    def convert(self, s, numRows):
        if numRows==1:
            return s
        if numRows > len(s):
            return s
        l = len(s)
        l = int(l/2)
        a = [[0]*len(s) for i in range(numRows)]
        i=0
        j=0
        goingdown = 1
        result = []
        for k in range(len(s)):
            if goingdown == 1:
                a[i][j] = s[k]
                #print (a[i][j],k,i,j)
                i = i+1
                if i == numRows:
                    i = i-1
                    goingdown = 0
                    continue;
            if goingdown == 0:
                i = i-1
                j = j+1
                a[i][j] = s[k]
                #print (a[i][j],k,i,j)
                if i == 0:
                    i = i+1
                    goingdown = 1
                    continue;
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j]!=0:
                    result.append(a[i][j])
        result = "".join(str(x) for x in result)
        return result
                
