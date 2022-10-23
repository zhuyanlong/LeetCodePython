class Solution:
    def findDuplicate(self, nums):
        slow=0
        fast=0
        t=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            print(slow,fast)
            if slow==fast:
                break
        while True:
            slow=nums[slow]
            t=nums[t]
            if slow==t:
                break
            print(slow,t)
        print(slow)

def main():
    nums=[1,3,4,2,2]
    s=Solution()
    s.findDuplicate(nums)

main()