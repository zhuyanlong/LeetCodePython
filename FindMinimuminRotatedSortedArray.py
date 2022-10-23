class Solution:
    def findMin(self, nums):
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
            print(left,mid,right)
        return nums[left]

# 21.11.07新解，其实是一样的，只是拆分了条件判断
class Solution:
    def findMin(self, nums):
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>=nums[left] and nums[mid]<nums[right]:
                return nums[left]
            if nums[mid]>=nums[left] and nums[mid]>nums[right]:
                left=mid+1
            if nums[mid]<=nums[left] and nums[mid]<nums[right]:
                right=mid
        return nums[left]

def main():
    s=Solution()
    nums=[4,5,6,7,0,1,2]
    print(s.findMin(nums))

main()