import random

class Solution:

    def __init__(self, nums):
        self.initNums = nums.copy()
        self.nums = nums

    def reset(self):
        return self.initNums

    def shuffle(self):
        n = len(self.nums)
        for i in range(n):
            index = random.randint(0, n - 1)
            tmp = self.nums[i]
            self.nums[i] = self.nums[index]
            self.nums[index] = tmp
        return self.nums
        
def main():
    nums = [-6,10,184]
    sol = Solution(nums)
    print(sol.reset())
    print(sol.shuffle())
    
main()
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()