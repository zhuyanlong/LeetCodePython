class Solution:
    def combinationSum(self, candidates, target):
        result=[]
        re=[]
        stack=[]
        for item in candidates:
            if item<=target:
                stack.append((0,item))
        while stack:
            tmp=stack.pop()
            # print("tmp",tmp)
            while len(re)!=tmp[0]:
                re.pop()
            re.append(tmp[1])
            # print("re",re)
            for item in candidates:
                if item <= target-sum(re) and item >= re[-1]:
                    stack.append((tmp[0]+1,item))
            if sum(re)==target:
                result.append(re.copy())
            # print("stack",stack)
        print(result)
        return result

def main():
    s=Solution()
    candidates = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    target = 20
    s.combinationSum(candidates,target)

main()