# 仍旧是错的，这种方式只能用来求解奇偶交错的场景
class Solution:
    def longestAlternatingSubarray(self, nums, threshold):
        res = 1
        for i in range(len(nums) - 1):
            cnt = 1
            if nums[i] % 2 != 0:
                continue
            for j in range(i, len(nums) - 1):
                if nums[j] <= threshold and nums[j + 1] <= threshold:
                    if (nums[j] % 2 == 0 and nums[j + 1] % 2 != 0) or (nums[j] % 2 != 0 and nums[j + 1] % 2 == 0):
                        cnt += 1
                    else:
                        break
                if cnt > res:
                    res = cnt
        if res == 1:
            for item in nums:
                if item % 2 == 0 and item <= threshold:
                    return 1
            return 0
        return res
    
def main():
    nums = [1, 2]
    threshold = 2
    sol = Solution()
    res = sol.longestAlternatingSubarray(nums, threshold)
    print(res)

main()