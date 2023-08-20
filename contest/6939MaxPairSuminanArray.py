# 没看懂题目
class Solution:
    def maxSum(self, nums):
        res = set()
        maxVal = -1
        for i in range(len(nums)):
            s = self.digitSum(nums[i])
            if s in res:
                if s > maxVal:
                    maxVal = s
            else:
                res.add(s)
        return maxVal
        
    def digitSum(self, num):
        s = 0
        while num != 0:
            s += num % 10
            num //= 10
        return s
            
    
def main():
    nums = [51,71,17,24,42]
    sol = Solution()
    res = sol.maxSum(nums)
    print(res)

main()