from collections import defaultdict

class Solution:
    def getDigits(self,n):
        self.nDigits = 0
        if n < 10:
            return 1
        while n >= 1:
            n = n/10
            self.nDigits = self.nDigits + 1
        return self.nDigits
    
    def largestNumber(self, nums):
        result = ''
        self.d = defaultdict(int)
        self.maxNumber = max(nums)
        self.maxNumberDigits = self.getDigits(self.maxNumber)
        
        for i in range(len(nums)):
            self.numberDigits = self.getDigits(nums[i])
            self.d[nums[i]] = self.numberDigits
            while self.numberDigits < self.maxNumberDigits:
                nums[i] = nums[i]*10
                self.numberDigits = self.numberDigits + 1

        nums2 = nums
        nums2.sort(reverse= True)
        # get indices in hash map!
        # get number and indices in another hash map ===> JOIN!! 
        #return nums2,self.d
        print(nums2,self.d)
        for i in range(len(nums2)-1):
            print(nums2[i])
            if nums2[i] != nums2[i+1]:
                while self.getDigits(nums2[i]) > self.d[nums2[i]]:
                    nums2[i] = nums2[i]/10
                result+= str(int(nums2[i]))
        while self.getDigits(nums2[i+1]) > self.d[nums2[i+1]]:
                    nums2[i+1] = nums2[i+1]/10
        result += str(int(nums2[i+1]))
        return result
                
                
    
