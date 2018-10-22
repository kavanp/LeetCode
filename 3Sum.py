class Solution:
    def check(self,nums,i,j,table,result,c):
        flag = 0
        a = [nums[i],nums[j],c]
        a.sort()
        for q in table:
            if q == a:
                flag = 1
        if flag == 0:
            table.append(a)
            result.append([nums[i],nums[j],c])
        
        
    def threeSum(self, nums):
        #n = copy.deepcopy(nums)
        hashm = dict.fromkeys(nums,1)
        result = []
        table = []
        #flag = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if j!=i:
                    c = -nums[i] - nums[j]
                    if hashm.get(c):
                        #print (c)
                        if c==0 and nums.count(0) > 2:
                            self.check(nums,i,j,table,result,c)
                                                        
                        if nums.index(c)!=nums.index(nums[i]) and nums.index(c)!=nums.index(nums[j]):
                            self.check(nums,i,j,table,result,c)                    
        return result#,table
