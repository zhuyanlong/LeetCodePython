class Solution:
    def combinationSum3(self, k, n):
        result=[]
        stack=[]
        re=[]
        if k==0 or n==0:
            return []
        for i in range(1,10):
            if i*k+(k*(k-1))//2<=n:
                stack.append((i,0))
            else:
                break
        while stack:
            tmp=stack.pop()
            while stack[-1][1]!=tmp[1]:
                stack.pop()
            while len(re)!=tmp[1]:
                re.pop()
            re.append(tmp[0])
            if sum(re)==n:
                result.append(re.copy())
            for i in range(tmp[0]+1,10):
            #等差数列求和
                if i*(k-tmp[1]-1)+((k-tmp[1]-1)*(k-tmp[1]-2))//2<=n-tmp[0]:
                    stack.append((i,tmp[1]+1))
            print(re)

def main():
    s=Solution()
    k=3
    n=7
    s.combinationSum3(k,n)

main()
