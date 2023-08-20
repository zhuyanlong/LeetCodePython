class Solution:
    def shuffle(self, nums, n):
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n + i])
        return res
    
def main():
    nums = [1,1,2,2]
    n = 2
    sol = Solution()
    print(sol.shuffle(nums, n))

main()