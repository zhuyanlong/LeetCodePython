# 没看懂代码
class Solution:
    def minDeletion(self, nums):
        j = 0
        for i in range(len(nums) - 1):
            k = i - j
            if k % 2 == 0 and nums[i] == nums[i + 1]:
                j += 1
        return j + (len(nums) - j) % 2
        
def main():
    nums = [1, 1, 2, 2, 3, 5]
    sol = Solution()
    res  = sol.minDeletion(nums)
    print(res)
    
main()