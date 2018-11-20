class Solution:
    def maxProduct(self, nums):
        a=1
        i=0
        if len(nums) == 1:
            return nums[0]
        mul = [-1]*len(nums)
        for i in range(len(nums)):
            #print (i)
            mul[i] = nums[i]
            j = i
            for j in range(i,-1,-1):
                #print ("-",j)
                a = a*nums[j]
                #print (a)
                if a > mul[i]:
                    mul[i] = a
            a = 1
        return max(mul)
                                
                
        
                
        
