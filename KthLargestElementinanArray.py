#基本上把时间复杂度保持在O(nlgn)就可以了，空间复杂度要低一些
# class Solution:
#     def findKthLargest(self, nums, k):
#         nums.sort()
#         return nums[-k]

#采用堆排序的思想，可以原地排序，并且时间复杂度在O(nlgn)
class Solution:
    def findKthLargest(self, nums, k):
        nums.insert(0,0)
        n=len(nums)
        #建立堆
        for i in range(2,n):
            m=i
            while m>1 and nums[m]>nums[m//2]:
                nums[m],nums[m//2]=nums[m//2],nums[m]
                m=m//2
        m=k
        while m>0:
            nums[1],nums[n-1]=nums[n-1],nums[1]
            # print(nums[n-1])
            n-=1
            i=1
            #这里的n-1是最后一个元素的下标
            while 2*i<=n-1:
                j=2*i
                if j<n-1:
                    if nums[j]<nums[j+1]:
                        j+=1
                if nums[i]>=nums[j]:
                    break
                nums[i],nums[j]=nums[j],nums[i]
                i=j
            m-=1
        # print(nums)
        return nums[-k]

def main():
    s=Solution()
    nums=[0,1,0,90,89,88,87,86,85,84,83,82,81]
    k=3
    print(s.findKthLargest(nums,k))

main()