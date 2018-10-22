class Solution:
    def find132pattern(self, nums):
        if len(nums) == 0:
            return False
        minn = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < minn:
                minn = nums[i]
            for j in range(len(nums)-1,i-1,-1):
                if nums[j] < nums[i] and nums[j] > minn:
                    return True
        return False
                
                
