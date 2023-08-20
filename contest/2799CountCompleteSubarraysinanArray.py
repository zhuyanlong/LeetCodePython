class Solution:
    def countCompleteSubarrays(self, nums):
        cnt = len(set(nums))
        res = 0
        i = 0
        j = i + 1
        while i < len(nums) and j < len(nums):
            if set(nums[i, j]) == cnt:
                res += nums - j + 1
                i += 1
                j = i + 1
                continue
            j += 1
        print(res)
    
def main():
    sol = Solution()
    nums = [1,3,1,2,2]
    sol.countCompleteSubarrays(nums)

main()