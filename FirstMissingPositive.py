#放弃这道题了，感觉目前还是有点难，而且算法特殊，不太适合现在做
class Solution:
    def firstMissingPositive(self, nums):
        n=len(nums)
        for i in range(n):
            if nums[i]<=0:
                nums[i]=n+2
        print(nums)

def main():
    s=Solution
    nums=[1,2,0]
    print(s.firstMissingPositive(s,nums))

main()

