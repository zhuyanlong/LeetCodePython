class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            #i=0 is the first position.
            #nums[i]>nums[i-1] can not repeat
            if nums[i]>0:
                break
            if i==0 or nums[i]>nums[i-1]:
                left=i+1
                right=len(nums)-1
                while left<right:
                    if nums[left]+nums[right]==-nums[i]:
                        if len(res)==0 or [nums[i],nums[left],nums[right]]!=res[-1]:
                            res.append([nums[i],nums[left],nums[right]])
                        left+=1
                        right-=1
                    elif nums[left]+nums[right]<-nums[i]:
                        while nums[left]==nums[left+1] and left<len(nums)-2:
                            left=left+1
                        left+=1
                    else:
                        while nums[right]==nums[right-1] and right>0:
                            right=right-1
                        right-=1
        return res