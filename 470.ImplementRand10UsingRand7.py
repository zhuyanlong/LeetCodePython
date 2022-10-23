import random

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        res=(rand7()-1)*7+rand7()
        while res>40:
            res=(rand7()-1)*7+rand7()
        return res%10+1

def rand7():
    return random.randint(1,7)

def main():
    sol=Solution()
    res=sol.rand10()
    print(res)

main()

# 1到40怎么生成1到10
# x%10+1

# https://career.huawei.com/reccampportal/portal4_index.html#!portal/usercenter4/recruitmentProgress/recruitmentProgress.html