class Solution:
    def twoSum(self, nums, target):
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=i
        # print(dic)
        for i in range(len(nums)):
            tmp=target-nums[i]
            if tmp in dic and i!=dic[tmp]:
                return [i,dic[tmp]]
        return []

def main():
    nums=[3,2,4]
    target=6
    s=Solution()
    print(s.twoSum(nums,target))

main()
