class Solution:         
    def findMin(self, nums):
        if len(nums) < 3:
            return min(nums)
        else:
            mid = int((len(nums))/2)
            print (mid,nums[mid])
            if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                return nums[mid]
            else:
                self.findMin(nums[0:mid])
                self.findMin(nums[mid:])
