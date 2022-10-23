class Solution:
    def search(self, nums, target):
        m=0
        n=len(nums)-1
        res=self.binarySearch(m,n,nums,target)
        return res

    def binarySearch(self,m,n,nums,target):
        if m>n:
            return -1
        k=(m+n)//2
        if nums[k]<target:
            return self.binarySearch(k+1,n,nums,target)
        elif nums[k]>target:
            return self.binarySearch(m,k-1,nums,target)
        else:
            return k


def main():
    nums = [-1,0,3,5,9,12,13]
    target=8
    sol=Solution()
    res=sol.search(nums,target)
    print(res)

main()