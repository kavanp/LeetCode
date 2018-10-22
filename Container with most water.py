class Solution:
    def maxArea(self,height):
        i = 0
        j = len(height) - 1
        maxarea = 0
        while i < j:
            maxarea = max(min(height[i],height[j]) * (j - i),maxarea)
            if (height[i] < height[j]):
                i = i+1
            else:
                j = j-1
        return maxarea
            
