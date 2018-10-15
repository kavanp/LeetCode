class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        maxa = 0
        while i < j:
            if maxa < ((j+1)*(i+1)*height[i]*height[j]):
                maxa = (j+1)*(i+1)*height[i]*height[j]
            if height[i] < height[j]:
                i = i+1
            else:
                j = j-1
        return maxa
