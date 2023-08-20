class Solution:
    def majorityElement(self, nums):
        numDict = {}
        for item in nums:
            if item not in numDict:
                numDict[item] = 1
            else:
                numDict[item] += 1
            if numDict[item] > len(nums) // 2:
                return item
        return nums[0]
    
def main():
    nums = [2, 2, 1, 1, 1, 2, 2]
    sol = Solution()
    res = sol.majorityElement(nums)
    print(res)

main()