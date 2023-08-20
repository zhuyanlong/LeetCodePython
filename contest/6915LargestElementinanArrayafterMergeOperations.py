class Solution:
    def maxArrayValue(self, nums):
        largest = float('-inf')  # Initialize largest as negative infinity

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                largest = max(largest, nums[i])
            else:
                nums[i + 1] = nums[i] + nums[i + 1]

        return max(largest, nums[-1])
    
def main():
    nums = [2,3,7,9,3]
    sol = Solution()
    print(sol.maxArrayValue(nums))
    
main()