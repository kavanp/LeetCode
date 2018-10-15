
class Solution(object):
    def threeSum(self, nums):
        sol = []
        for i in range(len(nums)):
            a = nums[i]
            for j in range(0,len(nums)):
               # if j!=i:
                    b = nums[j]
                    for k in range(0,len(nums)):
                        #if k!=j and k!=i:
                            c = nums[k]
                            if (a+b+c) == 0:
                                if a == -2:
                                    print (a,b,c)
                                temp = [a,b,c]
                                #print (temp)
                                temp.sort()
                                a,b,c = temp
                                if [a,b,c] not in sol:
                            #print (self.checkuni(i,j,k,hashm),nums[i],nums[j],nums[k],hashm[i**2 + j**2 + k**2])
                            #if [a,b,c] not in sol:
                                    sol.append([a,b,c])
        print (i,j,k)
        return sol
