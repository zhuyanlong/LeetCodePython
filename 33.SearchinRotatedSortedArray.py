class Solution:
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            #这个条件成立，左半段有序，在左边查找
            if nums[mid]>=nums[left]:
                if target>=nums[left] and target <nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            elif nums[mid]<nums[right]:
                if target<=nums[right] and target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
        return -1