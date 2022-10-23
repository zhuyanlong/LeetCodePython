class Solution:
    def mySqrt(self, x):
        for i in range(x+1):
            if i*i<=x and (i+1)*(i+1)>x:
                return i

def main():
    x=0
    sol=Solution()
    res=sol.mySqrt(x)
    print(res)

main()